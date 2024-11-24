from service import FrameService, ImageProcessor
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
from io import BytesIO
from config import DBConfig
import base64
import sqlite3
import pandas as pd
import os
from typing import List, Dict, Any
from db_service import DatabaseHandler


app = FastAPI(
    title="Image Data API",
    description="API to fetch and process image frames based on depth, with pagination.",
)




# API Endpoint
@app.get("/frames/", description="Fetch image frames between depth_min and depth_max with pagination.")
def fetch_frames(
    depth_min: float = Query(..., description="Minimum depth value."),
    depth_max: float = Query(..., description="Maximum depth value."),
    offset: int = Query(0, description="Offset for pagination."),
    limit: int = Query(10, description="Number of records to fetch."),
):
    # Dependency Injection
    db_handler = DatabaseHandler(db_path= DBConfig.PATH)
    image_processor = ImageProcessor()
    frame_service = FrameService(db_handler, image_processor)
    frames = frame_service.get_frames(depth_min, depth_max, offset, limit)
    return {
        "total_frames": len(frames),
        "offset": offset,
        "limit": limit,
        "frames": frames,
    }
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
from io import BytesIO
from config import DBConfig
import base64
import sqlite3
import pandas as pd
from typing import List, Dict, Any
from db_service import DatabaseHandler




class ImageProcessor:
    """Processes image data and converts it to base64."""
    @staticmethod
    def apply_colormap(image_array: Any) -> str:
        fig, ax = plt.subplots(figsize=(8, 1))
        ax.imshow(image_array, cmap='viridis', aspect='auto')
        ax.axis('off')
        
        # Convert plot to base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
        buffer.seek(0)
        base64_image = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close(fig)
        return base64_image


class FrameService:
    """Handles the business logic for fetching frames."""
    def __init__(self, db_handler: DatabaseHandler, image_processor: ImageProcessor):
        self.db_handler = db_handler
        self.image_processor = image_processor

    def get_frames(self, depth_min: float, depth_max: float, offset: int, limit: int) -> List[Dict]:
        query = f"""
        SELECT * FROM image_data
        WHERE depth BETWEEN {depth_min} AND {depth_max}
        LIMIT {limit} OFFSET {offset}
        """
        data = self.db_handler.execute_query(query)

        if data.empty:
            raise HTTPException(status_code=404, detail="No frames found for the given range.")

        frames = []
        for _, row in data.iterrows():
            image_array = row.iloc[1:].to_numpy().reshape(1, -1)
            base64_image = self.image_processor.apply_colormap(image_array)
            frames.append({
                "depth": row["depth"],
                "image_base64": base64_image,
            })

        return frames



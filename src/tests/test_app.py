import pytest
from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is in the 'main.py' file

# Create a TestClient for FastAPI app
client = TestClient(app)
 
  
def test_fetch_frames_invalid_params():
    # Set invalid depth range (depth_min > depth_max)
    depth_min = 10.0
    depth_max = 5.0
    offset = 0
    limit = 10
    
    # Call the endpoint
    response = client.get(
        "/frames/",
        params={
            "depth_min": depth_min,
            "depth_max": depth_max,
            "offset": offset,
            "limit": limit,
        },
    )
    
    # Check if status code is 400 for bad request
    assert response.status_code == 404

# Test case for missing query parameters
def test_fetch_frames_missing_params():
    # Call the endpoint without necessary query params
    response = client.get("/frames/")
    
    # Check if status code is 422 for unprocessable entity (missing params)
    assert response.status_code == 422

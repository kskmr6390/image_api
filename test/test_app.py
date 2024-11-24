import pytest
from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is in the 'main.py' file

# Create a TestClient for FastAPI app
client = TestClient(app)

# Test case to fetch image frames with pagination and depth filters
def test_fetch_frames():
    # Set test parameters
    depth_min = 9000
    depth_max = 9001
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
    
    # Check the status code
    assert response.status_code == 200
    
    # Check if the response JSON structure is as expected
    response_json = response.json()
    assert "total_frames" in response_json
    assert "offset" in response_json
    assert "limit" in response_json
    assert "frames" in response_json
    
    # Check that the total frames is not negative
    assert response_json["total_frames"] >= 0
    
    # Check if frames are returned (this will depend on your test data setup)
    if response_json["total_frames"] > 0:
        assert isinstance(response_json["frames"], list)
        assert len(response_json["frames"]) == response_json["limit"]
    else:
        # If no frames match the filter, ensure frames is an empty list
        assert response_json["frames"] == []

# Test case when invalid parameters are passed
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
    assert response.status_code == 400

# Test case for missing query parameters
def test_fetch_frames_missing_params():
    # Call the endpoint without necessary query params
    response = client.get("/frames/")
    
    # Check if status code is 422 for unprocessable entity (missing params)
    assert response.status_code == 422

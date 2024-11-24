# Writing test cases using pytest
test_code = """
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_fetch_frames_valid_range():
    response = client.get("/frames/?depth_min=9000.1&depth_max=9000.5")
    assert response.status_code == 200
    data = response.json()
    assert "frames" in data
    assert len(data["frames"]) > 0

def test_fetch_frames_no_results():
    response = client.get("/frames/?depth_min=0&depth_max=1")
    assert response.status_code == 404
    data = response.json()
    assert data["message"] == "No frames found for the given range."
"""

# Writing the README.md file
readme_content = """
# # Image Data API

# ## Description
# This project provides an API to process and fetch image frames based on depth values. The images are resized, stored in a database, and served with a custom colormap.

# ## Features
# - Resize images from width 200 to 150 pixels.
# - Store resized images in an SQLite database.
# - Fetch image frames between specified depth ranges.
# - Apply a custom colormap (`viridis`) to images.

# ## Requirements
# - Python 3.8+
# - Dependencies listed in `requirements.txt`

# ## Setup
# 1. Clone this repository and navigate to the project directory.
# 2. Install dependencies:
#    ```bash
#    pip install -r requirements.txt


# Image Data Processing API

## **Live Application**

You can access the deployed API here:  
[https://images-api-data-processing-57e171f4a71a.herokuapp.com/docs](https://images-api-data-processing-57e171f4a71a.herokuapp.com/docs)

## **API Documentation**

Explore the API endpoints and their details using the following documentation interfaces:

- **Swagger UI:** [https://images-api-data-processing-57e171f4a71a.herokuapp.com/docs](https://images-api-data-processing-57e171f4a71a.herokuapp.com/docs)
- **ReDoc:** [https://images-api-data-processing-57e171f4a71a.herokuapp.com/redoc](https://images-api-data-processing-57e171f4a71a.herokuapp.com/redoc)



## Description
This project provides a FastAPI-based solution for processing image data stored in a CSV file. It includes the following features:
- Resizing image data (from 200 pixels wide to 150 pixels wide).
- Storing resized images in an SQLite database.
- Providing an API to fetch image frames based on a depth range.
- Applying a custom colormap (`viridis`) to the image frames.

---

## Features
1. Resize images from width 200 to 150 pixels.
2. Store resized images and their depth values in an SQLite database.
3. Fetch image frames between specified depth ranges using an API.
4. Serve images with a custom colormap applied.

---

## Requirements
- Python 3.8+
- Libraries:
  - `fastapi`
  - `uvicorn`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `pytest`

---

## Setup and Installation

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/kskmr6390/image_api
```

### Docker build & run

```bash

docker build -t image-data-api .
docker run -p 8000:8000 image-data-api
```


### API Docs Referance
#### docs refs: http://0.0.0.0:8000/docs

###  Step 1 : Create Virtual env and activate

```bash
cd src
python3 -m venv env
source env/bin/activate
```

### Step 2 : Install all requirements
```bash
pip install -r requirements.txt

```

### Step 3:  Resize images & load data to DB
```bash
 python3 resize_images.py

```
### Step 4: Run the servr run 
```bash
 uvicorn app:app --reload




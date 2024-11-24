FROM python:3.10-slim

# Set the working directory for the app
WORKDIR /app

# Copy the contents of the current directory to the container's /app directory
COPY . /app



# Change to the src directory
WORKDIR /app/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the image_resize script
# Install dependencies

RUN python resize_images.py

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

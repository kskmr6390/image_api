import sqlite3
import numpy as np
from scipy.ndimage import zoom
import pandas as pd
from config import DBConfig, ImageData
from db_service import DatabaseHandler


class ImageResizer:
    def __init__(self, original_width, new_width):
        self.original_width = original_width
        self.new_width = new_width

    def resize(self, row):
        """Resizes a single row of image data."""
        image = np.array(row, dtype=np.float32)
        zoom_factor = self.new_width / self.original_width
        return zoom(image, zoom_factor)


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Load data from CSV and return as DataFrame."""
        df = pd.read_csv(self.file_path)
        return df


class ImageDataProcessor:
    def __init__(self, data_loader, image_resizer, db_handler):
        self.data_loader = data_loader
        self.image_resizer = image_resizer
        self.db_handler = db_handler

    def process_data(self):
        # Load the image data
        df = self.data_loader.load_data()
        
        # Extract image data (exclude depth column)
        image_data = df.iloc[:, 1:]
        
        # Resize the images
        resized_images = image_data.apply(self.image_resizer.resize, axis=1, result_type='expand')
        resized_images.columns = [f'pixel_{i+1}' for i in range(self.image_resizer.new_width)]
        
        # Combine with the depth column
        resized_df = pd.concat([df[['depth']], resized_images], axis=1)

        # Save the resized data to the database
        self.db_handler.save_to_db(resized_df)

        return f"Resized images saved to database at {self.db_handler.db_path}."



if __name__ == "__main__":
    # Configure paths
    file_path = ImageData.PATH
    db_path = DBConfig.PATH

    # Create necessary instances
    data_loader = DataLoader(file_path)
    image_resizer = ImageResizer(original_width=200, new_width=150)
    db_handler = DatabaseHandler(db_path)

    # Process the data
    processor = ImageDataProcessor(data_loader, image_resizer, db_handler)
    result = processor.process_data()

    print(result)

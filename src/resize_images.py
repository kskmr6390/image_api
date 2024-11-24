import sqlite3
import numpy as np
from scipy.ndimage import zoom
import pandas as pd


#get data
file_path = './data/img_data.csv'
df = pd.read_csv(file_path)
    # Display basic information about the dataset to understand the structure
df.info(), df.head()


# Step 1: Resize the image width from 200 to 150
def resize_image(row, original_width=200, new_width=150):
    """Resizes a single row of image data."""
    image = np.array(row, dtype=np.float32)
    zoom_factor = new_width / original_width
    resized_image = zoom(image, zoom_factor)
    return resized_image

# Extract image data and resize
image_data = df.iloc[:, 1:]  # Exclude depth column
resized_images = image_data.apply(resize_image, axis=1, result_type='expand')
resized_images.columns = [f'pixel_{i+1}' for i in range(150)]

# Combine with depth column
resized_df = pd.concat([df[['depth']], resized_images], axis=1)

# Step 2: Store resized data in SQLite database
db_path = '/Users/satyam/Desktop/satyam/data/images.db'
conn = sqlite3.connect(db_path)

# Save to SQLite
resized_df.to_sql('image_data', conn, if_exists='replace', index=False)
conn.close()

f"Resized images saved to database at {db_path}."

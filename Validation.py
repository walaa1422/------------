import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow import keras

# Load the trained model
model_save_path = 'C:/Users/96655/Desktop/inception1_model-acc93.h5'
loaded_model = keras.models.load_model(model_save_path)

# Define possible classes (broken and intact)
class_labels = ["There is a fracture", "There is no fracture"]

# Function to classify the image
def classify_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    predictions = loaded_model.predict(img)
    class_index = np.argmax(predictions)
    class_label = class_labels[class_index]

    return class_label

# Function to open file dialog and select an image
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        load_and_display_image(file_path)
        result = classify_image(file_path)
        result_label.config(text=f"Image Classification: {result}")

# Function to load and display the selected image
def load_and_display_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

# Set up the application window
app = tk.Tk()
app.title("Upload and Classify Image")
app.geometry("400x570")  # Adjusted height for better appearance

# Create a title for the application
title_label = tk.Label(app, text="Upload and Classify Images", font=("Arial", 24), bg="#f0f0f0")
title_label.pack(pady=20)

# Create a button to choose the image
open_button = tk.Button(app, text="Choose Image", command=open_file_dialog, font=("Arial", 14))
open_button.pack(pady=20)

# Create an element to display the selected image
image_label = tk.Label(app)
image_label.pack()

# Create an element to display the image classification
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=20)  # Added padding for better spacing

# Run the application
app.mainloop()

# Resume Data Extraction Project

This project focuses on automating the extraction of key information from resumes (CVs) using Deep Learning techniques. The goal is to streamline the recruitment process by efficiently processing CVs and extracting relevant data.

## Overview

The project is divided into two main components:

1. **YOLO Model Training:**
   - The `YOLO_train.ipynb` notebook combines data preprocessing and YOLOv8 model training.
   - It covers tasks such as data exploration, cleaning, formatting, and YOLO model configuration for recognizing and locating specific CV blocks.

2. **Flask Visualization Project:**
   - The `flask_app` directory contains a mini Flask project for visualizing the results of the trained YOLO model.
   - This web application allows users to upload a resume (PDF or photo) and visually see the extracted information.

## How to Use

1. **YOLO Model Training:**
   - Open and run the `YOLO_train.ipynb` notebook to preprocess the data and train the YOLOv8 model.

2. **Flask Visualization Project:**
   - Clone the project repository.
   - Navigate to the `flask_app` directory.
   - Install dependencies using `pip install -r requirements.txt`.
   - Run the Flask app with `flask run`.
   - Access the visualization interface in your browser.

## Folder Structure

- `YOLO_train.ipynb`: Jupyter notebook for data preprocessing and YOLOv8 model training.
- `venv`: Mini Flask project for visualizing YOLO model results.

## Note Regarding PDF Files

While the YOLO model and Flask visualization project are designed to handle image-based resumes, it currently encounters errors when processing resumes in PDF format. To ensure smooth operation, we recommend using only image files (e.g., JPEG, PNG) for the extraction process.

We are actively working on enhancing PDF support for future updates. In the meantime, please convert your resumes to image format before uploading them to the Flask visualization interface.

Thank you for your understanding and cooperation.

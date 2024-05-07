## Introduction to Face Mask Detection using YOLOv8

This project focuses on leveraging YOLOv8, a state-of-the-art object detection algorithm, to detect faces and classify whether individuals are wearing masks correctly, incorrectly, or not wearing masks at all. The dataset used for this project is sourced from Kaggle and includes annotated images of people with various mask-wearing scenarios.

**Dataset Source:** [Kaggle Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection/data)

### Objective
The main goal of this project is to develop an accurate and efficient system for face mask detection in real-time scenarios. By training the YOLOv8 model on this dataset, we aim to create a robust solution capable of identifying faces and determining whether masks are being worn correctly or not.

### Key Components
1. **YOLOv8 Model:** YOLOv8 is a popular and powerful object detection model known for its speed and accuracy in detecting objects in images and videos. We have customized and trained the YOLOv8 model specifically for face mask detection in this project.
   
2. **Training Data:** The training data comprises annotated images of individuals with varying mask-wearing behaviors, including wearing masks correctly, wearing masks incorrectly, and not wearing masks at all. These annotations help the model learn to recognize different mask-related classes accurately.

### Project Workflow
1. **Data Preparation:** Cleaning and annotating the dataset to ensure accurate training data for the YOLOv8 model.
   
2. **Model Training:** Training the YOLOv8 model on the annotated dataset to learn the features necessary for face mask detection.

3. **Evaluation:** Evaluating the trained model's performance using metrics such as precision, recall, and accuracy to assess its effectiveness in real-world scenarios.

4. **Deployment:** Deploying the trained model for real-time face mask detection applications, which can be utilized in various settings like public spaces, workplaces, and security systems.

## Face Mask Detection Dataset

This repository contains the dataset and preprocessing scripts used for training a YOLOv8 model for face mask detection. The dataset structure is organized as follows:

Mask_Dataset/
│
├── train/                 # Training images and annotations
│   ├── image1.png
│   ├── image2.png
│   ├── ...
│   └── imageN.png
│   ├── annotation1.txt    # Corresponding annotations in YOLO format
│   ├── annotation2.txt
│   ├── ...
│   └── annotationN.txt
│
└── val/                   # Validation images and annotations
    ├── image1.png
    ├── image2.png
    ├── ...
    └── imageN.png
    ├── annotation1.txt    # Corresponding annotations in YOLO format
    ├── annotation2.txt
    ├── ...
    └── annotationN.txt

### Dataset Overview
- **Images:** The dataset contains images of individuals with varying mask-wearing scenarios. Images are named in the format `maksssksksssX.png`.
  
- **Annotations:** Annotations are provided in YOLO format and correspond to each image in the dataset. Annotation files are named similarly to image files (`maksssksksssX.txt`).

### Preprocessing
The dataset preprocessing includes:
1. **Label Mapping:** Conversion of label names to numeric IDs using a custom module in the `Pre-Process` folder.
2. **Annotation Format:** Conversion of annotations from Pascal VOC format to YOLO format using another module in the `Pre-Process` folder.

### Important Note
- **Dataset Consistency:** Due to various reasons, there might be mismatches or errors in the dataset, such as missing or inaccurate annotations for some images. It is essential to review the dataset and annotations, especially during training, to ensure data consistency and model accuracy.

## Training and Evaluating the Model

### Training the Model

1. **Data Preparation:** Ensure that your dataset is organized according to the specified structure, with training images and corresponding annotations in the `Mask_Dataset/train/` directory.

2. **Training Script:** Run the `trainer.py` script to initiate the training process. This script contains the necessary configurations for training the model, including data paths, hyperparameters, and training settings.

3. **Training Process:** During training, the model iteratively learns from the training data to improve its ability to detect masks in images. The training progress, including loss metrics and performance indicators, will be displayed during the training process.

4. **Checkpoint Saving:** The trained model checkpoints will be saved periodically during training. These checkpoints capture the model's state at different training epochs, allowing you to resume training or evaluate the model later.

5. **Completion:** Once the training process completes the specified number of epochs or reaches convergence criteria, the training script will finish execution.

### Checking the Results

1. **Output Directory:** Navigate to the `Runs/` folder in your project directory. This folder contains subdirectories corresponding to different training runs or experiments.

2. **Results Analysis:** Inside each run's directory, you can find logs, metrics, and trained model files. Analyze the training logs to understand the model's performance metrics such as loss values, accuracy, precision, recall, and other relevant metrics.

3. **Model Evaluation:** Use the trained model files to evaluate the model's performance on validation or test datasets. The evaluation process may involve running inference on validation images, calculating metrics such as mAP (mean Average Precision), and visualizing detection results.

4. **Iterative Improvement:** Based on the evaluation results, you can fine-tune hyperparameters, adjust model architectures, or perform data augmentation to improve model performance further. Iterate this process until you achieve satisfactory results.

By following these steps, you can effectively train your model to detect masks in images and assess its performance through thorough result analysis.

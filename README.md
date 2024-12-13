# Automated Waste Sorting Management System

This repository contains the code, design, and documentation for the **Automated Waste Sorting Management System**, a final year major project developed using **OpenCV**, **deep learning (CNN)**, and **Arduino** to classify and manage waste effectively. The system classifies waste into four categories: **glass, metal, paper, and plastic**, ensuring efficient recycling and waste management.



## Introduction
The **Automated Waste Sorting Management System** aims to address the growing need for efficient and environmentally friendly waste management. By leveraging **deep learning models** and **embedded systems**, this project automates the sorting of recyclable materials, reducing manual labor and improving accuracy.

## Features
- **Real-Time Waste Classification**: Classifies waste into four categories (glass, metal, paper, plastic) using a trained CNN model.
- **Hardware Integration**: Uses **Arduino** to control motors for waste sorting into designated bins.
- **Voice Feedback**: Provides audio feedback about the classification result.
- **Cost-Efficient Design**: Built using affordable components and open-source tools.

## System Overview
The system includes the following components:
1. **Camera Module**: Captures the image of waste.
2. **Deep Learning Model**: A pre-trained CNN model for waste classification.
3. **Arduino Uno**: Controls the motorized mechanism to sort waste into bins.
4. **Voice Module (Optional)**: Provides voice feedback based on classification results.

## Technologies Used
- **Programming Languages**: Python, C++ (for Arduino)
- **Deep Learning Framework**: TensorFlow (via Google Teachable Machine)
- **Computer Vision**: OpenCV
- **Microcontroller**: Arduino Uno
- **Dataset**: Kaggle Dataset for waste classification

## Hardware Requirements
- **Arduino Uno**
- **Servo Motors** (2 or more)
- **Camera Module**
- **Breadboard and Jumper Wires**
- **Power Supply**
- **Voice Module (Optional)**
- **Bins for Waste Sorting**

## Software Requirements
- **Python 3.10**
- **Arduino IDE**
- **PyCharm (or any Python IDE)**
- **Teachable Machine** (for training the model)
- Libraries: 
  - TensorFlow 2.13.0
  - OpenCV 4.10.0.81
  - NumPy
  - cvzone 1.5.6

## Architecture
1. **Image Capture**: A camera captures the image of waste.
2. **Classification**: The CNN model processes the image and predicts the waste category.
3. **Hardware Control**: The prediction is sent to the Arduino, which activates motors to sort the waste into appropriate bins.

## Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/RitikaKumari1234/automated-waste-sorting.git
cd automated-waste-sorting
```

### Step 2: Train or Use the Pre-Trained Model
- The trained model (`keras.h5`) is included in the repository.
- If you want to train your own model, use **Google Teachable Machine** .

### Step 3: Upload Arduino Code
1. Open the `code.txt` file in the Arduino IDE.
2. Connect your Arduino Uno via USB.
3. Upload the code to the board.

### Step 4: Run the System
1. Connect all hardware components as per the wiring diagram.
2. Run the Python script:
   ```bash
   python main.py
   ```

## How It Works
1. **Capture and Classification**:
   - A camera captures the waste image.
   - The image is processed by the CNN model to classify the waste.
2. **Hardware Interaction**:
   - The classification result is sent to the Arduino.
   - Based on the result, motors are activated to sort the waste into bins.
3. **Feedback**:
   - The system provides voice or visual feedback about the waste type.

## Results
- Achieved **80% accuracy** on the test dataset.
- Successfully integrated the hardware and software for real-time classification and sorting.

## Future Improvements
- Add more waste categories for better classification.
- Use a more robust hardware setup for industrial use.
- Implement cloud-based monitoring and analytics.



Feel free to contribute to this project.

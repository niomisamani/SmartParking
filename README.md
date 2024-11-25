# SmartParking 🚘🅿️🚧

## Overview
SmartParking is a project aimed at creating a system for automated vehicle parking detection. This system leverages computer vision techniques to recognize license plates, detect empty parking spots, and manage the parking flow efficiently. It can be used to improve parking efficiency and reduce human intervention in parking areas.

## Features
- **License Plate Recognition**: Utilizes machine learning and deep learning models to detect and recognize license plates.
- **Parking Slot Detection**: Identifies available parking slots and allocates them effectively.
- **Automatic Gate Management**: Can be extended to automate the entry and exit of vehicles based on recognition results.

## Technologies Used
- **Python**: Main programming language for the project.
- **OpenCV**: For image processing and vehicle detection.
- **TensorFlow/Keras**: Used for training and utilizing the deep learning model (`wpod-net.h5`) to detect license plates.
- **Flask** (optional): Can be used to create a web-based interface for managing the parking lot.

## Prerequisites
To run this project, you need to have the following installed:
- Python 3.7+
- TensorFlow
- OpenCV
- Flask (if you want to run a web interface)

Install the necessary dependencies using the following command:
```sh
pip install -r requirements.txt
```

## Project Structure
- **main.py**: Entry point for the SmartParking application.
- **detect.py**: Contains functions for vehicle and license plate detection.
- **functions.py**: Utility functions used across the project.
- **car_data.csv**: Dataset containing information about vehicles.
- **wpod-net.h5**: Pre-trained model used for license plate detection.
- **videos/**: Sample videos used for testing.
- **plates/**: Directory containing sample license plate images.

## Running the Project
To run the project, use the following command:
```sh
python main.py
```

This command will initiate the parking system, processing input video streams to detect and manage parking.

## How It Works
1. **Vehicle Detection**: The system takes input from video feeds and detects the incoming vehicles.
2. **License Plate Recognition**: Using the pre-trained `wpod-net.h5` model, the system detects and reads license plates.
3. **Parking Allocation**: Detects available slots and assigns parking spaces accordingly.

## Future Improvements
- **Cloud Integration**: Store data on cloud-based databases to make it accessible across locations.
- **Mobile App Integration**: Develop a mobile app to allow users to reserve parking slots in advance.
- **Gate Automation**: Integrate with hardware to manage physical barriers based on vehicle recognition.

## Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are reviewed on a regular basis.


## Acknowledgments
- **OpenCV** for providing a comprehensive set of computer vision tools.
- **TensorFlow/Keras** for facilitating model training and inference.
- **Community Contributors** who have helped improve this project.


---

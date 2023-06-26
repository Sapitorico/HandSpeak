# Dataset manager
## Image Collection Tool
The Image_Collection function is used to capture images from a camera feed and save them to a specified directory.
It utilizes the MediaPipe Hands library to detect hand landmarks in the captured images and allows the user to select which hand to capture.
The captured images are resized and saved to the specified directory in a format suitable for training a machine learning model.

### Prerequisites
Before using the image collection tool, make sure that you have the necessary dependencies installed

```shell
pip install -r requirements.txt
```

### Usage
Run the script through the terminal : Open a terminal or command prompt, navigate to the directory containing the Image_Collection.py file and run the following command:

```
python images_data_collector.py --id_cam <camera_id> --data_path <directory_path> --action <action> --img_size <image_size> --size_data <total_images> --num_hands <max_hands> --hand_type <hand_type> --capture_time <interval>
```

Replace the placeholders <camera_id>, <directory_path>, <action>, <image_size>, <total_images>, <max_hands>, <hand_type>, and <interval> with the appropriate values according to your requirements.

* --**id_cam**: The ID of the camera to capture images from. You can set it to 0 if you have only one camera connected.
* --**data_path**: The path to the directory where you want to save the captured images.
* --**action**: Specify the action being performed in the captured images. You can set it to a descriptive label (e.g., "nombe").
* --**img_size**: The size to resize the captured images to. Choose an appropriate value based on your model requirements.
* --**size_data**: The total number of images to capture. Decide how many images you want to collect for your dataset.
* --**num_hands**: The maximum number of hands to detect in the captured images. Set it according to your application.
* --**hand_type**: Specify the type of hand to capture. Valid options are "Left", "Right", or "all".
* --**capture_time**: The time interval between capturing images, in seconds. Adjust it as per your capturing needs.

The script will start capturing images from the camera feed and display the captured frames.
Capture Images: While the script is running, perform the desired hand action within the camera's view. The script will detect the hand landmarks and display a bounding box around the selected hand (if detected). Press the 's' key to save the captured hand image to the specified directory.
Exit the Script: To stop the image capturing process, press the 'esc' key. The script will release the camera feed and close all windows.

### Limitations
The accuracy of hand landmark detection depends on the camera feed quality and lighting conditions. Ensure sufficient lighting for better results.
The tool assumes the presence of a single hand or multiple hands (based on num_hands parameter) and may not work as expected in scenarios with overlapping or occluded hands.

## Dataset Subset Creator -tool
The Dataset Subset Creator is a Python script that allows you to create a subset of a given training dataset for machine learning purposes.
It copies a specified number of images per class from the training set to the subset directory and moves a specified percentage of those images to a validation set.

### Usage
Follow the steps below to use the Dataset Subset Creator:
Run the Script: Open a terminal or command prompt, navigate to the directory containing the DatasetSubsetCreator.py file, and run the following command:
```
python split_dataset.py --training_dir <dataset_path> --subset_dir <subset_path> --subset_num <num_images> --train_images_per_class <num_images> --validation_percentage <val_split>
```

## CreateDataset YOLO -tool
The CustomHandDataset class is used to create a custom dataset for hand detection or recognition tasks.
It takes input data directories for training and validation sets, and outputs a structured dataset with images and corresponding labels.

### Usage
Follow the steps below to use the CustomHandDataset class:
Open a terminal and navigate to the directory where the script containing the CustomHandDataset class is located.

Execute the following command, replacing the arguments with the corresponding values:
```
python base.py --data_dir_train <train_directory> --data_dir_val <val_directory> --output_dir <output_directory> --dataset_name <dataset_name> --img_size <image_size>
```
* --**data_dir_train**: The directory path for the training data.
* --**data_dir_val**: The directory path for the validation data.
* --**output_dir**: The directory path for the output dataset.
* --**dataset_name**: The name of the dataset directory.
* --**img_size** (optional): The desired size for the output images (default: 224).

### Limitations
The CustomHandDataset class assumes the input data directory structure follows a class-based organization, with each class having its own folder containing the respective images.
The hand detection model used in the class should be properly configured and available.
Additional modifications may be required to suit specific use cases or requirements.

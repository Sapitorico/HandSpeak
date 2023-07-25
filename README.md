# LSU models

## Alphabet model

The alphabetic model is a model trained to recognize the letters of the Uruguayan alphabet. It is trained with the [LSU dataset](https://hub.ultralytics.com/datasets/RWCFcZKsUlnnqG6igzem), the [Yolov8n](https://github.com/ultralytics/ultralytics) model has been used together with image processing techniques using [OpenCV](https://opencv.org) and [MediaPipe](https://developers.google.com/mediapipe/framework).

We adapted YOLOv8 so that it can detect hands and finger positions in images. We used a proprietary dataset that we created with the help of MediaPipe, an open source library for image analysis and pose detection. MediaPipe and OpenCV allowed us to capture real-time images of the hands and generate a dataset labeled with finger positions.

### Image processing and dataset creation

For image processing and dataset creation, we used the MediaPipe and OpenCV libraries. With MediaPipe, we were able to obtain the position of hands in the images in real time. We then used OpenCV to perform tasks such as cropping the hand images and color normalization.

In addition, we used MediaPipe and OpenCV to create the datasets required by YOLO. Initially, we created subfolders for each letter of the Uruguayan alphabet and stored the hand images corresponding to each letter in their respective subfolder. Then, we divided the training data into subfolders for training and validation, taking 25% of the images for validation. Next, we converted these sets of images to the format required by YOLO, which consists of a directory called "images" containing all the images and a directory called "labels" containing the annotation files in a specific format.

### Training

The training was carried out using Google Colab and PyTorch.

* Model evaluation: Once the training was completed, we evaluated the performance of the model using metrics such as accuracy, recall, and F1-score. These metrics helped us evaluate the model's ability to correctly recognize the letters of the Uruguayan alphabet in the hand images.
#### optimization
ONNX is an open and widely adopted format for representing machine learning models. It provides a standard way to exchange models between different machine learning frameworks and tools. You can use ONNX in your project to achieve interoperability and portability of trained models.
* Model saving: Finally, we saved the trained model in ONNX format in the "models" folder. This trained model will be used later in the real-time implementation to make predictions on the captured images.

Throughout the training process, we used monitoring tools such as ClearML, CometML, and Weight & Biases (W&B) to record and visualize metrics, save model checkpoints, and compare different iterations of the training. This allowed us to track progress in detail and make informed decisions to improve model performance.


### Real-time implementation

We again use the MediaPipe library to track the hand in real time. MediaPipe provides us with the necessary tools to capture the real-time image of the clipped hand as it moves and changes position.

Once the real-time image of the hand is obtained, we pass this image to the model.

Once the predictions have been made and processed, we can display the recognized letter on the user interface in real time, thus providing an interactive and practical tool for sign language recognition of the Uruguayan alphabet.

## CNN (Convolutional Neural Network) models

Deep learning is a field of artificial intelligence that focuses on learning and extracting meaningful representations from data. In the case of images, Convolutional Neural Networks (CNNs) play a crucial role in extracting relevant features and enabling tasks such as image classification, object detection, and image generation.

### How do CNNs work?

At its core, a CNN operates on the principles of pattern recognition and hierarchical feature learning. It is inspired by the organization and functionality of the human visual system. Let's understand the key components and steps involved:

#### Convolutional Layers:

The first step in a CNN involves passing the input image through one or more convolutional layers. These layers consist of a set of filters, also known as kernels, which are small matrices that scan the image. The filters highlight specific patterns or features present in the image, such as edges, textures, or shapes. The result is a set of feature maps that represent different extracted features.

### Pooling Layers:

After each convolutional layer, a pooling layer is often applied. Pooling helps reduce the spatial dimensions of the feature maps while retaining the most important information. The most common pooling operation is max pooling, which selects the maximum value from each local region of the feature map. This downsampling process reduces the computational complexity and makes the network more robust to variations in the input.

### Activation Function:

After each convolutional or pooling layer, an activation function is applied element-wise to introduce non-linearity into the network. The most commonly used activation function is the Rectified Linear Unit (ReLU), which sets negative values to zero and keeps positive values unchanged. This allows the network to learn complex, nonlinear relationships between features.

### Fully Connected Layers:

Following several convolutional and pooling layers, the feature maps are flattened into a vector and passed through one or more fully connected layers. These layers perform high-level reasoning and decision-making based on the learned features. The final layer typically uses an activation function such as softmax to produce the predicted probabilities for different classes in classification tasks.

### Training and Optimization:

CNNs are trained using labeled data through a process called backpropagation. This involves iteratively adjusting the network's parameters (weights and biases) to minimize the difference between predicted outputs and ground truth labels. Optimization algorithms, such as stochastic gradient descent (SGD) or its variants, are used to update the parameters and improve the model's performance.

# Transfer Learning

Transfer learning is a technique in deep learning that enables the use of pre-trained models as a starting point for solving new tasks or domains. Instead of training a model from scratch, transfer learning leverages the knowledge and learned representations from a pre-trained model, which has been trained on a large-scale dataset.

## How Transfer Learning Works

### Pre-trained Models:

CNN architectures like VGG, ResNet, Inception, and others are pre-trained on large-scale benchmark datasets such as ImageNet, which contains millions of labeled images across thousands of categories. These pre-trained models have learned general features and patterns that can be useful for a wide range of tasks.

### Feature extraction:

Transfer learning consists of using the pre-trained CNN as a feature extractor. The initial layers of the CNN are kept frozen and used as a fixed feature extractor. The output of these layers is fed into a new classifier or set of layers trained specifically for the new task.

## Practical Implementation

* Select a pre-trained CNN model suitable for your task, taking into account factors such as architecture, complexity, and availability of pre-trained weights.

* Remove the last fully connected layer(s) from the pre-trained model, as they are specific to the original classification task.

* Add a new set of fully connected layers or a custom classifier on the remaining layers of the pre-trained model.

* Initialize the weights of the added layers randomly or with predefined values.

* Train the new model using the new custom dataset.

* Optionally, perform fine-tuning by unfreezing and updating the weights of some layers of the pre-trained model, particularly those closest to the added layers. This step helps the model adapt to the new task.

* Evaluate the performance of the trained model on the validation or test set and make any necessary adjustments to improve its performance.

# YOLOv8: The Latest Generation of YOLO

## Architecture


![YOLOv8 arquitecture.png](..%2F..%2F..%2F..%2F..%2FDownloads%2FYOLOv8%20arquitecture.png)


### Detection

The model is trained using a labeled dataset containing images and corresponding bounding boxes that indicate the location and size of objects of interest in each image.

The model makes predictions using multiple detection layers. Each detection layer divides the image into a grid and assigns each object to the center of the corresponding cell in the grid.

For each grid cell, YOLOv8 predicts the coordinates of the bounding box center and its size, along with the classification probabilities for different object categories. These predictions are made using linear regression and activation functions.

Once the predictions for all detection layers are obtained, a process called non-maximum suppression (NMS) is applied to eliminate redundant detections. The NMS takes care of selecting the most reliable detections, discarding those that overlap significantly and keeping only the most accurate detection for each object.

![(NMS).png](..%2F..%2F..%2F..%2F..%2FDownloads%2F%28NMS%29.png)

Basically, when the model is ready to make predictions, it divides the image into many small parts, like a grid. For each part, the model tries to guess whether there is an object and, if there is, where it is and what kind of object it is.
The YOLOv8 process is faster and less cumbersome because it divides the image into small parts and only needs to make predictions for those parts. It does not need to try all possible locations of objects in the image, which makes it faster.
In addition, YOLOv8 is more memory efficient because it does not need to store information about many predefined anchor frames, but can directly predict object coordinates.

### Closing the Mosaic Augmentation

YOLOv8 augments images during training online. At each epoch, the model sees a slightly different variation of the images it has been provided.

One of those augmentations is called mosaic augmentation. This involves stitching four images together, forcing the model to learn objects in new locations, in partial occlusion, and against different surrounding pixels.


## Conclusion

The LSU models presented in this repository demonstrate the use of deep learning techniques and transfer learning for sign language recognition and object detection tasks. The alphabetic model focuses on recognizing the letters of the Uruguayan alphabet using a combination of YOLOv8, MediaPipe, and OpenCV. The CNN models utilize convolutional neural networks for image classification tasks, leveraging transfer learning to improve efficiency and accuracy. Finally, YOLOv8 showcases the latest advancements in real-time object detection algorithms.

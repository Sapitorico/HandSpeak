#/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2
import os
import random
import yaml
from utils.utils import Utils

"""
The CustomHandDataset class is responsible for creating a custom dataset for hand gesture recognition.
It takes in the directories for training and validation data, the output directory, the name of the dataset directory, and the image size as input.
The class creates the necessary directories for the dataset, reads the class names from a file, detects hands in the images, creates annotations in
the YOLO format, and saves the resized images and annotations in the appropriate directories. Finally, it creates a configuration file for the dataset.

Methods:
- __init__: Initializes the class and sets the necessary directories and image size.
- create_dataset: Calls the create_dataset_yolo method for both the training and validation directories.
- create_dataset_yolo: Iterates through the images in a directory, detects hands in the images, creates annotations in the YOLO format, and saves the resized images and annotations in the appropriate directories.
- create_dataset_config: Creates a configuration file for the dataset.
- __len__: Returns the total number of images in the training and validation directories.

Fields:
- data_dir_train: Directory for the training data.
- data_dir_val: Directory for the validation data.
- output_dir: Directory for the output dataset.
- img_size: Size of the images in the dataset.
- val_image_dir: Directory for the validation images.
- train_image_dir: Directory for the training images.
- label_train: Directory for the training annotations.
- label_val: Directory for the validation annotations.
- class_file: File containing the class names.
- classes: List of class names.
- hands: Hands model configuration for detecting hands in the images.
"""


class CustomHandDataset:
    def __init__(self, data_dir_train, data_dir_val, output_dir, dataset_name_dir, img_size=224):
        self.data_dir_train = data_dir_train
        self.data_dir_val = data_dir_val
        self.output_dir = output_dir + "/" + dataset_name_dir
        self.img_size = img_size


        val_image_dir = os.path.join(self.output_dir, 'images/val')
        train_image_dir = os.path.join(self.output_dir, 'images/train')
        label_train = os.path.join(self.output_dir, 'labels/train')
        label_val = os.path.join(self.output_dir, 'labels/val')

        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(val_image_dir, exist_ok=True)
        os.makedirs(train_image_dir, exist_ok=True)
        os.makedirs(label_train, exist_ok=True)
        os.makedirs(label_val, exist_ok=True)

        class_file = os.path.join(self.output_dir, 'clases.txt')
        self.class_file = class_file.replace('\\', '/')

        try:
            if os.path.exists(self.class_file):
                with open(self.class_file, 'r') as f:
                    self.classes = f.read().splitlines()
            else:
                with open(self.class_file, 'w') as f:
                    self.classes = []

            self.hands = Utils.Hands_model_configuration(False, 2, 1)
            self.create_dataset(train_image_dir, val_image_dir, label_train, label_val)

            # Shuffle the classes
            random.shuffle(self.classes)

            self.create_dataset_config(train_image_dir, val_image_dir, class_file, os.path.join(self.output_dir, 'dataset.yaml'), dataset_name_dir)

        except Exception as e:
            print("Se produjo un error durante la creación del dataset:", str(e))

    def __len__(self):
        train_image_count = sum(len(files) for _, _, files in os.walk(os.path.join(self.output_dir, 'images/train')))
        val_image_count = sum(len(files) for _, _, files in os.walk(os.path.join(self.output_dir, 'images/val')))
        print("Total de imágenes de entrenamiento", train_image_count)
        print("Total de imágenes de validación", val_image_count)
        return train_image_count + val_image_count

    def create_dataset(self, train_image_dir, val_image_dir, label_train, label_val):
        with self.hands:
            self.create_dataset_yolo(self.data_dir_train, train_image_dir, label_train)
            self.create_dataset_yolo(self.data_dir_val, val_image_dir, label_val)

    def create_dataset_yolo(self, dataset_dir, image_dir, label_dir):
        for folder in os.listdir(dataset_dir):
            folder_path = os.path.join(dataset_dir, folder)
            if os.path.isdir(folder_path):
                class_name = folder
                if class_name not in self.classes:
                    with open(self.class_file, 'a') as f:
                        f.write(f'{class_name}\n')
                    self.classes.append(class_name)
                class_index = self.classes.index(class_name)
                images_per_class = 0  # Counter for images per class
                for index, image_file in enumerate(os.listdir(folder_path)):
                    if image_file.endswith('.jpg') or image_file.endswith('.png'):
                        image_path = os.path.join(folder_path, image_file)
                        image = cv2.imread(image_path)
                        image, results = Utils.Hands_detection(image, self.hands)
                        if results.multi_hand_landmarks:
                            annotation_file = os.path.join(label_dir, f'{os.path.splitext(image_file)[0]}.txt')
                            Utils.anotation_data(results, image, annotation_file, class_index)
                            image_name = os.path.splitext(image_file)[0]
                            new_image_name = f'{class_name}_{image_name}.jpg'
                            new_annotation_file = os.path.join(label_dir, f'{class_name}_{image_name}.txt')
                            output_image_path = os.path.join(image_dir, new_image_name)
                            cv2.imwrite(output_image_path, image)
                            os.rename(annotation_file, new_annotation_file)
                            images_per_class += 1

    def create_dataset_config(self, train_img_dir, val_dir, class_file, output_file, dataset_name_dir):
        try:
            with open(class_file, 'r') as f:
                classes = f.read().splitlines()

            config = {
                'path': dataset_name_dir,
                'train': train_img_dir[len(self.output_dir) + 1:],  # Remove the output_dir prefix
                'val': val_dir[len(self.output_dir) + 1:],  # Remove the output_dir prefix
                'nc': len(classes),
                'names': {idx: name for idx, name in enumerate(classes)}
            }

            with open(output_file, 'w') as f:
                yaml.dump(config, f)
                output_file = output_file.replace('\\', '/')
            print("Archivo de configuración creado:", output_file)


        except Exception as e:
            print("Se produjo un error al crear el archivo de configuración:", str(e))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Custom Hand Dataset Creator')
    parser.add_argument('--data_dir_train', type=str, required=True, help='Directory for training data')
    parser.add_argument('--data_dir_val', type=str, required=True, help='Directory for validation data')
    parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('--dataset_name', type=str, required=True, help='Name of the dataset directory')
    parser.add_argument('--img_size', type=int, default=224, help='Image size')

    args = parser.parse_args()

    data_dir_train = args.data_dir_train
    data_dir_val = args.data_dir_val
    output_dir = args.output_dir
    dataset_name = args.dataset_name
    img_size = args.img_size

    dataset = CustomHandDataset(data_dir_train, data_dir_val, output_dir, dataset_name, img_size)
    dataset_length = len(dataset)
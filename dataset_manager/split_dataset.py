#!/usr/bin/python3
# -*- coding: utf-8 -*-
import shutil
import os
import random

"""
The DatasetSubsetCreator class is designed to create a subset of a given training dataset for machine learning purposes. The class takes in a training directory, a subset directory, a subset number, the number of training images per class, and a validation percentage. The main functionalities of the class are to create a subset of the training dataset with a specified number of images per class and a validation set with a specified percentage of the training set. The class achieves this by copying a specified number of images from each class in the training set to the subset directory and moving a specified percentage of those images to the validation set.

Methods:
- __init__(self, training_dir, subset_dir, subset_num, train_images_per_class=500, validation_percentage=0.2): Constructor method that initializes the class fields with the given parameters.
- create_subset(self): Method that creates the subset and validation sets by copying and moving images from the training set to the subset and validation directories. It iterates through each class in the training set, copies a specified number of images to the subset directory, and moves a specified percentage of those images to the validation directory.

Fields:
- training_dir: The directory path of the training dataset.
- subset_dir: The directory path where the subset and validation sets will be created.
- subset_num: The number of the subset being created.
- train_images_per_class: The number of training images to be copied per class.
- validation_percentage: The percentage of training images to be moved to the validation set.
"""


class DatasetSubsetCreator:
    def __init__(self, training_dir, subset_dir, subset_num, train_images_per_class=500, validation_percentage=0.2):
        self.training_dir = training_dir
        self.subset_dir = subset_dir
        self.subset_num = subset_num
        self.train_images_per_class = train_images_per_class
        self.validation_percentage = validation_percentage

    def create_subset(self):
        subset_name = f"training_subset_{self.subset_num}"
        subset_path = os.path.join(self.subset_dir, subset_name)
        os.makedirs(subset_path, exist_ok=True)

        val_subset_name = f"validation_subset_{self.subset_num}"
        val_subset_path = os.path.join(self.subset_dir, val_subset_name)
        os.makedirs(val_subset_path, exist_ok=True)

        classes = os.listdir(self.training_dir)

        for class_name in classes:
            class_dir = os.path.join(self.training_dir, class_name)
            subset_class_dir = os.path.join(subset_path, class_name)
            os.makedirs(subset_class_dir, exist_ok=True)

            images = os.listdir(class_dir)
            total_images = len(images)

            copied_images = len(os.listdir(subset_class_dir))
            copied_names = set(os.listdir(subset_class_dir))

            for image_name in images:
                src_path = os.path.join(class_dir, image_name)
                dst_path = os.path.join(subset_class_dir, image_name)

                if not os.path.exists(dst_path) and copied_images < self.train_images_per_class and image_name not in copied_names:
                    shutil.copy(src_path, dst_path)
                    copied_images += 1
                    copied_names.add(image_name)

            total_train_images = len(os.listdir(subset_class_dir))
            print(f"Class: {class_name} - Total training images: {total_train_images}")

        for class_name in classes:
            subset_class_dir = os.path.join(subset_path, class_name)
            val_class_dir = os.path.join(val_subset_path, class_name)
            os.makedirs(val_class_dir, exist_ok=True)

            images = os.listdir(subset_class_dir)
            val_images_per_class = int(len(images) * self.validation_percentage)

            validation_images = random.sample(images, val_images_per_class)
            for image_name in validation_images:
                src_path = os.path.join(subset_class_dir, image_name)
                dst_path = os.path.join(val_class_dir, image_name)
                shutil.move(src_path, dst_path)

            total_val_images = len(os.listdir(val_class_dir))
            print(f"Class: {class_name} - Total validation images: {total_val_images}")

        print("Training and validation subsets created successfully.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Dataset Subset Creator')
    parser.add_argument('--training_dir', required=True, help='Directory path of the training dataset')
    parser.add_argument('--subset_dir', required=True, help='Directory path where the subset and validation sets will be created')
    parser.add_argument('--subset_num', type=int, default=1, help='Number of the subset being created')
    parser.add_argument('--train_images_per_class', type=int, default=500, help='Number of training images to be copied per class')
    parser.add_argument('--validation_percentage', type=float, default=0.2, help='Percentage of training images to be moved to the validation set')
    args = parser.parse_args()

    subset_creator = DatasetSubsetCreator(args.training_dir, args.subset_dir, args.subset_num,
                                          args.train_images_per_class, args.validation_percentage)
    subset_creator.create_subset()

#!/usr/bin/python3
import shutil
import os
import random

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
    training_dir = "images/Training"
    subset_dir = "images"
    subset_num = 1
    num_image_per_class = 7050
    validation_percentage = 0.25
    subset_creator = DatasetSubsetCreator(training_dir, subset_dir, subset_num, num_image_per_class, validation_percentage)
    subset_creator.create_subset()
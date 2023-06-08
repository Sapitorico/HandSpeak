#/usr/bin/python3
import cv2
import os
import random
import yaml
from utils import Utils

class CustomHandDataset:
    def __init__(self, data_dir_train, data_dir_val, output_dir, dataset_name_dir, img_size=224, max_images_per_class=None):
        self.data_dir_train = data_dir_train
        self.data_dir_val = data_dir_val
        self.output_dir = output_dir + "/" + dataset_name_dir
        self.img_size = img_size
        self.max_images_per_class = max_images_per_class


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

            self.hands = Utils.Hands_model_configuration(False, 1, 1)
            self.create_dataset(train_image_dir, val_image_dir, label_train, label_val)

            # Shuffle the classes
            random.shuffle(self.classes)

            # Limit the number of images per class if specified
            if self.max_images_per_class is not None:
                self.classes = self.classes[:self.max_images_per_class]

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
                        if self.max_images_per_class is not None and images_per_class >= self.max_images_per_class:
                            break  # Reached the maximum number of images for this class
                        image_path = os.path.join(folder_path, image_file)
                        image = cv2.imread(image_path)
                        frame, results = Utils.Hands_detection(image, self.hands)
                        if results.multi_hand_landmarks:
                            annotation_file = os.path.join(label_dir, f'{os.path.splitext(image_file)[0]}.txt')
                            Utils.anotation_data(results, frame, annotation_file, class_index)
                            image_name = os.path.splitext(image_file)[0]
                            new_image_name = f'{class_name}_{image_name}.jpg'
                            new_annotation_file = os.path.join(label_dir, f'{class_name}_{image_name}.txt')
                            image = cv2.resize(frame, (self.img_size, self.img_size))
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
    data_dir_train = "images/Training"
    data_dir_val = "images/Training"
    output_dir = "datasets"
    dataset_name = "dataset-v2"
    img_size = 224
    max_images_per_class = 2  # Choose the desired maximum number of images per class

    dataset = CustomHandDataset(data_dir_train, data_dir_val, output_dir, dataset_name, img_size, max_images_per_class)
    dataset_length = len(dataset)
    print(dataset_length)
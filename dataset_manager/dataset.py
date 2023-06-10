#!/usr/bin/python3
import yaml
import os
import cv2
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt

class Dataset_Images(Dataset):
    def __init__(self, yaml_file, dataset_dir=None, labels_dir=None):
        """
        Dataset class for loading images and corresponding labels from YAML metadata.

        Args:
            yaml_file (str): Path to the YAML metadata file.
            dataset_dir (str): Directory containing the image files.
            labels_dir (str): Directory containing the label files.
        """
        with open(yaml_file, 'r') as file:
            yaml_data = yaml.safe_load(file)
        self.etiquetas = yaml_data.get('names', {})
        self.dataset_dir = dataset_dir
        self.labels_dir = labels_dir
        self.image_files = sorted(os.listdir(self.dataset_dir))
        self.labels_files = sorted(os.listdir(self.labels_dir))

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        image_file = self.image_files[index]
        label_file = self.labels_files[index]
        image_path = os.path.join(self.dataset_dir, image_file)
        label_path = os.path.join(self.labels_dir, label_file)

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        with open(label_path, 'r') as file:
            label_xyz = file.readline().strip()
            label_data = label_xyz.split()[0]
            label = self.etiquetas.get(int(label_data))
        return image, label


if __name__ == '__main__':
    dataset = Dataset_Images("datasets/dataset-v2/dataset.yaml", "datasets/dataset-v2/images/val", "datasets/dataset-v2/labels/train")
    dataloader_imagenes= DataLoader(dataset, 1, shuffle=True)
    plt.figure(figsize=(12, 6))

    for index, data in enumerate(dataloader_imagenes):
        imagen = data[0][0]
        clase = data[1][0]

        ax = plt.subplot(2, 6, index + 1)
        ax.title.set_text(clase)
        plt.imshow(imagen)

        height, width, _ = imagen.shape
        annotation_text = f'Dimensiones: {height}x{width}'
        ax.annotate(annotation_text, (0, 0), (0, -20), xycoords='axes fraction',
                    textcoords='offset points', va='top', ha='left')
        if index == 4:
            break

    plt.tight_layout()
    plt.show()
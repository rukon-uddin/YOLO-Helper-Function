import cv2
import matplotlib.pyplot as plt
import random
import os

my_dpi = 50
img_path = "test_images"
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(30, 30), dpi=my_dpi)
fig.suptitle('Image Plot', fontsize=20)
img_list = [i for i in os.listdir(img_path) if i.endswith(".jpg")]
n = len(img_list)
random_num = random.sample(range(1, n), 9)
counter = 0
for i in range(3):
    for j in range(3):
        rand = random_num[counter]
        counter+=1
        img = cv2.imread(f"{img_path}/{img_list[rand]}")
        axes[i,j].imshow(img)
        axes[i,j].set_xticklabels("")
        axes[i,j].set_yticklabels("")
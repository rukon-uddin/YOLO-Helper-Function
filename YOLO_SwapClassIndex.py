import os
import pandas as pd
import numpy as np
from tqdm import tqdm


class_folder = "classes/car" # folder which contains the txt files
from_idx = 1
to_idx = 0

for txt in tqdm(os.listdir(class_folder)):
   if txt.endswith(".txt"):
       df = pd.read_csv(f"{class_folder}/{txt}", header=None, sep=" ", names=["class", "xm", "ym", "x", "y"])
       df['class'] = df['class'].replace([from_idx],to_idx)   # replacing label 2 to 0
       file_to_delete = open(f"{class_folder}/{txt}",'w')   # clearing the data in the txt file
       file_to_delete.close()
       df.to_csv(f'{class_folder}/{txt}', header=None, index=None, sep=' ', mode='a')
#!/usr/bin/python

# import thread
import time
from PIL import Image
import glob
from tqdm import tqdm
import os

from ecosystools.task_pool import MPITaskPool
from concurrent.futures import ThreadPoolExecutor


print('starting')
data_dir = 'physionet.org/files/mimic-cxr'
version = '2.0.0'

paths_done = glob.glob(f'{data_dir}/{version}/resized_new/**/*.jpg', recursive = True)
print('done', len(paths_done))

paths = glob.glob(f'{data_dir}/{version}/files/**/*.jpg', recursive = True)

all_paths_size = len(paths)

print('all', all_paths_size)

batch_size = 1200

def resize_images(path):
    basewidth = 512
    filename = path.split('/')[-1]
    img = Image.open(path)

    wpercent = (basewidth/float(img.size[0]))
    
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize))
    
    img.save(f'{data_dir}/{version}/resized_new/{filename}')


def work(start_path_idx):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for path_idx in range(start_path_idx, all_paths_size, batch_size):
            futures.append(executor.submit(resize_images, paths[path_idx]))
        
        # Ensure all tasks complete
        for future in futures:
            future.result()

tasks = []
for start_path_idx in range(batch_size):
    tasks.append(start_path_idx)

exe = MPITaskPool()
exe.run(tasks, work, log_freq=1)

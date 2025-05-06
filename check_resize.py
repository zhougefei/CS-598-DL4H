#!/usr/bin/python

# import thread
import time
from PIL import Image
import glob
from tqdm import tqdm
import os

print('starting')
data_dir = 'physionet.org/files/mimic-cxr-jpg'
version = '2.0.0'

paths_done = glob.glob(f'{data_dir}/{version}/resized/**/*.jpg', recursive = True)
print('done', len(paths_done))
# 362078
paths_all = glob.glob(f'{data_dir}/{version}/files/**/*.jpg', recursive = True)
print('all', len(paths_all))

done_files = [os.path.basename(path) for path in paths_done]

paths = [path for path in paths_all if os.path.basename(path) not in done_files ]
print('left', len(paths))

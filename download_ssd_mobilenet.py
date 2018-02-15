#!/usr/bin/env python3

import requests
import os
import shutil

curr_path = os.getcwd()
models_path = os.path.join(curr_path,"data")

try:
    os.makedirs(models_path)
except Exception as e:
    pass


# downloading from: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
url = 'http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz'

if os.path.exists(os.path.join(models_path,"ssd_mobilenet_v1_coco_11_06_2017.tar.gz")) == False:
    response = requests.get(url, stream=True)
    with open(os.path.join(models_path,"ssd_mobilenet_v1_coco_11_06_2017.tar.gz"), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


import tarfile
filePath = os.path.join(models_path,"ssd_mobilenet_v1_coco_11_06_2017.tar.gz")
os.chdir(models_path)


if (filePath.endswith("tar.gz")):
    tar = tarfile.open(filePath, "r:gz")
    tar.extractall()
    tar.close()
elif (filePath.endswith("tar")):
    tar = tarfile.open(filePath, "r:")
    tar.extractall()
    tar.close()


print("done")

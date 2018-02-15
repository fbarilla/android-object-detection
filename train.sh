#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Did you update the paths ssd_mobilenet_v1_face.config?"
echo "and tensorflow_models in this script"
read -rsp $'Press any key to continue...\n' -n 1 key
echo ">>>>>"

python ../tensorflow/tensorflow/models/research/object_detection/train.py --logtostderr --pipeline_config_path=ssd_mobilenet_v1.config  --train_dir=model_output



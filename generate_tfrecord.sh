#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python generate_tfrecord.py --images_path=data/tf_train/images --csv_input=data/tf_train/train.csv  --output_path=data/train.record
python generate_tfrecord.py --images_path=data/tf_val/images --csv_input=data/tf_val/val.csv  --output_path=data/val.record

#!/usr/bin/env sh
set -e

# -weights flag will tell Caffe to load pre-trained weights from specified file 
# if you want to freeze any layers, just set lr_mult = 0
$CAFFE_ROOT/build/tools/caffe train --solver=./solver.prototxt $@ -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0

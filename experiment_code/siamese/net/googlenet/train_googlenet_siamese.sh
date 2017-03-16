#!/usr/bin/env sh
set -e

TOOLS=$CAFFE_ROOT/build/tools

$TOOLS/caffe train -solver ./siamese_googlenet_train.prototxt -weights ./bvlc_alexnet.caffemodel -gpu 0

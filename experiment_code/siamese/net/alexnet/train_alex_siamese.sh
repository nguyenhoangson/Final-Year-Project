#!/usr/bin/env sh
set -e

TOOLS=$CAFFE_ROOT/build/tools

$TOOLS/caffe train -solver ./siamese_alexnet_solver.prototxt -weights ./bvlc_alexnet.caffemodel -gpu 0

#!/usr/bin/env sh
set -e

~/Caffe/caffe/build/tools/caffe train --solver=./lenet_solver.prototxt $@

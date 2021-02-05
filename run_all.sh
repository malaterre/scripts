#!/bin/sh -e
set -x

videodb="$1"

#for id in $(./checkvideoxml --print "$videodb"); do echo $id; done
for id in $(./checkvideoxml --print "$videodb"); do ./fortiche --verbose $id; done

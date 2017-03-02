#!/bin/sh
cat /dev/zero > ./file.zero
sync
rm ./file.zero

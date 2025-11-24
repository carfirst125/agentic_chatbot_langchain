#!/bin/sh
# Ngăn commit file >100MB
find . -type f -size +100M | while read file; do
    echo "Error: $file is larger than 100MB. Remove or use Git LFS."
    exit 1
done

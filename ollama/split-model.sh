#!/bin/bash
set -e

# Script to split large files into chunks to work around layer size limits

MODEL_DIR=$1
THRESHOLD_SIZE=$((40*1024*1024*1024)) # 40GB threshold

echo "Scanning for large files in $MODEL_DIR..."

# Find all large files over threshold size
find "$MODEL_DIR" -type f -size +${THRESHOLD_SIZE}c | while read -r large_file; do
    echo "Splitting large file: $large_file"
    
    # Get file size
    file_size=$(stat -c%s "$large_file")
    echo "File size: $file_size bytes"
    
    # Calculate split point (roughly half)
    half_size=$((file_size / 2))
    
    # Create part1
    echo "Creating part1..."
    dd if="$large_file" of="${large_file}.part1" bs=1M count=$((half_size / 1024 / 1024))
    
    # Create part2
    echo "Creating part2..."
    dd if="$large_file" of="${large_file}.part2" bs=1M skip=$((half_size / 1024 / 1024))
    
    # Create metadata file with original size
    echo "$file_size" > "${large_file}.size"
    
    # Remove the original file to save space
    rm "$large_file"
    
    echo "Split completed for $large_file"
done

echo "All large files have been processed"
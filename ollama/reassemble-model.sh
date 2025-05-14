#!/bin/bash
set -e

# Script to reassemble large model files that were split during build

MODEL_DIR="${1:-/home/ollama/.ollama/models}"
echo "Scanning for split files in $MODEL_DIR..."

# Find all *.part1 files and process them
find "$MODEL_DIR" -name "*.part1" | while read -r part1_file; do
    base_file="${part1_file%.part1}"
    part2_file="${base_file}.part2"
    size_file="${base_file}.size"
    
    if [[ -f "$part2_file" && -f "$size_file" ]]; then
        echo "Reassembling: $base_file"
        
        # Read the original file size
        original_size=$(cat "$size_file")
        echo "Original size: $original_size bytes"
        
        # Reassemble the file using cat
        cat "$part1_file" "$part2_file" > "$base_file"
        
        # Verify the size
        reassembled_size=$(stat -c%s "$base_file")
        echo "Reassembled size: $reassembled_size bytes"
        
        if [[ "$reassembled_size" -eq "$original_size" ]]; then
            echo "Reassembly successful, removing part files"
            rm "$part1_file" "$part2_file" "$size_file"
        else
            echo "WARNING: Size mismatch for $base_file! Expected $original_size, got $reassembled_size"
            # We'll keep the parts in case manual intervention is needed
        fi
    else
        echo "WARNING: Missing part2 or size file for $part1_file"
    fi
done

echo "All split files have been processed"

# Make sure Ollama can access all files
if [[ -d "$MODEL_DIR" ]]; then
    chown -R ollama:ollama "$MODEL_DIR" 2>/dev/null || true
fi
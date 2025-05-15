#!/bin/bash
# This script runs the Python Data Processing program

INPUT_FILE="input_data.csv"
OUTPUT_FILE="output_data.csv"

python3 data_processing.py $INPUT_FILE $OUTPUT_FILE

echo "Data processing completed. Results stored in $OUTPUT_FILE."

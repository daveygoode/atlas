#!/bin/bash
# Simple wrapper for ATLAS update script

# Determine the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the Python update script
python3 "$SCRIPT_DIR/update_atlas.py" "$@"
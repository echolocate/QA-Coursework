#!bin/bash

source venv/bin/activate
echo "Creating schema..."
python3 create.py
echo "Schema created!"
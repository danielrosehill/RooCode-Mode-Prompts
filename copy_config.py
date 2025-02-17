#!/usr/bin/env python3
import shutil
import os

def main():
    # Define source and destination paths
    source_path = '/home/daniel/.config/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_custom_modes.json'
    dest_path = 'cline_custom_modes.json'
    
    # Copy the file
    try:
        shutil.copy2(source_path, dest_path)
        print(f"Successfully copied {source_path} to {dest_path}")
    except Exception as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    main()
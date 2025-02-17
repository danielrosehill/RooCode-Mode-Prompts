#!/usr/bin/env python3
import os
import tarfile
from datetime import datetime
import logging

def setup_logging():
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def create_timestamp():
    """Create a timestamp string suitable for file naming."""
    return datetime.now().strftime('%y%m%d_%H%M%S')

def ensure_directory(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

def create_tarfile(source_dir, output_filename):
    """Create a compressed tar archive of the source directory."""
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        logging.info(f"Created compressed archive: {output_filename}")

def export_prompts():
    """Main function to export prompts directory as a compressed archive."""
    try:
        # Setup logging
        setup_logging()
        
        # Get script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create paths
        prompts_dir = os.path.join(script_dir, 'prompts')
        packages_dir = os.path.join(script_dir, 'packages')
        
        # Ensure packages directory exists
        ensure_directory(packages_dir)
        
        # Create timestamped archive name
        timestamp = create_timestamp()
        archive_name = f'prompts_export_{timestamp}.tar.gz'
        archive_path = os.path.join(packages_dir, archive_name)
        
        # Create compressed archive
        create_tarfile(prompts_dir, archive_path)
        
        logging.info(f"Successfully exported prompts to: {archive_path}")
        return True
        
    except FileNotFoundError as e:
        logging.error(f"Source directory not found: {e}")
        return False
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    export_prompts()
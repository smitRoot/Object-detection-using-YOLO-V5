import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project name
project_name = "WasteDetection"

# List of files to create
list_files = [
    ".github/workflows/.gitkeep",   
    "data/.gitkeep",  
    f"{project_name}/__init__.py",  
    # Fixed typo here from 'componenets' to 'components'
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/components/training_pipeline/__init__.py",
    f"{project_name}/components/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Iterate over the list of files
for filepath in list_files:
    filepath = Path(filepath)  ### Path object will handle path compatibility

    # Get the directory and filename separately
    filedir, filename = os.path.split(filepath)

    # Debugging: Print the filedir before trying to create the directory
    logging.info(f"Checking directory: {filedir} for the file {filename}")

    # Check if there's a file where the directory is supposed to be
    if filedir and os.path.isfile(filedir):
        logging.error(f"Cannot create directory: {filedir} because a file already exists with that name.")
        continue  # Skip to the next file in the list

    # Create the directory if it doesn't exist
    try:
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file {filename}")
    except Exception as e:
        logging.error(f"Error creating directory {filedir}: {e}")
        continue  # Skip to the next file in the list

    # Create the file if it doesn't exist or if it's empty
    try:
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass  # Just creating an empty file
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filepath} already exists and is not empty.")
    except Exception as e:
        logging.error(f"Error creating file {filepath}: {e}")

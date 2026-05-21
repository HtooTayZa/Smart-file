import yaml
import logging
from pathlib import Path

def setup_logger():
    """Sets up a clean console logger."""
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger("SmartOrganizer")

def load_config(config_path: Path) -> dict:
    """Reads and parses the YAML configuration file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def build_extension_map(rules: dict) -> dict:
    """
    Inverts the rules dictionary from:
    { 'Dest': ['.ext1', '.ext2'] } 
    to:
    { '.ext1': 'Dest', '.ext2': 'Dest' }
    """
    extension_map = {}
    for destination, extensions in rules.items():
        for ext in extensions:
            # Ensure extensions are stored in lowercase for reliable matching
            extension_map[ext.lower()] = Path(destination)
    return extension_map
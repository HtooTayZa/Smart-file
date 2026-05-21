import shutil
import logging
from pathlib import Path

logger = logging.getLogger("SmartOrganizer")

def safe_move(source: Path, target_dir: Path, strategy: str):
    """Safely moves a file to the target directory handling collisions."""
    # Ensure the target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / source.name
    
    # Handle name collisions
    if target_path.exists():
        if strategy == "skip":
            logger.info(f"Skipped: '{source.name}' already exists in target.")
            return
            
        elif strategy == "rename":
            stem = source.stem
            suffix = source.suffix
            counter = 1
            # Loop until we find a filename that doesn't exist yet
            while target_path.exists():
                target_path = target_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            logger.info(f"Renamed: '{source.name}' -> '{target_path.name}' to avoid collision.")
            
        elif strategy == "overwrite":
            logger.info(f"Overwriting: '{target_path.name}' with '{source.name}'.")
    
    # Execute the move inside a try-except block to catch locked files
    try:
        shutil.move(str(source), str(target_path))
        logger.info(f"Moved: '{source.name}' -> {target_dir}")
    except PermissionError:
        logger.error(f"Permission Denied: '{source.name}' is currently open or locked by another program.")
    except Exception as e:
        logger.error(f"Failed to move '{source.name}': {e}")

def run_organization_loop(source_dirs: list, ext_map: dict, strategy: str):
    """Scans source directories and moves files based on the extension map."""
    for source in source_dirs:
        src_path = Path(source)
        
        if not src_path.exists():
            logger.warning(f"Source directory not found: {src_path}")
            continue
            
        # Iterate files in the directory
        for file_path in src_path.iterdir():
            if file_path.is_file():
                
                suffix = file_path.suffix.lower()
                
                # find the target destination
                target_dir = ext_map.get(suffix)
                
                if target_dir:
                    safe_move(file_path, target_dir, strategy)
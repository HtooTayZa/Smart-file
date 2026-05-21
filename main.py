from pathlib import Path
from utils import setup_logger, load_config, build_extension_map
from organizer import run_organization_loop

def main():
    logger = setup_logger()
    logger.info("Starting Smart File Organizer...")

    config_path = Path('config.yaml')
    
    if not config_path.exists():
        logger.error("config.yaml not found! Please create one in the root directory.")
        return

    # 1. Load Configuration
    try:
        config = load_config(config_path)
    except Exception as e:
        logger.error(f"Failed to parse config.yaml: {e}")
        return

    source_dirs = config.get('source_dirs', [])
    rules = config.get('rules', {})
    strategy = config.get('collision_strategy', 'rename')

    # 2. Build the reverse-lookup map
    ext_map = build_extension_map(rules)
    logger.info(f"Loaded rules for {len(ext_map)} different file extensions.")

    # 3. Execute the sorting logic
    run_organization_loop(source_dirs, ext_map, strategy)
    
    logger.info("File organization complete!")

if __name__ == "__main__":
    main()
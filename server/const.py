import sys
from pathlib import Path


# BASE_DIR_STR = Path(__file__).resolve().parent
BASE_DIR_STR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
DATABASE_PATH = BASE_DIR_STR / "database.db"
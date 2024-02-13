import sys
from pathlib import Path

BASE_DIR_STR = Path(__file__).resolve().parent
# BASE_DIR_STR = Path(sys.executable)
DATABASE_PATH = BASE_DIR_STR / "database.db"
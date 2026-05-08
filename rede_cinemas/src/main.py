import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database import init_db
from view.menu import run

if __name__ == "__main__":
    init_db()
    run()
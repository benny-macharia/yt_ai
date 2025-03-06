import sys
import importlib.util

def patch_sqlite():
    """
    Patch sqlite3 with pysqlite3 to ensure ChromaDB works correctly.
    This must be called before importing crewAI or any module that uses ChromaDB.
    """
    try:
        # Try to import pysqlite3
        __import__('pysqlite3')
        # Replace sqlite3 with pysqlite3
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
        print("SQLite successfully patched with pysqlite3")
    except ImportError:
        print("Warning: pysqlite3 not found. If you encounter SQLite version errors, "
              "please install it with: pip install pysqlite3-binary")
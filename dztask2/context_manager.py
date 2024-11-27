from contextlib import contextmanager
import json

@contextmanager
def file_manager(file_name, mode):
    file = None
    try:
        print(f"Attempting to open {file_name}")
        file = open(file_name, mode)
        yield file
    except FileNotFoundError:
        print(f"File {file_name} not found. Please ensure the file exists in the correct directory.")
        yield None
    finally:
        if file is not None:
            print(f"Closing file {file_name}")
            file.close()
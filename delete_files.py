import os
import shutil

path = "test.txt"

try:
    os.remove(path)  # delete a file
    os.rmdir(path)  # delete and empty directory
    shutil.rmtree(path)  # delete a directory containing files (dangerous)
except FileNotFoundError:
    print("That file was no found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

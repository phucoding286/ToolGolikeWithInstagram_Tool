import os, sys, shutil

if os.path.exists("./driver_data"):
    shutil.rmtree("./driver_data")

if sys.platform.startswith("win"):
    os.system("python ./instagram/main.py")
else:
    os.system("python3 ./instagram/main.py")
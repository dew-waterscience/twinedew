import inspect
import glob
import os
import sys
import pathlib
import shutil

dest = pathlib.Path(
    r"r:\watermondev\waterscience-code\apps\services-data\pypiserver\wheels"
)


__version__ = "0.1"


def upload_wheel_file(src_fname):
    fname = os.path.basename(src_fname)
    dest_fname = str(dest / fname)
    if os.path.isfile(dest_fname):
        if (os.stat(src_fname).st_mtime - os.stat(dest_fname).st_mtime) > 1:
            shutil.copy2(src_fname, dest_fname)
            print(dest_fname)
    else:
        shutil.copy2(src_fname, dest_fname)
        print(dest_fname)


def twinedew():
    if sys.argv[1] == "upload":
        for filename in glob.glob(sys.argv[2]):
            upload_wheel_file(filename)

def main():
    pass


if __name__ == "__main__":
    main()

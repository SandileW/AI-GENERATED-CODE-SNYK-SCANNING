import tarfile
import os

#unzip the tar file to /tmp/unpack
##with tarfile.open("archive.zip") as tar:
#-tabnine next line-


def unzip_file(file_path):
    with tarfile.open(file_path) as tar:
        tar.extractall()
        tar.close()
        os.remove(file_path)
        return True
        
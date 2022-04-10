# copyfile() => copies content of a file
# copy() => copyfile() + permission mode + destination can be a directory
# copy2() => copy() + copies meta data (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'testcopy.txt')  # src, destination

# Files and Directories
from pathlib import Path

# Absolute Path
# C:\Program Files\Microsoft - Windows
# /usr/local/bin - Mac/Linux
# Relative Path
# path = Path("./Packages/ecommerce")
path = Path("../")
for file in path.glob('*'):
    print(file)

# glob() searches for files or directories
# mkdir() makes a directory whereas rmdir() removes a directory

# Personal Notes - 
# Apparently, if I just try to run a file through VS Code that involves directories or files, then it wont work.
# I have to do it via a command prompt (not the weird sudo Python terminal) and typing out "python (filename).py"
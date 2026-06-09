import os


def purge(target):
    # Command injection via os.system (file DELETED in C1)
    os.system("rm -rf " + target)

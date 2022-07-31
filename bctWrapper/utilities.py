import argparse
import os
import numpy as np
import bct
from glob import glob

dirname = os.path.dirname(__file__)

# f = open("/home/chris/cs680/project1/bctWrapper/connectomes/c001_s1.txt", "r")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file", required=False)


# tempConn = np.loadtxt("/home/chris/cs680/project1/bctWrapper/connectomes/c001_s1.txt")
#
# tempConn2 = np.loadtxt(
#     "/home/chris/cs680/project1/bctWrapper/fmri_connectomes/8315.txt"
# )


fmri_connectomes = os.listdir("/home/chris/cs680/project1/bctWrapper/fmri_connectomes/")

file_list = sorted(fmri_connectomes)

i = 0
while i < 100:
    filename = file_list[i].split(".")[0]
    print(filename)
    i += 1

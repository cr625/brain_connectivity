import argparse
import os
from matplotlib.pyplot import get
import numpy as np
import bct
from glob import glob

# parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--input", help="input file", required=False)


cwd = os.getcwd()
connectomes_dir = os.path.join(cwd, "pnc_fmri_connectomes")  # pnc dataset connectomes
subjects_file = os.path.join(
    cwd, "src/pnc_subjects.txt"
)  # files parsed subjects to include in the analysis

subject_file_list = sorted(os.listdir(connectomes_dir))


def add_to_subjects_file(subject_file_list):
    with open(subjects_file, "w") as f:
        for subject in subject_file_list:
            f.write(subject + "\n")
    f.close()


def get_subjects(n):
    i = 0
    subject_list = []
    while i < n:
        subject_list.append(subject_file_list[i].split(".")[0])
        i += 1
    return subject_list


if __name__ == "__main__":
    add_to_subjects_file(get_subjects(200))

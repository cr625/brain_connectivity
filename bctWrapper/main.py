
import bct
import scipy.stats as stt
import numpy as np
import os
import matplotlib.pyplot as plt
import click

from helpers import heatMap as heat_map



# list of 50 subjects
cwd = os.getcwd()
fmri_connectomes_dir = os.path.join(cwd, "pnc_fmri_connectomes")  # pnc dataset connectomes
dmri_connectomes_dir = os.path.join(cwd, "pnc_dmri_connectomes")  # pnc dataset connectomes

subjects_file = os.path.join(
    cwd, "src/pnc_subjects.txt"
) 

def get_subject_list(n=50):
    with open(subjects_file, "r") as f:
        subject_list = [line.strip() for line in f]
    f.close()
    return sorted(subject_list[0:n])

def connectome_file_name(subject):
    return str(subject) + ".txt"
    
def get_weighted_connectome(subject_id, mri_type):
    connectome_file = connectome_file_name(subject_id)
    connectome_dir = fmri_connectomes_dir if mri_type == "fmri" else dmri_connectomes_dir
    temp_connectome = os.path.join(connectome_dir, connectome_file)
    connectome = np.loadtxt(temp_connectome)
    weighted_connectome = np.array(connectome)
    return weighted_connectome

def get_flat_connectome(subject_id, mri_type):
    connectome_file = str(subject_id) + ".txt"
    if mri_type == "fmri":
        temp_connectome = os.path.join(fmri_connectomes_dir, connectome_file)
    elif mri_type == "dmri":
        temp_connectome = os.path.join(fmri_connectomes_dir, connectome_file)
    connectome = np.loadtxt(temp_connectome)
    return connectome


@click.group()
def cli():
    pass

@click.command()
@click.argument("subject", type=int)
def heatmap(subject):
    subject_id = str(subject)
    data = get_weighted_connectome(subject_id, "fmri")
    output_path = os.path.join(cwd, "heatmap_" + subject_id + ".png")
    heat_map(data,0, output_path,"white",1,)
       

cli.add_command(heatmap)


if __name__ == "__main__":
    cli()
    
    subjects = get_subject_list(5)


 
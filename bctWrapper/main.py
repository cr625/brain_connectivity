import bct
import scipy.stats as stt
import numpy as np
import os
import matplotlib.pyplot as plt
import click

from helpers import drawCorrelationPlot, heatMap as heat_map


# list of 50 subjects
cwd = os.getcwd()
fmri_connectomes_dir = os.path.join(
    cwd, "pnc_fmri_connectomes"
)  # pnc dataset connectomes
dmri_connectomes_dir = os.path.join(
    cwd, "pnc_dmri_connectomes"
)  # pnc dataset connectomes

subjects_file = os.path.join(cwd, "src/pnc_subjects.txt")


def get_subject_list(start=0, stop=50):
    with open(subjects_file, "r") as f:
        subject_list = [line.strip() for line in f]
    f.close()
    return sorted(subject_list[start:stop])


def connectome_file_name(subject):
    return str(subject) + ".txt"


def get_weighted_connectome(subject_id, mri_type="fmri"):
    connectome_file = connectome_file_name(subject_id)
    connectome_dir = (
        fmri_connectomes_dir if mri_type == "fmri" else dmri_connectomes_dir
    )
    temp_connectome = os.path.join(connectome_dir, connectome_file)
    connectome = np.loadtxt(temp_connectome)
    weighted_connectome = np.array(connectome)
    return weighted_connectome


def get_flat_connectome(subject_id, mri_type="fmri"):
    connectome_file = str(subject_id) + ".txt"
    connectome_dir = (
        fmri_connectomes_dir if mri_type == "fmri" else dmri_connectomes_dir
    )
    temp_connectome = os.path.join(connectome_dir, connectome_file)
    flat_connectome = np.loadtxt(temp_connectome, max_rows=1)
    return flat_connectome


def get_training_connectomes(subject_list, mri_type="fmri"):
    training_connectomes = []
    for subject in subject_list:
        training_connectomes.append(get_weighted_connectome(subject, mri_type))
    return training_connectomes

def get_test_connectomes(subject_list, mri_type="fmri"):
    training_connectomes = []
    for subject in subject_list:
        training_connectomes.append(get_weighted_connectome(subject, mri_type))
    return training_connectomes





@click.group()
def cli():
    pass


@click.command()
@click.argument("subject", type=int)
def heatmap(subject):
    subject_id = str(subject)
    data = get_weighted_connectome(subject_id, "fmri")
    output_path = os.path.join(cwd, "heatmap_" + subject_id + ".png")
    heat_map(
        data,
        0,
        output_path,
        "white",
        1,
    )


@click.command()
@click.argument("subject", type=int)
def correlation(subject):
    subject_id = str(subject)
    fmri_subject_connectome = get_flat_connectome(subjects[subject], "fmri")
    dmri_subject_connectome = get_flat_connectome(subjects[subject], "dmri")

    click.echo("fMRI dMRI Correlation for Subject : " + subject_id)
    drawCorrelationPlot(
        fmri_subject_connectome,
        dmri_subject_connectome,
        0.4,
        0.05,
        "fmri",
        "dmri",
        "fMRI dMRI Correlation",
        "pnc_connectome_correlation.png",
    )
    # data = get_weighted_connectome(subject_id, "fmri")
    # output_path = os.path.join(cwd, "correlation_" + subject_id + ".png")
    # drawCorrelationPlot(data, output_path)


def count_subject_files(connectome_dir):
    dir_contents = os.listdir(connectome_dir)
    return len(dir_contents)  # 821h


cli.add_command(heatmap)
cli.add_command(correlation)

if __name__ == "__main__":

    subjects = get_subject_list(50)  # 50 subjects in pnc_subjects.txt
    subject = subjects[0]

    cli()

import bct
import numpy as np
import os

from helpers import (
    calculateZScore,
    fdr,
    calculateGroupDifference,
    drawHistogram2Dataset,
    drawBoxPlot,
    drawViolinPlot,
    heatMap,
)


cwd = os.getcwd()
connectomes_dir = os.path.join(cwd, "fmri_connectomes")  # pnc dataset connectomes

subject_id = "2738"
connectome_file = "2738" + ".txt"

temp_connectome = os.path.join(connectomes_dir, connectome_file)

connectome = np.loadtxt(temp_connectome)

weighted_connectome = np.array(connectome)

output_filename = subject_id + "_heatmap"

heatMap(weighted_connectome, 0, output_filename, "white", 1)

# -*- coding: utf-8 -*-
#Loading of the packages
import scanpy as sc
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import colors

import seaborn as sb
from gprofiler import GProfiler
import seaborn as sns

from IPthon import get_ipython
get_ipython().magic('who print')
import rpy2.rinterface_lib.callbacks
from rpy2.robjects import pandas2ri
import anndata2ri

import importlib
import logging
import warnings
warnings.filterwarnings("ignore")

import pickle as pkl
from matplotlib.colors import LinearSegmentedColormap

#Define the colorblind-friendly colormap and color pallete
values = [0,1]
colors = [(227, 227, 227), (255, 42, 18)]
norm = plt.Normalize(min(values), max(values))
my_cmap = LinearSegmentedColormap.from_list(
    '', [(norm(value), tuple(np.array(color) / 255)) for value, color in zip(values, colors)])
my_pallete = ['#0351A8','#8CB0E0','#D56D11',
              '#FFBB78','#234E08','#53CB8B',
              '#D30083','#CB788D','#4E195A',
              '#C58CCF','#AA290F','#B03FD1',
              '#E8BCCF','#64605F','#B2AD9A',
              '#D2D30B','#D1BD4F','#06DCF2',
              '#9EDAE5','#517219','#5B43CF',
              '#D92F24','#FFD900','#002F33','#B8A3A3']

#Start setting up the R-python interface
rpy2.rinterface_lib.callbacks.logger.setLevel(logging.ERROR)

# Automatically convert rpy2 outputs to pandas dataframes
pandas2ri.activate()
anndata2ri.activate()
%load_ext rpy2.ipython

sc.logging.print_versions()



%%R
#Set up the path to your R library
.libPaths(.libPaths('C:\\Users\\16220\\AppData\\Local\\R\\win-library\\4.2'))
#Load all the R library that are going to be used in this analysis
library(scran)
library(Seurat)
library(RColorBrewer)
library(slingshot)
library(monocle)
library(gam)
library(ggplot2)
library(plyr)
library(MAST)
library(clusterExperiment)
library(monocle3)

# This function was originally written by Dan Hallatt, in-part using the ternary plotter made by Corentin Le Guillou. Both at the Université de Lille.

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.tri as tri
import scipy.stats as st
from scipy.interpolate import griddata
import numpy as np
import pandas as pd
import math


# A) "Ternary_Contour" : plots ternary contour plot, using a data in the form [[A1, B1, C1], [A2, B2, C2], ...]. Also plots a ternary plot of all of the raw data, for comparison/check of the contours.

#   A.1) "Tern_Base" : defines the base structure (axis names, stoichiometric reference lines, ect..) of the ternary plot.

#   A.2) "triplot" : plots static ternary plot of raw data.

def Ternary_Contour(dataset, type, NumLevels, ContLines, FigureSavePath, FileName, Colour, ContLines, WhiteCutoff=0):
    """ Uses matplotlib to plot a ternary diagram
    ** dataset : should be an array containing the values to plot, in the form [Ai, Bi, Ci] where A is the top corner, B is the left corner and C the right corner of the triangle (A = Si + Al, B = Fe, C = Mg for example)
        - Several datapoints should be within this array, where the entire dataset is in the form [[A1, B1, C1], [A2, B2, C2], ...[An, Bn, Cn]] for n datapoints. This form is fundamentally required for contours (populations of datapoints, not single datapoints).
        
        !!! NOTE !!! : Data cannot contain 'NaN' values. Must be cleaned prior to input in this function (or this function modified to clean data by removing them).
        
    ** type : Either 'silicate' [Si+Al, Mg, Fe], 'silicateHydration' [Si+Al, Mg+Fe, O], or 'sulfide' [S, Ni, Fe].
    ** NumLevels: number of contour levels.
    ** ContLines : Either 'y' (yes) or 'n' (no) to display lines of each contour (as opposed to just the colour contours).
    ** FigureSavePath : Path to folder location where figures should be saved. Must be in single quotations, example : '/Volumes/Samsung_T5/Experiment categories/Laser/Figures/'
    ** FileName : General name of files to be saved. Must be in single quotations, example : 'TEST_DataSet01'
    ** Colour : In quotations (such as 'Blues') the colour of the contour plot. Options available according to 'cmap' of matplotlib (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
    ** ContLines : Either 'y' (yes) or 'n' (no), plot or not to plot the lines seperating contour levels.
    ** WhiteCutoff : A value of data density used as the maximum density cutoff for colouring contour levels white (to make a white background). Default value is zero(0), which can be adjusted by trial-and-error (or by reading contour line values with ContourValues='y') to find an appropriate value such that the background is white.
    ** ContourValues : Either 'y' (yes) or 'n' (no), plot or not to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    """
    
    def Tern_Base():
        """
        This is specifically the base style of the ternary plot.
        - defines axis positions, stoichiometric reference lines/locations.
        """
        ax.plot([-0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0],  [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], color = 'black', marker="_")
        ax.plot([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],  [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0], color='black', marker="_")
        ax.plot([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5], [0,0,0,0,0,0,0,0,0,0,0], color='black', marker="|")

        if type == 'silicate':
            ax.plot([0.29, -0.29], [0.4, 0.4], linestyle=':', color='dimgrey')
            ax.annotate('Serp', xy=(0.3, 0.4), xytext = (0.32, 0.39), size = 10)
            
            ax.plot([0.21, -0.21], [0.57, 0.57], linestyle=':', color='dimgrey')
            ax.annotate('Sap', xy=(0.21, 0.57), xytext = (0.23, 0.56), size = 10)
            
            ax.plot([0.329, -0.329], [0.333, 0.333], linestyle='--', color='dimgrey')
            ax.annotate('Ol', xy=(0.333, 0.333), xytext = (0.35, 0.32), size = 10)
            
            ax.plot([0.24, -0.24], [0.5, 0.5], linestyle='--', color='dimgrey')
            ax.annotate('Py', xy=(0.25, 0.50), xytext = (0.27, 0.49), size = 10)
            
            ax.annotate('Si + Al', xy=(0.2, 1.), xytext = (-0.06, 1.03), size = 13)
            ax.annotate('Fe', xy=(-0.55,0.0), xytext = (-0.57,-0.03), size = 13)
            ax.annotate('Mg', xy=(0.55,0.0), xytext = (0.53, -0.03), size = 13)

        if type == 'sulfide':
            ax.plot(-0.25, 0.5, 'ro', markersize=5)
            ax.plot(0.0, 0.47, 'bo', markersize = 5)
            ax.plot([-0.25, -0.22], [0.5, 0.56], color='purple', linewidth = 7)
            ax.plot(-0.17,0.67, 'go',  markersize = 5)
            ax.annotate('Troilite', xy=(-0.25, 0.5), xytext = (-0.4, 0.5), size=10)
            ax.annotate('Pentlandite', xy=(0.0, 0.47), xytext = (0.03,0.47), size=10)
            ax.annotate('Pyrrhotite', xy=(-0.235, 0.55), xytext = (-0.42,0.55), size=10)
            ax.annotate('Pyrite', xy=(-0.17,0.67), xytext = (-0.32,0.67), size=10)
            ax.annotate('S', xy=(0., 1.0), xytext = (-0.05, 1.03), size=13)
            ax.annotate('Fe', xy=(-0.55,0.0), xytext = (-0.56,-0.03), size=13)
            ax.annotate('Ni', xy=(0.55,0.0), xytext = (0.52, -0.03), size=13)
            
        if type == 'silicateHydration':
            ax.plot(-0.21, 0.142857, marker="3", color= 'dimgrey', markersize=8, alpha=0.5)
            ax.annotate('Serp', xy=(-0.2, 0.14), xytext = (-0.235,0.05), size=6)
            ax.annotate('Si + Al', xy=(0.01, 1.0), xytext = (-0.06, 1.05), size = 13)
            ax.annotate('O', xy=(-0.55,0.0), xytext = (-0.57,-0.03), size = 13)
            ax.annotate('Mg + Fe', xy=(0.55,0.0), xytext = (0.53, -0.03), size = 13)
            

    def triplot(dataset, mask, legend, type, dataform):
        """ A general plot that uses matplotlib to plot a ternary diagram. !!! This function is used here in the contour video function to plot a static ternary diagram with all of the data as a reference to the contour plot for the user. !!!
        ** dataset should be an array containing the values to plot, in the form [A, B, C] where A is the top corner, B is the left corner and C the right corner of the triangle (A = Si + Al, B = Fe, C = Mg for example).
        ** dataform : 'single' or 'multiple': Several datasets can be plotted, in that case the dataset is in the form [[A1, B1, C1], [A2, B2, C2], ...]. 'multiple' is required for the contour plot use of this function, as is used here.
        ** mask : can be applied to the dataset
        ** legend : A list for legending different datasets
        ** type : Either 'silicate' [Si+Al, Mg, Fe],  'silicateHydration' [Si+Al, Mg+Fe, O], or 'sulfide' [S, Ni, Fe].
        """
        
        tri_y=[]
        tri_x=[]
        # Converting the 3D ternary data of [A, B, C] into 2D coordinates of [x,y] which correspond to the area within the ternary bounds. New data is thus tri_y and tri_x.
        if dataform == 'multiple':
            for i in range (len(dataset)): # i is number of datapoints (not number of data total (groups of 3, for each axis)).
                tri_y.append(dataset[i][0]/(dataset[i][0]+dataset[i][1]+dataset[i][2]))
                tri_x.append(np.array(-0.5)*(np.array(1.)-tri_y[i])+(dataset[i][2]/(dataset[i][0]+dataset[i][1]+dataset[i][2])))
        elif dataform == 'single':
            tri_y.append(dataset[0]/(dataset[0]+dataset[1]+dataset[2]))
            tri_x.append(np.array(-0.5)*(np.array(1.)-tri_y)+(dataset[2]/(dataset[0]+dataset[1]+dataset[2])))
        else:
            print('Problem in user-definition of "dataform" variable within "Ternary_Contour" function.')
            
        Tern_Base()

        for i in range(len(dataset)):
            ax.plot(tri_x[i], tri_y[i])

        ax.axis('off')
        fig.savefig(FigureSavePath + FileName +  '_Ternary_RawData_' + type + 'Axis.pdf')

    # MAKING TERNARY DIAGRAM OF RAW DATA:
    fig, ax = plt.subplots()
    triplot(dataset=dataset, mask=None, legend=None, type=type, dataform='multiple')
    
    # MAKING TERNARY DIAGRAM OF CONTOURS:
    tri_y=[]
    tri_x=[]

    # Converting the 3D ternary data of [A, B, C] into 2D coordinates of [x,y] which correspond to the area within the ternary bounds. New data is thus tri_y and tri_x.
    for i in range (len(dataset)): # Number of ternary coordinates (Si, Fe, Mg trio's).
        tri_y.append(dataset[i][0]/(dataset[i][0]+dataset[i][1]+dataset[i][2]))
        tri_x.append(np.array(-0.5)*(np.array(1.)-tri_y[i])+(dataset[i][2]/(dataset[i][0]+dataset[i][1]+dataset[i][2])))
    
    fig, ax = plt.subplots()
    Tern_Base()

    y_Ternary = tri_y
    x_Ternary = tri_x
    xmin_Ternary, xmax_Ternary = -0.6, 0.6
    ymin_Ternary, ymax_Ternary = -0.1, 1.1

    # Peform the kernel density estimate
    xx_Ternary, yy_Ternary = np.mgrid[xmin_Ternary:xmax_Ternary:300j, ymin_Ternary:ymax_Ternary:300j]
    positions_Ternary = np.vstack([xx_Ternary.ravel(), yy_Ternary.ravel()])
    values_Ternary = np.vstack([x_Ternary, y_Ternary])
    kernel_Ternary = st.gaussian_kde(values_Ternary)
    f_Ternary = np.reshape(kernel_Ternary(positions_Ternary).T, xx_Ternary.shape)
    ContColour_Ternary = plt.contourf(xx_Ternary, yy_Ternary, f_Ternary, NumLevels, cmap=Colour)
    # Making a white background for contour levels below the value specified by the user ('WhiteCutoff')
    ContColour_Ternary.cmap.set_under('w')
    ContColour_Ternary.set_clim(WhiteCutoff)
    if ContLines == 'y':
        cset_Ternary = plt.contour(xx_Ternary, yy_Ternary, f_Ternary, NumLevels, colors='k', alpha=1, linewidths = 0.5, linestyles = '-')
        if == 'y':
            ax.clabel(cset, inline=1, fontsize=5)
    ax.axis('off')
    fig.savefig(FigureSavePath + FileName +  '_Ternary_Contour_' + type + 'Axis.pdf')


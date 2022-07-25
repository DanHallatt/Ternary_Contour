# This function was originally written by Dan Hallatt, in-part using the ternary plotter made by Corentin Le Guillou. Both at the Université de Lille.

import numpy as np
import pandas as pd
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker
import matplotlib.tri as tri
import scipy.stats as st
from scipy.interpolate import griddata

from Tern_Base import Tern_Base

def Ternary_Contour(dataset, type, Colour, NumLevels, ContourValues, ContLines, ContColourFill, DataPointDisp, NormOption, FigureSavePath, FileName):
    """ Uses matplotlib to plot a ternary diagram
    ** dataset : in the form of a list of list [ [ [A11, B11, C11], ... [A1n, B1n, .. C1n] ], [ [A21, B21, C21], ... [A2n, B2n, .. C2n] ] , ... [ [Am1, Bm1, Cm1], ... [Amn, Bmn, .. Cmn] ] ], where n is the numer of datapoints in a given dataset and m is the number of datasets to plot individually. Even if m = 1, data must be in form of [ [A11, B11, .. C11], ... [A1n, B1n, C1n] ], where dataset[0] = [ [A11, B11, .. C11], ... [A1n, B1n, C1n] ] and not = [A11, B11, C11]. Note that for the ternary diagram, A is the top corner, B is the left corner, and C the right corner of the triangle (A = Si + Al, B = Fe, C = Mg for example)
        
        !!! NOTE !!! : Data cannot contain 'NaN' values. Must be cleaned prior to input in this function (or this function modified to clean data by removing them).
        
    ** type : Either 'silicate' [Si+Al, Mg, Fe], 'silicateHydration' [Si+Al, Mg+Fe, O], or 'sulfide' [S, Ni, Fe].
    ** Colour : In quotations a list of the colour of the contour plots in form of ['Blues', 'Reds', ect..]. Number of colours defined must = m. Options available according to 'cmap' of matplotlib (https://matplotlib.org/stable/tutorials/colors/colormaps.html). Still required to be defined even if ContColourFill == 'n'.
    ** NumLevels: number of contour levels.
    ** ContourValues : Either 'y' (yes) or 'n' (no), to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    ** ContLines : Either 'y' (yes) or 'n' (no), plot or not to plot the lines seperating contour levels.
    ** ContColourFill : Either 'y' (yes) or 'n' (no), to fill contour values with the colours defined in 'Colour' list.
    ** DataPointDisp : Either 'y' (yes) or 'n' (no), to plot the individual datapoints in the ternary diagram.
    ** NormOption : Either 'y' (yes) or 'n' (no), to normalize the KDE values to be within [0,1] domain. Allows for interpretation of contour lines to be limit beyond which samples are less likely to be found beyond than the most-likely area.
    ** FigureSavePath : Path to folder location where figures should be saved. Must be in single quotations, example : '/Volumes/Samsung_T5/Experiment categories/Laser/Figures/'
    ** FileName : General name of files to be saved. Must be in single quotations, example : 'TEST_DataSet01'
    ** ContourValues : Either 'y' (yes) or 'n' (no), plot or not to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    """
    
    ContourLabelTextSize = 0.5
    ContourLineThickness = 0.4
    ContourLineStyle = '-'
    DataPointSize = 0.5
    DataPointColour = 'dim-grey'
    DataPointTransparency = 0.5
    
    # MAKING TERNARY DIAGRAM OF CONTOURS:
    fig, ax = Tern_Base(type)
    for k in range(0,len(dataset)): # Each loop is an individual dataset (corresponding to a single colour in 'Colour')
        tri_y=[]
        tri_x=[]
        Data_Indiv = dataset[k]
        # Converting the 3D ternary data of [A, B, C] into 2D coordinates of [x,y]. New data is thus tri_y and tri_x.
        for i in range (len(Data_Indiv)): # Number of ternary coordinates (Si, Fe, Mg trio's).
            tri_y.append(Data_Indiv[i][0]/(Data_Indiv[i][0]+Data_Indiv[i][1]+Data_Indiv[i][2]))
            tri_x.append(np.array(-0.5)*(np.array(1.)-tri_y[i])+(Data_Indiv[i][2]/(Data_Indiv[i][0]+Data_Indiv[i][1]+Data_Indiv[i][2])))
        y = tri_y
        x = tri_x
        xmin, xmax = -0.6, 0.6
        ymin, ymax = -0.1, 1.1

        # Peform the kernel density estimate
        kernel = st.gaussian_kde(np.vstack([x, y]))
        xx, yy = np.mgrid[xmin:xmax:1000j, ymin:ymax:1000j]
        f = kernel(np.vstack([xx.flatten(), yy.flatten()]))
        if NormOption == 'y':
            f = (f - f.min()) / (f.max() - f.min())
        f = f.reshape(xx.shape)
        
        # Including all th possible user-specified combinations of displaying contour colour, lines, & contour values.
        if ContColourFill == 'y':
            ContColour = plt.contourf(xx, yy, f, NumLevels, cmap=Colour[k], locator = ticker.MaxNLocator(prune = 'lower', nbins=NumLevels), zorder=5)
        if ContLines == 'n' and ContourValues == 'y':
            ContourLineThickness = 0
            if ContColourFill == 'y': # Gauruntee same levels as colour levels
                cset = plt.contour(xx, yy, f, ContColour.levels, colors='k', alpha=1, linewidths = ContourLineThickness, linestyles = ContourLineStyle, zorder=10, extend='both') # Drawing contour lines.
            else: #Making their own levels, without coloured levels.
                cset = plt.contour(xx, yy, f, NumLevels, colors='k', alpha=1, linewidths = ContourLineThickness, linestyles = ContourLineStyle, locator = ticker.MaxNLocator(prune = 'lower', nbins=NumLevels), zorder=10) # Drawing contour lines.
            ax.clabel(cset, inline=1, fontsize=ContourLabelTextSize, zorder=15) # Labelling contour levels within the contour lines.
        if ContLines == 'y':
            if ContColourFill == 'y': # Gauruntee same levels as colour levels.
                cset = plt.contour(xx, yy, f, ContColour.levels, colors='k', alpha=1, linewidths = ContourLineThickness, linestyles = ContourLineStyle, zorder=10) # Drawing contour lines.
            else:
                cset = plt.contour(xx, yy, f, NumLevels, colors='k', alpha=1, linewidths = ContourLineThickness, linestyles = ContourLineStyle, locator = ticker.MaxNLocator(prune = 'lower', nbins=NumLevels), zorder=10) # Drawing contour lines.
            if ContourValues == 'y':
                ax.clabel(cset, inline=1, fontsize=ContourLabelTextSize, zorder=15) # Labelling contour levels within the contour lines.
        if DataPointDisp=='y':
            ax.scatter(tri_x, tri_y, color=DataPointColour, alpha=DataPointTransparency, s=DataPointSize, zorder=5)

    ax.axis('off')
    fig.savefig(FigureSavePath + FileName +  '_Ternary_Contour_' + type + 'Axis.pdf')


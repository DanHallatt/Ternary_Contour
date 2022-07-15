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



# A) "Ternary_Contour" : plots ternary contour plot, using a data in the form [[A1, B1, C1], [A2, B2, C2], ...]. Also plots a ternary plot of all of the raw data, for comparison/check of the contours.

#   A.1) "Tern_Base" : defines the base structure (axis names, stoichiometric reference lines, ect..) of the ternary plot.

def Ternary_Contour(dataset, type, Colour, NumLevels, ContourValues, ContLines, ContColourFill, DataPointDisp, FigureSavePath, FileName):
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
    ** FigureSavePath : Path to folder location where figures should be saved. Must be in single quotations, example : '/Volumes/Samsung_T5/Experiment categories/Laser/Figures/'
    ** FileName : General name of files to be saved. Must be in single quotations, example : 'TEST_DataSet01'
    ** ContourValues : Either 'y' (yes) or 'n' (no), plot or not to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    """
    
    StoichTextSize = 11
    StoichMarkerSize = 8
    StoichLineWidth = 1
    StoichLineColour = 'dimgrey'
    StoichTextColour = 'dimgrey'
    EndMemberTextSize = 13
    AxisTickSize = 5
    AxisLineWidth = 0.5
    
    def Tern_Base():
        """
        This is specifically the base style of the ternary plot.
        - defines axis positions, stoichiometric reference lines/locations.
        """
        ax.plot([-0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0],  [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], color = 'black', marker="_", markersize=AxisTickSize, linewidth=AxisLineWidth)
        ax.plot([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],  [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0], color='black', marker="_",  markersize=AxisTickSize, linewidth=AxisLineWidth)
        ax.plot([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5], [0,0,0,0,0,0,0,0,0,0,0], color='black', marker="|",  markersize=AxisTickSize, linewidth=AxisLineWidth)
        
        if type == 'silicate':
            ax.plot([0.29, -0.29], [0.4, 0.4], linestyle=':', color=StoichLineColour, linewidth=StoichLineWidth)
            ax.annotate('Serp', xy=(0.3, 0.4), xytext = (0.32, 0.39), size=StoichTextSize, color=StoichTextColour)
            
            ax.plot([0.21, -0.21], [0.57, 0.57], linestyle=':', color=StoichLineColour, linewidth=StoichLineWidth)
            ax.annotate('Sap', xy=(0.21, 0.57), xytext = (0.23, 0.56), size=StoichTextSize, color=StoichTextColour)
            
            ax.plot([0.329, -0.329], [0.333, 0.333], linestyle='--', color=StoichLineColour, linewidth=StoichLineWidth)
            ax.annotate('Ol', xy=(0.333, 0.333), xytext = (0.35, 0.32), size=StoichTextSize, color=StoichTextColour)
            
            ax.plot([0.24, -0.24], [0.5, 0.5], linestyle='--', color=StoichLineColour, linewidth=StoichLineWidth)
            ax.annotate('Py', xy=(0.25, 0.50), xytext = (0.27, 0.49), size=StoichTextSize, color=StoichTextColour)
            
            ax.annotate('Si + Al', xy=(0.2, 1.), xytext = (-0.06, 1.03), size=EndMemberTextSize)
            ax.annotate('Fe', xy=(-0.55,0.0), xytext = (-0.57,-0.03), size=EndMemberTextSize)
            ax.annotate('Mg', xy=(0.55,0.0), xytext = (0.53, -0.03), size=EndMemberTextSize)

        if type == 'sulfide':
            ax.plot(-0.25, 0.5, 'ro', markersize=StoichMarkerSize)
            ax.annotate('Troilite', xy=(-0.25, 0.5), xytext = (-0.4, 0.5), size=StoichTextSize, color=StoichTextColour)
            
            ax.plot(0.0, 0.47, 'bo', markersize=StoichMarkerSize)
            ax.annotate('Pentlandite', xy=(0.0, 0.47), xytext = (0.03,0.47), size=StoichTextSize, color=StoichTextColour)
            
            ax.plot(-0.17,0.67, 'go',  markersize=StoichMarkerSize)
            ax.annotate('Pyrite', xy=(-0.17,0.67), xytext = (-0.32,0.67), size=StoichTextSize, color=StoichTextColour)
                            
            ax.plot([-0.25, -0.22], [0.5, 0.56], color='purple', linewidth=StoichLineWidth)
            ax.annotate('Pyrrhotite', xy=(-0.235, 0.55), xytext = (-0.42,0.55), size=StoichTextSize, color=StoichTextColour)
                
            ax.annotate('S', xy=(0., 1.0), xytext = (-0.05, 1.03), size=EndMemberTextSize)
            ax.annotate('Fe', xy=(-0.55,0.0), xytext = (-0.56,-0.03), size=EndMemberTextSize)
            ax.annotate('Ni', xy=(0.55,0.0), xytext = (0.52, -0.03), size=EndMemberTextSize)
            
        if type == 'silicateHydration':
            ax.plot(-0.21, 0.142857, marker="3", color= StoichLineColour, markersize=StoichMarkerSize, alpha=0.5)
            ax.annotate('Serp', xy=(-0.2, 0.14), xytext = (-0.235,0.05), size=StoichTextSize, color=StoichTextColour)
            
            ax.annotate('Si + Al', xy=(0.01, 1.0), xytext = (-0.06, 1.05), size=EndMemberTextSize)
            ax.annotate('O', xy=(-0.55,0.), xytext = (-0.57,-0.03), size=EndMemberTextSize)
            ax.annotate('Mg + Fe', xy=(0.55,0.0), xytext = (0.53, -0.03), size=EndMemberTextSize)
    
    # MAKING TERNARY DIAGRAM OF CONTOURS:
    fig, ax = plt.subplots()
    Tern_Base()
    for k in range(0,len(dataset)):
        tri_y=[]
        tri_x=[]
        Data_Indiv = dataset[k]
        # Converting the 3D ternary data of [A, B, C] into 2D coordinates of [x,y] which correspond to the area within the ternary bounds. New data is thus tri_y and tri_x.
        for i in range (len(Data_Indiv)): # Number of ternary coordinates (Si, Fe, Mg trio's).
            tri_y.append(Data_Indiv[i][0]/(Data_Indiv[i][0]+Data_Indiv[i][1]+Data_Indiv[i][2]))
            tri_x.append(np.array(-0.5)*(np.array(1.)-tri_y[i])+(Data_Indiv[i][2]/(Data_Indiv[i][0]+Data_Indiv[i][1]+Data_Indiv[i][2])))
        y_Ternary = tri_y
        x_Ternary = tri_x
        xmin_Ternary, xmax_Ternary = -0.6, 0.6
        ymin_Ternary, ymax_Ternary = -0.1, 1.1

        # Peform the kernel density estimate
        xx_Ternary, yy_Ternary = np.mgrid[xmin_Ternary:xmax_Ternary:1000j, ymin_Ternary:ymax_Ternary:1000j]
        positions_Ternary = np.vstack([xx_Ternary.ravel(), yy_Ternary.ravel()])
        values_Ternary = np.vstack([x_Ternary, y_Ternary])
        kernel_Ternary = st.gaussian_kde(values_Ternary)
        f_Ternary = np.reshape(kernel_Ternary(positions_Ternary).T, xx_Ternary.shape)
        ContColour_Ternary = plt.contourf(xx_Ternary, yy_Ternary, f_Ternary, NumLevels, cmap=Colour[k], locator = ticker.MaxNLocator(prune = 'lower'))
        if ContLines == 'y':
            cset_Ternary = plt.contour(xx_Ternary, yy_Ternary, f_Ternary, NumLevels, colors='k', alpha=1, linewidths = 0.5, linestyles = '-') # Drawing contour lines.
            if ContourValues == 'y':
                ax.clabel(cset_Ternary, inline=1, fontsize=5) # Labelling contour levels within the contour lines.
        if DataPointDisp=='y':
            ax.scatter(tri_x, tri_y, color='black', alpha=1, s=0.5)    ax.axis('off') # Plotting individual datapoints.
    ax.axis('off')
    fig.savefig(FigureSavePath + FileName +  '_Ternary_Contour_' + type + 'Axis.pdf')


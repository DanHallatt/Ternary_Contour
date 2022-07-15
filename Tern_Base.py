# This function was originally written by Corentin Le Guillou, and later modified by Dan Hallatt, both at the Université de Lille.

import math
import matplotlib.pyplot as plt
import matplotlib.style as mpl_style
import matplotlib as mpl
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from sigfig import round
from statistics import mean
import scipy.stats as st

def Tern_Base(type):
    """
    This is specifically the base style of the ternary plot.
    - defines axis positions, stoichiometric reference lines/locations.
    """
    
    StoichTextSize = 9.5
    StoichMarkerSize = 8
    StoichLineWidth = 1
    StoichLineColour = 'dimgrey'
    StoichTextColour = 'dimgrey'
    EndMemberTextSize = 13
    AxisTickSize = 5
    AxisLineWidth = 1
    
    fig, ax = plt.subplots()
    ax.plot([-0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0],  [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], color = 'black', marker="_", markersize=AxisTickSize, linewidth=AxisLineWidth)
    ax.plot([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],  [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0], color='black', marker="_",  markersize=AxisTickSize, linewidth=AxisLineWidth)
    ax.plot([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5], [0,0,0,0,0,0,0,0,0,0,0], color='black', marker="|",  markersize=AxisTickSize, linewidth=AxisLineWidth)
    
    if type == 'silicate':
        ax.plot([0.29, -0.29], [0.4, 0.4], linestyle=':', color=StoichLineColour, linewidth=StoichLineWidth, zorder=1)
        ax.annotate('Serp', xy=(0.3, 0.4), xytext = (0.32, 0.39), size=StoichTextSize, color=StoichTextColour)
        
        ax.plot([0.21, -0.21], [0.57, 0.57], linestyle=':', color=StoichLineColour, linewidth=StoichLineWidth, zorder=1)
        ax.annotate('Sap', xy=(0.21, 0.57), xytext = (0.23, 0.56), size=StoichTextSize, color=StoichTextColour)
        
        ax.plot([0.329, -0.329], [0.333, 0.333], linestyle='--', color=StoichLineColour, linewidth=StoichLineWidth, zorder=1)
        ax.annotate('Ol', xy=(0.333, 0.333), xytext = (0.35, 0.32), size=StoichTextSize, color=StoichTextColour)
        
        ax.plot([0.24, -0.24], [0.5, 0.5], linestyle='--', color=StoichLineColour, linewidth=StoichLineWidth, zorder=1)
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

    return fig, ax

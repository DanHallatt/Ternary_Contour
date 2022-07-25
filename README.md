# Ternary_Contour
Plots a series of 3-dimensional data on a ternary diagram in the form of a contour map. Contours are based on 'spatial'-density of datapoints in the domain of the ternary plot, which is a representation of the bivariate PDF constructed from the bivariate KDE. Multiple 'sets' of series of 3D data can be plotted on the same figure, each with different colours of their contour maps.

* requires download of Tern_Base function as well.

<!-- Options -->
## Options
 User can specify the following parameters when calling the function:
 - choose the colours of the contour colours, according to cmap available options (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
 - choose the number of contours.
 - to plot contour lines.
 - to display values of the contour level values within the contour lines.
 - to plot the individual datapoints of each dataset.
 - to plot multiple datasets.
 - choose the end-members of the plot, which must match the content of the input dataset (systems are: [Si+Al, Mg, Fe], [Si+Al, Mg+Fe, O], or [S, Ni, Fe]).

User can also easily adjust plotting preferences (such as text size and stoichiometric line colour) by adjusting the variables defined within the first lines of the function, if so wishes.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Example output -->
## Example output

It should be noted that all data must be in the form of a list (of the different groups of data with different contour colours) of lists (of multiple datapoints for each contour) of lists (for each datapoint, for example [Si + Al, Mg, Fe]):

<br />
<div align="center">
 
 [ [ [A11, B11, C11], ... [A1n, B1n, .. C1n] ], ... [ [Am1, Bm1, Cm1], ... [Amn, Bmn, .. Cmn] ] ]
 
 </div>

- where n is the numer of datapoints in a given dataset (a particular colour of contours) and m is the number of datasets to plot individually (the number of individual contour plots of differing colours). Even if m = 1, data must be in the form of [ [A11, B11, .. C11], ... [A1n, B1n, C1n] ], where dataset[0] = [ [A11, B11, .. C11], ... [A1n, B1n, C1n] ] and not = [A11, B11, C11]. Note that for the ternary diagram, A is the top corner, B is the left corner, and C the right corner of the triangle (A = Si + Al, B = Fe, C = Mg for example)


<br />
<div align="center">

[![Product Name Screen Shot][product-screenshot]](https://example.com)
 
 </div>

This figures above were generated from the following user-specified options:
 - dataset = [[[A11, B11, C11], ...[A1n, B1n, C1n]], [[A21, B21, C21], ...[A2n, B2n, C2n]]] where A = Si+Al, B = Fe, and C = Mg at.%
     - red: data_1 (such as A11), blue: data_2 (such as A21)
 - Colour = ['Blues', 'Reds']
 - type = 'silicate'
 - and differing data options for each sub-figure:
     - A) ContLines = 'n',  ContourValues = 'n',  ContColourFill = 'y',  DataPointDisp = 'y', NormOption = 'n', ContourLevels = 8
     - B) ContLines = 'y',  ContourValues = 'y',  ContColourFill = 'y',  DataPointDisp = 'n', NormOption = 'y', ContourLevels = [0.1,0.25,0.5,0.68, 0.95, 1]
     - C) ContLines = 'n',  ContourValues = 'n',  ContColourFill = 'y',  DataPointDisp = 'n', NormOption = 'n', ContourLevels = 8

 
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community what it is. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Dan Hallatt - daniel.hallatt@univ-lille.fr

Project Link: [https://github.com/DanHallatt/Ternary_Contour](https://github.com/DanHallatt/Ternary_Contour)

Associated Institute Link: https://umet.univ-lille.fr/MTP/index.php?lang=fr

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Related repositories -->
## Related repositories
- plotting contours of compositions/metrics in 2D: https://github.com/DanHallatt/TwoDim_Contour
- making a video of dynamic ternary contours, as a window slides through the series of data: https://github.com/DanHallatt/Ternary_Contour_Vid
- making a video of dynamic contours compositions/metrics in 2D, as a window slides through the series of data: https://github.com/DanHallatt/TwoDim_Contour_Vid

<p align="right">(<a href="#top">back to top</a>)</p>


[product-screenshot]: Images/ExampleTernaryPlotOptions.png

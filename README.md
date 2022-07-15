# Ternary_Contour
Plots a series of 3-dimensional data on a ternary diagram in the form of a contour map. Contours are based on 'spatial'-density of datapoints in the domain of the ternary plot. Multiple 'sets' of series of 3D data can be plotted, each with different colours of their contours.

<!-- Options -->
## Options
 User can specify the following parameters when calling the function:
 - choode the colours of the contour colours, according to cmap available options (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
 - choose number of contours.
 - to plot contour lines.
 - to display values of the contour level values within the contour lines.
 - to plot individual data.
 - choose the end-members of the plot, which must match the content of the input dataset (systems are: [Si+Al, Mg, Fe], [Si+Al, Mg+Fe, O], or [S, Ni, Fe]).

User can also easily adjust plotting preferences (such as text size and stoichiometric line colour) by adjusting the variables defined within the first lines of the function, if so wishes.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Example output -->
## Example output

<br />
<div align="center">

[![Product Name Screen Shot][product-screenshot]](https://example.com)
 
 </div>

This figure was generated from the following user-specified options:
 - dataset = [[A1, B1, C1], [A2, B2, C2], ...[An, Bn, Cn]] where A = Si+Al, B = Fe, and C = Mg at.%
 - ContLines = 'n'
 - NumLevels = 8
 - Colour = 'Blues'
 - type = 'silicate'
 
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


[product-screenshot]: Images/ExampleTernaryPlot.png

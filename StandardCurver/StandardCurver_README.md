# StandardCurver version 1.1

This program takes in a raw .csv file of concentration and absorbance data from 


### Dependencies

- python3 (vers. 3.8.5)
- datetime (https://docs.python.org/3/library/datetime.html)
- argparse (https://docs.python.org/3/library/argparse.html)
- matplotlib (https://matplotlib.org)
- pandas (https://pandas.pydata.org/)
- numpy (https://www.numpy.org/)
- scipy (https://www.scipy.org/)


### Input

Input .csv file that contains two columns of equal length: 'Concentration' and 'Absorbance'
Optional .csv file that contains two columns of equal length: 'Sample' and 'UnknownAbs'
Wavelength argument: wavelength that absorbance was captured at (for example: 750nm)
Optional output file name argument: use .pdf file ending to save as a .pdf; defaults to 
"StandardCurve{date}" where date will be grabbed from your computer in m_d_y format.


### Options

Used for creation of standard curve figures from DC/BCA/Bradford Assays and calculation of
unknown protein concentrations

```
Options:
  -h, --help            show this help message and exit
  -a INPUT1, --input1 INPUT1
                        Standard Curve data (as 'Concentrations' and
                        'Absorbances')
  -b INPUT2, --input2 INPUT2
                        Unknown sample absorbances (as 'UnknownAbs')
  -w WAVELENGTH, --wavelength WAVELENGTH
                        Wavelength(nm)
  -o OUTPUT, --output OUTPUT
                        output file name and file extension
```

### Usage

```
usage: StandardCurver.py -a stdcurvedata -b unknownsampledata -w 750nm -o outputfilename.pdf
```
To get usage info:

```
StandardCurver.py -h
```


### Output

You will receive one graph that includes 1) line of best fit for your standard curve, 2)
your observed standard values, 3) the regression line equation printed on the graph, and 4)
the R-squared value for the regression line.


Copyright (C) 2021 Phillip Kalaniopio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

If you have any questions about either this program or the GNU General Public License,
please email me at Phillip.Kalaniopio@nau.edu
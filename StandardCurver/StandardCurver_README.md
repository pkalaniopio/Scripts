# StandardCurver version 1.1
This program takes in a raw .csv file of concentration and absorbance data from any type of
protein concentration assay (e.g., RC/DC, Lowry, BCA, Bradford Assay, etc.) in order to 
generate a standard curve and regression line in order to determine unknown protein sample
concentrations. 


### Dependencies

- python3 (vers. 3.8.5)
- datetime (https://docs.python.org/3/library/datetime.html)
- argparse (https://docs.python.org/3/library/argparse.html)
- matplotlib (https://matplotlib.org)
- pandas (https://pandas.pydata.org/)
- numpy (https://www.numpy.org/)
- scipy (https://www.scipy.org/)


### Input

	1. **.csv file** that contains two columns of equal length: **'Concentration' and 'Absorbance'**
	2. **Wavelength** that absorbance was captured at (for example: 750nm)
	3. **Optional .csv file** that contains two columns of equal length: **'Sample' and 'UnknownAbs'**
	4. **Optional output file name** use .pdf file ending to save as a .pdf; defaults to 
	"StandardCurve{date}" where date will be grabbed from your computer in m_d_y format.

### Usage

To get usage info:
```
StandardCurver.py -h
```
```
usage: StandardCurver.py -a stdcurvedata -b unknownsampledata -w 750nm -o outputfilename.pdf
```

### Options
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

### Output

You will receive one graph that includes:
	- line of best fit for your standard curve
	- your observed standard values
	- the regression line equation printed on the graph
	- the R-squared value for the regression line.

If you utilize the optional input2 argument and provide unknown protein samples you will 
also receive:
	- an excel spreadsheet with calculated concentrations from your regression line


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
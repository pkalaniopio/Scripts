# GO_parser_plotter version 1.1
This program is intended to take gene ontology (GO) enrichment data from an RNASeq experiment,
parse thru, grab relevant columns, and create user-defined heatmaps (Salanga Lab specific)


This program takes two tab-delimited (.tsv) input files. Both should be differentially 
expressed gene (DEG) gene ontology (GO) enrichment analysis data that contains at the bare
minimum, two columns: 1) GO term description (i.e., DNA binding) and 2) over-represented 
p-value. These are entered in via the command line using the -a and -b arguments respectfully.
In order to get a graph that looks nicer, the -i and -j arguments allow you to rename these
files so that their respective x-axis labels reflect the name that you have given them (and
putting them in quotes allows you to add x-axis labels that have spaces in them). Additionally, 
there is a p-value threshold argument (-p, --pvalue) that will institute a p-value cutoff 
(i.e., 0.5) so that only GO terms with an overrepresented p-value underneath the threshold
are shown in the resulting heatmap. The last command line argument is (-o, --output), which
is your preferred output file name with the desired extension at the end (i.e., output_file.pdf).

### Version 1.2

Version 1.2 of GO_parser_plotter introduces a new command line argument (-c, --color), which allows the user to specify a 
colormap palette for their heatmap given that it is supported by matplotlib and seaborn modules. Version 1.2 also makes 
the graphing portion of the script more readable and efficient, as well as updated help and usage information.


### Dependencies

- python3 (vers. 3.8.5)
- argparse (https://docs.python.org/3/library/argparse.html)
- matplotlib (https://matplotlib.org)
- pandas (https://pandas.pydata.org/)
- seaborn (https://seaborn.pydata.org/#)


### Input
1. **two input files (.tsv)** of Novogene DEG Gene Ontology term data with 2 columns (at minimum) labeled as "Description" and "Over_represented_pValue"
2. **input file names** for labeling the x-axis of the heatmap
3. **p-value threshold** for GO term inclusion
4. **output file name and extension** (e.g., output.pdf)
5. **colormap palette** (e.g., viridis)


### Usage
```
GO_parser_plotter_v1.2.py -a input_file1 -i "input_file1name" -b input_file2 -j "input_file2name" -p pvalue_threshold -o output_file_name -c colormap
```


### Options
```
Options:
  -h, --help            show this help message and exit
  -a INPUT1, --input1 INPUT1
                        Unformatted DEG file, one condition, relative path
  -i INPUT1NAME, --input1name INPUT1NAME
                        Input 1 name for graph
  -b INPUT2, --input2 INPUT2
                        Unformatted DEG file, one condition, relative path
  -j INPUT2NAME, --input2name INPUT2NAME
                        Input 2 name for graph
  -p PVALUE, --pvalue PVALUE
                        P-value threshold
  -o OUTPUT, --output OUTPUT
                        output file name, file extension
  -c COLOR, --color COLOR
                        colormap, any matplotlib supported palette
```


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
please email me at Phillip.Kalaniopio@nau.eduIf you have any questions about either this program or the GNU General Public License,
please email me at Phillip.Kalaniopio@nau.edu
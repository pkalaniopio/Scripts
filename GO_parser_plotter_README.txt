GO_parser_plotter User Manual - version 1.1

#######################################################################################################################
# This GO_parser_plotter software is intended to take gene ontology (GO) enrichment data from a Novogene RNASeq,      #
# parse thru, grab relevant columns, and create user-defined heatmaps (Salanga Lab specific)                          #
# Created by: Phillip Kalaniopio; Last edited: 4/22/2021                                                              #
#######################################################################################################################

This code takes two (2) input files. Both should be differentially expressed gene (DEG) gene ontology (GO) enrichment 
analysis data that contains at the bare minimum, two columns: 1) GO term description (i.e., DNA binding) and an 2) over-
represented p-value column. These are entered in via the command line using the -a and -b arguments respectfully. In order
to get a graph that looks nicer, the -i and -j arguments allow you to rename these files so that their respective x-axis 
labels reflect the name that you have given them (and putting them in quotes allows you to add x-axis labels that have spaces
in them). Additionally, there is a p-value threshold argument (-p, --pvalue) that will institute a p-value cutoff (i.e., 0.5) 
so that only genes with an overrepresented p-value underneath the threshold are shown in the resulting heatmap. The last 
command line argument is (-o, --output), which is your preferred output file name with the desired extension at the end 
(i.e., output_file.pdf). 

Version 1.2

Version 1.2 of GO_parser_plotter introduces a new command line argument (-c, --color), which allows the user to specify a 
colormap palette for their heatmap given that it is supported by matplotlib and seaborn modules. Version 1.2 also makes 
the graphing portion of the script more readable and efficient, as well as updated help and usage information.


Dependencies:



Python Modules:

argparse
matplotlib.pyplot
pandas
seaborn

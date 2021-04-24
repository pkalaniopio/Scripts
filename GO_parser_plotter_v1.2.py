#!/usr/bin/env python3

#######################################################################################################################
# This GO_parser_plotter software is intended to take gene ontology (GO) enrichment data from a Novogene RNASeq,      #
# parse thru, grab relevant columns, and create user-defined heatmaps (Salanga Lab specific)                          #
# Created by: Phillip Kalaniopio; Last edited: 4/24/2021                                                              #
#######################################################################################################################

version = "1.2"
print("You are using Phillip Kalaniopio's GO_parser_plotter version %s" % version)

# import modules
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# set parser variable as the argumentParser call and give user usage documentation
parser = argparse.ArgumentParser(
    usage='python GO_parser_plotter.py -a input_file1 -i "input_file1name" -b input_file2 -j "input_file2name" -p pvalue_threshold -o output_file_name -c colormap',
    add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter)

# add arguments as specified with corresponding help documentation
parser.add_argument("-a", '--input1', help="Unformatted DEG file, one condition, relative path", required=True)
parser.add_argument("-i", '--input1name', help="Input 1 name for graph", required=True)
parser.add_argument("-b", '--input2', help="Unformatted DEG file, one condition, relative path", required=True)
parser.add_argument("-j", '--input2name', help="Input 2 name for graph", required=True)
parser.add_argument('-p', '--pvalue', help='P-value threshold', required=True)
parser.add_argument('-o', '--output', help='output file name, file extension', default="parser_plotter_output.pdf")
parser.add_argument('-c', '--color', help='colormap, any matplotlib supported palette', default="plasma_r")

# set args variable as the parse_args() using dot notation for parser
args = parser.parse_args()

# import files

inFile1 = pd.read_csv(args.input1, sep='\t')
inFile2 = pd.read_csv(args.input2, sep='\t')

df1 = inFile1[['Description', 'Over_represented_pValue']]
df2 = inFile2[['Description', 'Over_represented_pValue']]

print("Data imported!")

# set parameter names
outputFile = args.output

# Parse
nums_dict = {}

for i in df1['Description']:
    for k in df2['Description']:
        if i == k:
            whatIwant = (df1.loc[df1['Description'] == str(i)])
            theOtherThing = (df2.loc[df2['Description'] == str(i)])
            theNumToCompare = whatIwant['Over_represented_pValue'].item()
            theOtherNumToCompare = theOtherThing['Over_represented_pValue'].item()
            if theNumToCompare < float(args.pvalue) and theOtherNumToCompare < float(args.pvalue):
                nums_dict[str(i)] = [whatIwant['Over_represented_pValue'].item(),
                                     theOtherThing['Over_represented_pValue'].item()]

numbers = []

for nums in nums_dict.values():
    numbers.append(nums)

print("Data has been parsed!")

# Graph
fig, ax = plt.subplots(figsize=(12, 12))

ax = sns.heatmap(numbers, yticklabels=nums_dict.keys(), xticklabels=[str(args.input1name), str(args.input2name)],
                 vmax=args.pvalue, vmin=0, cmap=args.color)

ax.set_xlabel("Conditions", fontsize=14)

fig.savefig(outputFile, dpi=300, bbox_inches='tight')

# open output file for writing, name it via user input, write out output set to it, close it

print("Done!")

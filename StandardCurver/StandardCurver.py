#!/usr/bin/env python3

version = "1.2"
print(f"You are using Phillip Kalaniopio's StandardCurver version {version}")

# import modules
from datetime import date
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats

# set date and save to runDate variables
today = date.today()
runDatetoPlot = today.strftime("%m/%d/%y")
runDatetoWrite = today.strftime("%m_%d_%y")

# use argparse to add user help, arguments, etc.
parser = argparse.ArgumentParser(
	prog='StandardCurver',
	usage='StandardCurver.py -a stdcurvedata -b unknownsampledata -w 750nm -o outputfilename.pdf',
	description ='Used for creation of standard curve figures from RC/DC, BCA, and Bradford Assays and calculation of unknown protein concentrations',
	formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-a", '--input1', help="Standard Curve data (as 'Concentrations' and 'Absorbances')", required=True)
parser.add_argument("-b", '--input2', help="Unknown sample absorbances (as 'UnknownAbs')")
parser.add_argument("-w", '--wavelength', help="Wavelength(nm)", required=True)
parser.add_argument("-c", '--conc', help="Desired protein concentration calculation (ug)", default=20)
parser.add_argument("-d", '--dilution', help="Sample dilution factor", default=10)
parser.add_argument('-o', '--output', help='output file name and file extension', default=f"RCDC_StandardCurve{runDatetoWrite}.pdf")

args = parser.parse_args()

# read in data using pandas
df1 = pd.read_csv(args.input1)
df1 = df1.rename(columns=lambda x: x.strip())

if args.input2:
	df2 = pd.read_csv(args.input2)
	df2 = df2.rename(columns=lambda x: x.strip())
else: 
	pass

# save variables as x and y respectively
x = df1['Concentration']
y = df1['Absorbance']

#Save best fit line to variables
m, b = np.poly1d(np.polyfit(x, y, 1))

# Determine R^2 of regression line & save to variable for plotting
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
r2forPlot = f"$R^2={r_value:.5f}$"

# save m and b values to compiled regression equation for plotting
lineEqforPlot = f"$y={m:.4f}x+{b:.4f}$"

# Initialize graph
fig, ax = plt.subplots(figsize=(20,8))

# plot a best fit line using coefficients from above
ax.plot(x, m*x + b, label='Best Fit Line', c="red", zorder=1)

# scatterplot of points from dataset
ax.scatter(x, y, label="Observed Values", c="black", marker="s", s=200, zorder=2)

# Customization
ax.set_title(f"RC/DC Standard Curve {runDatetoPlot}", fontsize=28)
ax.set_xlabel('Protein Concentration (mg/mL)', fontsize=25)
ax.set_ylabel(f"Absorbance at {args.wavelength}", fontsize=25)
ax.legend(loc='best', fontsize=20, frameon=False)
ax.tick_params(axis='both', which='major', labelsize=18)

# add R^2 value and equation to plot
ax.text(1.25, 0.50, r2forPlot, fontsize=21)
ax.text(1.20, 0.55, lineEqforPlot, fontsize=21)

# save figure
fig.savefig(args.output, dpi=300, bbox_inches='tight')

# figuring out unknown concentrations
unk = df2['UnknownAbs']
df2['Calculated_concentration (ug/uL)'] = (unk - b)/m    # based on rearranging y=mx+b to get x=(y-b)/m
calc = df2['Calculated_concentration (ug/uL)'].astype('float')
df2['Undiluted_concentration (ug/uL)'] = calc * args.dilution
df2['volume/well (uL)'] = (args.conc / calc) / args.dilution
df2.to_excel(f"solved_unknowns{runDatetoWrite}.xlsx",
	columns=['Sample', 'UnknownAbs','Calculated_concentration (ug/uL)','Undiluted_concentration (ug/uL)','volume/well (uL)'], sheet_name="Sheet1")




print("Done!")
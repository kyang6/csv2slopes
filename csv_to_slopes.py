'''
csv_to_slopes.py
-----------------------------------------------------------
Script that takes a directory full of CSV files and finds 
the slopes of the data in that CSV file.

Basics:
	- Pass in the path to a directory including the csv files
	- Pass in the name of a csv file to include all the file:slope pairs

How to Use:
	- make sure python3 is installed
	- install dependencies pip3 install -r requirements.txt
	- call script: 'python3 csv_to_slopes.py 
		--path [PATH TO DIRECTORY]
		--output [NAME OF OUTPUT FILE] 
		--verbose [BOOLEAN]'
	- for help: 'python3 csv_to_slopes.py --help' 
'''
import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import argparse
import os

'''
private function get_slope()
-------------------------------
Reads in CSV file and returns the slope

Input:
	filename 	- path to CSV
	verbose 	- if true, show graph

Return:
	slope 		- slope of data

NOTE:
	Assumes that the X data is in column 3 and Y data is in column 4 (0-indexed)
	Calculates the slope between the voltages 1-8
'''
def get_slope(filename, verbose=False):
	df = pd.read_csv(filename)

	# Find the index when voltage becomes larger than 1V and 8V
	start_idx = None
	end_idx = None
	for idx, data in df.iterrows():
		if(data[4]) > 1 and not start_idx:
			start_idx = idx

		if(data[4]) > 8 and not end_idx:
			end_idx = idx


	# Format the CSV data and get only the correct datapoints
	data_X_train = np.array(df.iloc[start_idx:end_idx,3])
	data_Y_train = np.array(df.iloc[start_idx:end_idx,4])

	data_X_train = data_X_train.reshape(-1, 1)
	data_Y_train = data_Y_train.reshape(-1, 1)

	# Create linear regression object
	regr = linear_model.LinearRegression()

	# Train the model using the training sets
	regr.fit(data_X_train, data_Y_train)

	if(verbose):
		# Plot outputs
		plt.scatter(data_X_train, data_Y_train,  color='black')
		plt.plot(data_X_train, data_Y_train, color='blue', linewidth=3)

		plt.xticks(())
		plt.yticks(())

		plt.show()

	# The coefficients (slope)
	return regr.coef_

'''
private function get_slope_dir()
-------------------------------
Given directory, read in all CSV files, find slopes, and write to CSV file

Input:
	filename 	- path to Dir

Return:
	slope 		- slope of data

'''
def get_slope_dir(path, output, verbose):
	# dictionary to map file to slope
	fs_dict = {}

	# get all entries in path
	dirs = os.listdir(path)

	for file in dirs:
		# if file is csv
		if("csv" in file):
			if(verbose):
				print("Filename: {}".format(file))
			
			slope = float(get_slope('{}/{}'.format(path, file), verbose))	
			
			fs_dict[file] = slope


	if(output):
		with open(output + ".csv", 'w') as csvfile:
			fieldnames = ['filename', 'slope']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

			for file_csv, slope_csv in fs_dict.items():
				writer.writerow({'filename' : file_csv, 'slope' : slope_csv}) 


'''
private function _create_args()
-------------------------------
Creates an argeparse object for CLI 

Input:
	Void

Return:
	args object with required arguments for get_slope

'''
def _create_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--path", help="path to a directory of datasets as CSV", type=str)
	parser.add_argument("--output", help="name of file to write slope to. IE. output", type=str)
	parser.add_argument("--verbose", help="print out helpful data during runtime", type=bool)

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = _create_args()
	get_slope_dir(args.path, args.output, args.verbose)
	






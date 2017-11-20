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
	- Example: 'python3 csv_to_slopes.py --path /Users/admin/Desktop/meilincsv/csv --output file_and_slopes'
	- for help: 'python3 csv_to_slopes.py --help' 


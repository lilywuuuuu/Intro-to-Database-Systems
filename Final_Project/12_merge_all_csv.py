import csv
import glob
import os

# Replace `directory` with the path to the directory containing the CSV files
# Replace `output_filename` with the path to the output CSV file
directory = "/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/stock_data/output"
output_filename = "/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/stock_data/output/output.csv"

# Use the glob module to find the CSV files in the directory
input_filenames = glob.glob(os.path.join(directory, "*.csv"))
# Sort the list of filenames
input_filenames = sorted(input_filenames)

# Open the output file in write mode
with open(output_filename, "w", newline="") as f:
    # Create a CSV writer object
    writer = csv.writer(f)

    # Iterate over the input files
    for input_filename in input_filenames:
        # Open the input file in read mode
        with open(input_filename, "r") as g:
            # Create a CSV reader object
            reader = csv.reader(g)

            # Read the input CSV file line by line
            for row in reader:
                # Write the row to the output file
                writer.writerow(row)
            g.close()

    f.close()

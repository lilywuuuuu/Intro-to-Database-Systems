import csv
import os

# Replace `directory` with the path to the directory
directory = "/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/stock_data/input"

fn = ""

# Use the `os.listdir` function to get a list of the files in the directory
for filename in os.listdir(directory):
    # Use the `os.path.join` function to create the full path to the file
    file_path = os.path.join(directory, filename)

    if (filename == ".DS_Store"):
        continue

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Print the name of the file
        # print(filename)
        fn = filename

    
        # Replace `value` with the value you want to write
        # Replace `input_filename` and `output_filename` with the paths to the input and output CSV files
        value = fn[-16:-12]

        print(value)


        
        # Open the input file in read mode
        with open("/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/stock_data/input/"+fn, "r") as f:
            # Create a CSV reader object
            reader = csv.reader(f)

            # Open the output file in write mode
            with open("/Users/chinlinwu/Documents/6_Introductions_to_Database_Systems/Final_Project/stock_data/output/" + fn, "w", newline="") as g:
                # Create a CSV writer object
                writer = csv.writer(g)

                # Read the input CSV file line by line
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    # Insert the value at the beginning of the row
                    row.insert(0, value)
                    # Write the modified row to the output file
                    writer.writerow(row)
                g.close()
            f.close()
            









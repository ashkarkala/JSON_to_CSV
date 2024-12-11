# This code reads a JSON file and writes the data to a CSV file.
# The JSON file contains an array of objects, and each object has two properties: name and code.
# The code reads the JSON data, extracts the name and code properties from each object, and writes them to a CSV file.
# The CSV file has two columns: header1 and header2, corresponding to the name and code properties, respectively.

import json
import csv

# Read JSON data from a file
with open('input.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)

# Write data to a CSV file
with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['Name', 'Code'])
    # Write the data
    for item in data:
        csv_writer.writerow([item['name'], item['code']])
        print(item['name'], item['code'])
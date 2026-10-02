import json
import csv


class JsonToCsvConverter:

    def convert(self, json_path, csv_path):
        with open(json_path) as json_file:
            jsondata = json.load(json_file)

        data_file = open(csv_path, 'w', newline='')
        csv_writer = csv.writer(data_file)

        count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())

        data_file.close()

    def convert_file(self, json_path, csv_path):
        # Opening JSON file and loading the data into the variable data
        with open(json_path) as json_file:
            data = json.load(json_file)

        employee_data = data['emp_details']

        # now we will open a file for writing
        data_file = open(csv_path, 'w')

        # create the csv writer object
        csv_writer = csv.writer(data_file)

        # Counter variable used for writing headers to the CSV file
        count = 0

        for emp in employee_data:
            if count == 0:

                # Writing headers of CSV file
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1

            # Writing data of CSV file
            csv_writer.writerow(emp.values())

        data_file.close()

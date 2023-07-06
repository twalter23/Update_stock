import csv
import os

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            quantity = row['Quantity']
            manf = row['manf#']
            if manf:  # Skip rows where 'manf' value is empty
                data.append([manf, quantity])
    return data

def write_csv_file(file_path, data):
    directory = os.path.dirname(file_path)
    output_file = os.path.join(directory, 'BOM_FOUND.csv')
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['manf#', 'Quantity']
        writer.writerow(list(header))
        writer.writerows(data)
    print("The 'BOM_FOUND.csv' file has been created.")

def main():
    # Prompt the user to enter the local path of the CSV file
    file_path = input("Enter the local path of the CSV file: ")
    file_path = file_path.strip("& '")

    # Read the CSV file and store the content of 'quantity' and 'manf' columns in a 2D array
    csv_data = read_csv_file(file_path)

    # Write the 2D array into a CSV file named 'BOM_FOUND' at the same path as the opened CSV file
    write_csv_file(file_path, csv_data)


#**********************************************#
#                    main                      #
#**********************************************#
if __name__ == "__main__":
    main()

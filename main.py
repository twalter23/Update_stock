import os
import pandas as pd
import fileinput

def get_BOM_Stock():

    # Prompt the user to enter the path of the Excel file
    stock_path = input("Enter the path of the Excel file: ")
    stock_path = stock_path.replace("& '", "").replace("'", "")

    # Check if the file exists
    if not os.path.isfile(stock_path):
        print("File not found!")
        exit()

    # Read the Excel file using pandas
    Stock = pd.read_excel(stock_path)

    # Prompt the user to enter the path of the CSV file
    BOM_path = input("Enter the path of the CSV BOM file: ")
    BOM_path = stock_path.replace("& '", "").replace("'", "")

    # Check if the file exists
    if not os.path.isfile(BOM_path):
        print("File not found!")
        exit()

    # Read the CSV file using pandas
    BOM = pd.read_csv(BOM_path)

    return BOM, Stock


def main():

    BOM, STOCK = get_BOM_Stock()


#**********************************************#
#                    main                      #
#**********************************************#
if __name__ == "__main__":
    main()

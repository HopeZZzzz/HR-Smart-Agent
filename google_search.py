import openpyxl
import csv
from googlesearch import search

# Use the full path to the Excel file
file_path = "/Users/mac/Desktop/LinkedinProject/search_terms.xlsx"
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

# Create or open a CSV file to store the results
output_file = "/Users/mac/Desktop/LinkedinProject/search_results.csv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Search Term', 'Rank', 'URL'])  # Write the header row

    # Iterate through the rows and perform searches
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming first row is header
        search_term = row[0]  # Assuming the search term is in the first column
        print(f"Searching for: {search_term}")
        
        try:
            # Perform Google search and write results to the CSV file
            for rank, result in enumerate(search(search_term, num_results=100), start=1):  # Adjust number of results if needed
                writer.writerow([search_term, rank, result])
        except Exception as e:
            print(f"An error occurred while searching for '{search_term}': {e}")

print(f"Searches completed. Results are stored in '{output_file}'.")

import csv
import requests

# Replace with your API key and Custom Search Engine ID
API_KEY = ''
CSE_ID = ''

# Function to perform a Google search query
def google_search(query, api_key, cse_id, num_results=10):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'num': num_results,
    }
    response = requests.get(search_url, params=params)
    return response.json()

# Function to read CSV and perform searches
def search_companies(csv_file_path):
    search_results = []

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            company_name = row['Company Name']  # Replace with your actual CSV column name
            query = f'site:linkedin.com/in "{company_name}" (intitle:clinical director OR intitle:medical director)' #intitle:CEO OR intitle:Managing Director OR intitle:Chief Executive OR intitle:Senior Manager OR intitle:clinical OR intitle:medical
            print(f"Searching for: {query}")
            
            result = google_search(query, API_KEY, CSE_ID)
            
            for item in result.get('items', []):
                search_results.append({
                    'Company Name': company_name,
                    'Title': item.get('title'),
                    'Link': item.get('link'),
                    'Snippet': item.get('snippet')
                })
    
    # Writing the search results to a new CSV file
    output_file = '/Users/mac/Desktop/LinkedinProject/search_results.csv'
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Company Name', 'Title', 'Link', 'Snippet']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in search_results:
            writer.writerow(result)

    print(f"Search results saved to {output_file}")

# Call the function with the path to your CSV file
search_companies('/Users/mac/Desktop/LinkedinProject/pharmaceutical_companies.csv')

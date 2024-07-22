import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to retrieve the webpage')
    exit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract data
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

# Step 4: Store data in a list
data = []
for row in rows:
    cols = row.find_all(['th', 'td'])  # Use 'th' for headers and 'td' for data
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Step 5: Convert data to a DataFrame and save to CSV
# The columns are specific to this table; adjust as needed
df = pd.DataFrame(data[1:], columns=data[0])  # Use the first row as headers
df.to_csv('output.csv', index=False)

print('Data has been successfully written to output.csv')
#to read the csv file
import pandas as pd

# Read the CSV file
df = pd.read_csv('output.csv')

# Display the contents of the DataFrame
print(df)


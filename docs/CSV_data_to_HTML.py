import pandas as pd

# Get data from the CSV
df = pd.read_csv('Resources/cities.csv')

# Send data to html table
df.to_html('data_table.html', index=False)
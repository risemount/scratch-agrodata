from good_objects import ROC_year, afa_scratch, crops, items
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import time
import numpy as np

# Assuming you have lists of parameters that correspond by index
ROC_years = [ROC_year(y) for y in range(1997, 2023)]

# Use zip to iterate over matched elements
for year, item, crop in itertools.product(ROC_years, items.keys(), crops.keys()):

    response = afa_scratch(year, items[item], crops[crop])

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'lxml')

    # Find the table
    div = soup.find('div', class_='DivRestTbl')

    rows = div.find('table', class_= "TDFont")

    # Extract rows
    rows = rows.find_all('tr')
    # Process each row to extract column data
    data = []
    for row in rows:
        cols = [ele.text.strip() for ele in row.find_all('td')]
        if cols:  # Avoid empty lists from empty rows
            cols = [col.replace(",", "") for col in cols]
            data.append(cols)

    # Create a DataFrame with the extracted data
    # First row of data contains the headers
    if not ['查無資料！！'] in data:
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_csv(f"./response/{crop}_{year}_{item}.csv", index = False, encoding = 'big5')
    else:
        print(f"{(year, item, crop)} not found.")
        next

    time.sleep(np.round(np.random.normal(0.5, 0.03), 3))
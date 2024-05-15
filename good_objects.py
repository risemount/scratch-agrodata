import requests

def ROC_year(year):
    if year < 1912:
        raise ValueError("ROC year start from 1912 !")
    else:
        return int(year - 1911)

crops= {
    'Maize': '002',
    'Wheat': '003',
    'Soybean': '101',
    'Tomato': '425',
    'Sugarcane': '306',
    'Taro': '440',
    'Cabbage': '419'
}

items = {
    'winter': '00',
    'first_season': '01',
    'second_seanson': '02',
    'whole_year': '03'
}

def afa_scratch(year: int, item: str, crop: str, url: str = 'https://agr.afa.gov.tw/afa/pgcropcity.jsp'):
    if not 86 <= year <= 111:
        raise ValueError("Invalid year data")

    # Request data
    payload = {
        'accountingyear': "{:03.0f}".format(year),
        'item': item,
        'corn001': '',
        'input803': '',
        'crop': crop,
        'city': '00',
        'btnSend': '送　出'
    }

    try:
        # POST request
        response = requests.post(url, data = payload)

        # Check the responses
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)
        print('Success')  # Outputs the response text directly

        # Return response
        return response
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)



from bs4 import BeautifulSoup
import requests
import json

html_text = requests.get("https://www.kijiji.ca/b-real-estate/barrie/c34l1700006").text
soup = BeautifulSoup(html_text, 'html.parser')

listings = soup.find_all('div', class_='clearfix')

data = []
for listing in listings:
    listing_title_element = listing.find('div', class_='title')
    if listing_title_element is not None:
        listing_title = listing_title_element.text.strip().replace('N/A','Data unavailable for this post')
    else:
        listing_title = 'N/A'
    listing_rent_element = listing.find('div', class_='price')
    if listing_rent_element is not None:
        listing_rent = listing_rent_element.text.strip().replace('\n','').replace('\t','').replace('N/A','Data unavailable for this post')
    else:
        listing_rent = 'N/A'
    listing_town_element = listing.find_next_sibling('span')
    if listing_town_element is not None:
        listing_town = listing_town_element.text.strip().replace('N/A','Data unavailable for this post')
    else:
        listing_town = 'Barrie'
    listing_description_element = listing.find('div', class_='description')
    if listing_description_element is not None:
        listing_description = listing_description_element.text.strip().replace('N/A','Data unavailable for this post')
        listing_description = ' '.join(listing_description.split())
    else:
        listing_description = 'N/A'
    listing_street_element = listing.find('span', class_='intersection')
    if listing_street_element is not None:
        listing_street = listing_street_element.text.strip().replace('N/A','Data unavailable for this post')
    else:
        listing_street = 'N/A'
    listing_unit_size_element = listing.find('span', class_='bedrooms')
    if listing_unit_size_element is not None:
        listing_unit_size = listing_unit_size_element.text.strip().replace(' ','').replace('\n','')
    else:
        listing_unit_size = 'N/A'

    data.append({'title': listing_title, 'rent_amount': listing_rent, 'town': listing_town, 'description': listing_description, 'street_name': listing_street, 'unit_size': listing_unit_size})

json_data = json.dumps(data)
with open('data.json', 'w') as f:
    f.write(json_data)

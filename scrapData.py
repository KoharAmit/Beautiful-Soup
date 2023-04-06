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
    listing_price_element = listing.find('div', class_='price')
    if listing_price_element is not None:
        listing_price = listing_price_element.text.strip().replace('\n','').replace('\t','').replace('N/A','Data unavailable for this post')
    else:
        listing_price = 'N/A'
    listing_location_element = listing.find_next_sibling('span')
    if listing_location_element is not None:
        listing_location = listing_location_element.text.strip().replace('N/A','Data unavailable for this post')
    else:
        listing_location = 'Barrie'
    listing_time_element = listing.find('span', class_='date-posted')
    if listing_time_element is not None:
        listing_time = listing_time_element.text.strip().replace('<','about ')
    else:
        listing_time = 'N/A'
    listing_description_element = listing.find('div', class_='description')
    if listing_description_element is not None:
        listing_description = listing_description_element.text.strip().replace('N/A','Data unavailable for this post')
        listing_description = ' '.join(listing_description.split())
    else:
        listing_description = 'N/A'
    listing_intersection_element = listing.find('span', class_='intersection')
    if listing_intersection_element is not None:
        listing_intersection = listing_intersection_element.text.strip().replace('N/A','Data unavailable for this post')
    else:
        listing_intersection = 'N/A'
    listing_bedroom_element = listing.find('span', class_='bedrooms')
    if listing_bedroom_element is not None:
        listing_bedroom = listing_bedroom_element.text.strip().replace(' ','').replace('\n','')
    else:
        listing_bedroom = 'N/A'

    data.append({'title': listing_title, 'price': listing_price, 'location': listing_location, 'time': listing_time, 'description': listing_description, 'intersection': listing_intersection, 'bedroom': listing_bedroom})

json_data = json.dumps(data)
with open('data.json', 'w') as f:
    f.write(json_data)

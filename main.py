from bs4 import BeautifulSoup
import requests
from csv import writer

html_text=requests.get("https://www.kijiji.ca/b-real-estate/barrie/c34l1700006").text
soup = BeautifulSoup(html_text, 'html.parser')


listings = soup.find_all('div', class_='clearfix')

with open('kijiji_listing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title','Price','Location','Description','Time','Intersection','Rooms']
    thewriter.writerow(header)


    for listing in listings:
        listing_title_element = listing.find('div', class_='title')
        if listing_title_element is not None:
            listing_title = listing_title_element.text.replace('N/A','Data unavailable for this post' )
        else:
            listing_title = 'N/A'
        listing_price_element = listing.find('div', class_='price')
        if listing_price_element is not None:
            listing_price = listing_price_element.text.replace('N/A','Data unavailable for this post' )
        else:
            listing_price = 'N/A'
        listing_location_element = listing.find_next_sibling('span')
        if listing_location_element is not None:
            listing_location = listing_location_element.text.replace('N/A','Data unavailable for this post' )
        else:
            listing_location = 'Barrie'
        listing_time_element = listing.find('span', class_='date-posted')
        if listing_time_element is not None:
            listing_time = listing_time_element.text.replace('<','about ' )
        else:
            listing_time = 'N/A'
        listing_description_element = listing.find('div', class_='description')
        if listing_description_element is not None:
            listing_description = listing_description_element.text.replace('N/A','Data unavailable for this post' )
        else:
            listing_description = 'N/A'
        listing_intersection_element = listing.find('span', class_='intersection')
        if listing_intersection_element is not None:
            listing_intersection = listing_intersection_element.text.replace('N/A','Data unavailable for this post' )
        else:
            listing_intersection = 'N/A'
        listing_bedroom_element = listing.find('span', class_='bedrooms')
        if listing_bedroom_element is not None:
            listing_bedroom = listing_bedroom_element.text.replace(' ','')
        else:
            listing_bedroom = 'N/A'


        data=[listing_title,listing_price,listing_location,listing_description,listing_time,listing_intersection,listing_bedroom]
        thewriter.writerow(data)



from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import streamlit as st


from youtubesearchpython import *


allVideoLinks = []


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)




htp="https://raw.githubusercontent.com/cctij69/F1_highlights/main/F1%20logo.png" 
st.image(htp, width=350)



def getAllRaces():

    # URL of the website to scrape
    url = 'https://gpracingstats.com/seasons/2023-world-championship/'

    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the calendar data
    table = soup.find('table', {'class': 'summary calendar'})

    # Find all the rows in the table except the first one (header row)
    rows = table.find_all('tr')[1:]

    # Create an empty dictionary to store the calendar data
    calendar_data = {}

    # Loop through each row and extract the race number, name, and date
    for row in rows:
        cells = row.find_all('td')
        race_number = cells[0].text.strip()
        grand_prix_name = cells[1].text.strip()
        date_str = cells[3].text.strip()

        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%d %B')

        # Add the year to the date object
        date_obj = date_obj.replace(year=datetime.today().year)


        # Calculate the difference between the date from the website and today's date
        date_diff = date_obj - datetime.today()

        # If the date is within 4 days of today or has already passed, add it to the dictionary
        if date_diff <= timedelta(days=4):
            calendar_data[race_number] = (grand_prix_name, date_str)

    for race_number, (grand_prix_name, date_str) in reversed(calendar_data.items()):
        button = st.button(f"Race {race_number}: {grand_prix_name}", key=race_number)
        if button:
            # Call a function and pass the grand_prix_name
        
# Print the calendar data dictionary
#for item in calendar_data.values():
        #nameOfGP = list(item)
        #actualName = str(nameOfGP[0])
        #race_number = item
            actualName = grand_prix_name

            if actualName == "Saudi Arabia":
                actualName = "Saudi Arabian"
            elif actualName == "Australia":
                actualName = "Australian"

            FP1name = '"FP1 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP2name = '"FP2 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP3name = '"FP3 Highlights | 2023 ' + actualName + ' Grand Prix"'
            Quali = '"Qualifying Highlights | 2023 ' + actualName + ' Grand Prix"'
            PoleLap = 'Pole Lap | 2023 ' + actualName + ' Grand Prix | Pirelli'
            Race = '"Race Highlights | 2023 ' + actualName + ' Grand Prix"'


            print(Race)

            YTsearch2(FP1name)
            YTsearch2(FP2name)
            YTsearch2(FP3name)
            YTsearch2(Quali)
            YTsearch2(PoleLap)
            YTsearch2(Race)




def YTsearch2(search_keyword):
    #search = CustomSearch(search_keyword, VideoUploadDateFilter.thisWeek, limit = 1)
    search = CustomSearch(search_keyword, VideoUploadDateFilter.thisYear, limit = 1)
    for video in search.result()['result']:
        title = video['title']

        if "Pole" in title:
            lineToPrint = "Pole lap video - " + video['link']
            allVideoLinks.append(lineToPrint)
        else:
            if search_keyword == '"'+title+'"':
                lineToPrint = title + " - " + video['link']
                allVideoLinks.append(lineToPrint)
                #return video['link']






getAllRaces()

for item in allVideoLinks:
    st.write(item)



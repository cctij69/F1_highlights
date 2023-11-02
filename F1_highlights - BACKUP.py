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




gp_schedule = {
    1: {'Grand Prix': 'Bahrain', 'Circuit': 'Sakhir', 'Date': '05 March'},
    2: {'Grand Prix': 'Saudi Arabian', 'Circuit': 'Jeddah', 'Date': '19 March'},
    3: {'Grand Prix': 'Australian', 'Circuit': 'Melbourne', 'Date': '02 April'},
    4: {'Grand Prix': 'Azerbaijan', 'Circuit': 'Baku', 'Date': '30 April'},
    5: {'Grand Prix': 'Miami', 'Circuit': 'Florida', 'Date': '07 May'},
    6: {'Grand Prix': 'Emilia Romagna', 'Circuit': 'Imola', 'Date': '21 May'},
    7: {'Grand Prix': 'Monaco', 'Circuit': 'Monte Carlo', 'Date': '28 May'},
    8: {'Grand Prix': 'Spain', 'Circuit': 'Catalunya', 'Date': '04 June'},
    9: {'Grand Prix': 'Canadian', 'Circuit': 'Montreal', 'Date': '18 June'},
    10: {'Grand Prix': 'Austrian', 'Circuit': 'Spielberg', 'Date': '02 July'},
    11: {'Grand Prix': 'British', 'Circuit': 'Silverstone', 'Date': '09 July'},
    12: {'Grand Prix': 'Hungary', 'Circuit': 'Hungaroring', 'Date': '23 July'},
    13: {'Grand Prix': 'Belgium', 'Circuit': 'Spa-Francorchamps', 'Date': '30 July'},
    14: {'Grand Prix': 'Netherlands', 'Circuit': 'Zandvoort', 'Date': '27 August'},
    15: {'Grand Prix': 'Italian', 'Circuit': 'Monza', 'Date': '03 September'},
    16: {'Grand Prix': 'Singapore', 'Circuit': 'Marina Bay', 'Date': '17 September'},
    17: {'Grand Prix': 'Japan', 'Circuit': 'Suzuka', 'Date': '24 September'},
    18: {'Grand Prix': 'Qatar', 'Circuit': 'Losail', 'Date': '08 October'},
    19: {'Grand Prix': 'USA', 'Circuit': 'Austin', 'Date': '22 October'},
    20: {'Grand Prix': 'Mexican', 'Circuit': 'Mexico City', 'Date': '29 October'},
    21: {'Grand Prix': 'Sao Paulo', 'Circuit': 'Interlagos', 'Date': '05 November'},
    22: {'Grand Prix': 'Las Vegas', 'Circuit': 'Las Vegas', 'Date': '18 November'},
    23: {'Grand Prix': 'Abu Dhabi', 'Circuit': 'Yas Marina', 'Date': '26 November'}
}



















def getAllRacesBACKUP():

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

            actualName = grand_prix_name



            FP1name = '"FP1 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP2name = '"FP2 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP3name = '"FP3 Highlights | 2023 ' + actualName + ' Grand Prix"'
            Quali = '"Qualifying Highlights | 2023 ' + actualName + ' Grand Prix"'
            PoleLap = '"Pole Lap | 2023 ' + actualName + ' Grand Prix | Pirelli"'
            Race = '"Race Highlights | 2023 ' + actualName + ' Grand Prix"'


            print(Race)

            YTsearch2(FP1name)
            YTsearch2(FP2name)
            YTsearch2(FP3name)
            test = YTsearch2(Quali)
            if test == None:
                Quali = Quali.replace('"',"")
                test = YTsearch2(Quali)
            if not YTsearch2(PoleLap):
                PoleLap = PoleLap.replace('"',"")
                YTsearch2(PoleLap)
            YTsearch2(Race)

def getAllRaces(gp_schedule):

    calendar_data = {}

    for race_number, gp_info in gp_schedule.items():
        grand_prix_name = gp_info['Grand Prix']
        date_str = gp_info['Date']


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
        

            actualName = grand_prix_name



            FP1name = '"FP1 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP2name = '"FP2 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP3name = '"FP3 Highlights | 2023 ' + actualName + ' Grand Prix"'
            Quali = '"Qualifying Highlights | 2023 ' + actualName + ' Grand Prix"'
            PoleLap = '"Pole Lap | 2023 ' + actualName + ' Grand Prix | Pirelli"'
            Race = '"Race Highlights | 2023 ' + actualName + ' Grand Prix"'



            YTsearch2(FP1name)
            YTsearch2(FP2name)
            YTsearch2(FP3name)
            test = YTsearch2(Quali)
            if test == None:
                Quali = Quali.replace('"',"")
                test = YTsearch2(Quali)
            if not YTsearch2(PoleLap):
                PoleLap = PoleLap.replace('"',"")
                YTsearch2(PoleLap)
            YTsearch2(Race)




def YTsearch2(search_keyword):
    search = CustomSearch(search_keyword, VideoUploadDateFilter.thisYear, limit = 1)
    for video in search.result()['result']:
        title = video['title']
        if '"' not in search_keyword:
            search_keyword = '"' + search_keyword + '"'




        if "Pole" in title:
            search_keyword = search_keyword.replace('"',"")
            if search_keyword in title:
                lineToPrint = "Pole lap video - " + video['link']
                allVideoLinks.append(lineToPrint)
                return lineToPrint
            else:
                return None
        else:
            if search_keyword == '"'+title+'"':
                lineToPrint = title + " - " + video['link']
                allVideoLinks.append(lineToPrint)
                return lineToPrint
            else:
                return None

            







getAllRaces(gp_schedule)

for item in allVideoLinks:
    st.write(item)



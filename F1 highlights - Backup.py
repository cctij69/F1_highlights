from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import streamlit as st


import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import json

from youtubesearchpython import *


allVideoLinks = []


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

    for race_number, (grand_prix_name, date_str) in calendar_data.items():
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

            FP1name = '"FP1 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP2name = '"FP2 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP3name = '"FP3 Highlights | 2023 ' + actualName + ' Grand Prix"'
            Quali = '"Qualifying Highlights | 2023 ' + actualName + ' Grand Prix"'
            PoleLap = 'Pole Lap | 2023 ' + actualName + ' Grand Prix | Pirelli'
            Race = '"Race Highlights | 2023 ' + actualName + ' Grand Prix"'




            YTsearch2(FP1name)
            YTsearch2(FP2name)
            YTsearch2(FP3name)
            YTsearch2(Quali)
            YTsearch2(PoleLap)
            YTsearch2(Race)




def YTsearch(GPName):


    # Set the API credentials (you'll need to create a project and enable the YouTube API to get these)
    creds = json.load(open('credentials.json'))
    api_key = "AIzaSyA7yiYIC1R08c6btaT0G7hYSNQQnxeMrUY"

    # Set the YouTube API service
    youtube = build('youtube', 'v3', developerKey=api_key, cache_discovery=False)

    # Set the ID of the YouTube channel to search in
    channel_id = 'UCB_qr75-ydFVKSF9Dmo6izg'

    # Set the query to search for in the video titles
    query = GPName

    # Set the maximum number of videos to retrieve
    max_results = 1

    # Search for videos in the channel with the given query
    try:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            q=query,
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        videos = []
        for item in response['items']:
            video_id = item['id']['videoId']
            videos.append({
                'title': item['snippet']['title'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
                #'video_id': item['id']['videoId'],
                #'published_at': item['snippet']['publishedAt'],
                'video_link': f'https://www.youtube.com/watch?v={video_id}'
            })
        for race in videos:
            if "Pole" in race['title']:
                print (race['title'] + " - " + race['video_link'])
            else:
                print (query)
                print (race['title'])
                if query == race['title']:
                    print (race['title'] + " - " + race['video_link'])
                
            

        #print(videos)
        #st.write()
    except HttpError as error:
        print(f'An HTTP error {error.resp.status} occurred:\n{error.content}')







def YTsearch2(search_keyword):
    #search = CustomSearch(search_keyword, VideoUploadDateFilter.thisWeek, limit = 1)
    search = CustomSearch(search_keyword, VideoUploadDateFilter.thisYear, limit = 1)
    for video in search.result()['result']:
        title = video['title']

        if "Pole" in title:
            lineToPrint = title + " - " + video['link']
            allVideoLinks.append(lineToPrint)
        else:
            if search_keyword == '"'+title+'"':
                lineToPrint = title + " - " + video['link']
                allVideoLinks.append(lineToPrint)
                #return video['link']






getAllRaces()
#YTsearch()

for item in allVideoLinks:
    st.write(item)



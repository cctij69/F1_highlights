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
    1: {'Grand Prix': 'Bahrain', 'Circuit': 'Sakhir', 'Date': '05 March', 'Sprint': 'No'},
    2: {'Grand Prix': 'Saudi Arabian', 'Circuit': 'Jeddah', 'Date': '19 March', 'Sprint': 'No'},
    3: {'Grand Prix': 'Australian', 'Circuit': 'Melbourne', 'Date': '02 April', 'Sprint': 'No'},
    4: {'Grand Prix': 'Azerbaijan', 'Circuit': 'Baku', 'Date': '30 April', 'Sprint': 'Yes'},
    5: {'Grand Prix': 'Miami', 'Circuit': 'Florida', 'Date': '07 May', 'Sprint': 'No'},
    6: {'Grand Prix': 'Emilia Romagna', 'Circuit': 'Imola', 'Date': '21 May', 'Sprint': 'No'},
    7: {'Grand Prix': 'Monaco', 'Circuit': 'Monte Carlo', 'Date': '28 May', 'Sprint': 'No'},
    8: {'Grand Prix': 'Spanish', 'Circuit': 'Catalunya', 'Date': '04 June', 'Sprint': 'No'},
    9: {'Grand Prix': 'Canadian', 'Circuit': 'Montreal', 'Date': '18 June', 'Sprint': 'No'},
    10: {'Grand Prix': 'Austrian', 'Circuit': 'Spielberg', 'Date': '02 July', 'Sprint': 'Yes'},
    11: {'Grand Prix': 'British', 'Circuit': 'Silverstone', 'Date': '09 July', 'Sprint': 'No'},
    12: {'Grand Prix': 'Hungarian', 'Circuit': 'Hungaroring', 'Date': '23 July', 'Sprint': 'No'},
    13: {'Grand Prix': 'Belgium', 'Circuit': 'Spa-Francorchamps', 'Date': '30 July', 'Sprint': 'Yes'},
    14: {'Grand Prix': 'Netherlands', 'Circuit': 'Zandvoort', 'Date': '27 August', 'Sprint': 'No'},
    15: {'Grand Prix': 'Italian', 'Circuit': 'Monza', 'Date': '03 September', 'Sprint': 'No'},
    16: {'Grand Prix': 'Singapore', 'Circuit': 'Marina Bay', 'Date': '17 September', 'Sprint': 'No'},
    17: {'Grand Prix': 'Japan', 'Circuit': 'Suzuka', 'Date': '24 September', 'Sprint': 'No'},
    18: {'Grand Prix': 'Qatar', 'Circuit': 'Losail', 'Date': '08 October', 'Sprint': 'Yes'},
    19: {'Grand Prix': 'USA', 'Circuit': 'Austin', 'Date': '22 October', 'Sprint': 'Yes'},
    20: {'Grand Prix': 'Mexican', 'Circuit': 'Mexico City', 'Date': '29 October', 'Sprint': 'No'},
    21: {'Grand Prix': 'Sao Paulo', 'Circuit': 'Interlagos', 'Date': '05 November', 'Sprint': 'Yes'},
    22: {'Grand Prix': 'Las Vegas', 'Circuit': 'Las Vegas', 'Date': '18 November', 'Sprint': 'No'},
    23: {'Grand Prix': 'Abu Dhabi', 'Circuit': 'Yas Marina', 'Date': '26 November', 'Sprint': 'No'}
}





def getAllRaces(gp_schedule):

    calendar_data = {}
    for race_number, gp_info in gp_schedule.items():
        grand_prix_name = gp_info['Grand Prix']
        date_str = gp_info['Date']
        sprint_check = (gp_info['Sprint'])
        

        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%d %B')

        # Add the year to the date object
        date_obj = date_obj.replace(year=datetime.today().year)


        # Calculate the difference between the date from the website and today's date
        date_diff = date_obj - datetime.today()

        # If the date is within 4 days of today or has already passed, add it to the dictionary
        if date_diff <= timedelta(days=4):
            calendar_data[race_number] = (grand_prix_name, date_str,sprint_check)

    for race_number, (grand_prix_name, date_str, sprint_check) in reversed(calendar_data.items()):
        button = st.button(f"Race {race_number}: {grand_prix_name}", key=race_number)
        if button:
        

            actualName = grand_prix_name



            FP1name = '"FP1 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP2name = '"FP2 Highlights | 2023 ' + actualName + ' Grand Prix"'
            FP3name = '"FP3 Highlights | 2023 ' + actualName + ' Grand Prix"'
            Quali = '"Qualifying Highlights | 2023 ' + actualName + ' Grand Prix"'
            PoleLap = '"Pole Lap | 2023 ' + actualName + ' Grand Prix | Pirelli"'
            SprintShootout = '"Sprint Shootout Highlights | 2023 ' + actualName + ' Grand Prix"'
            SprintShootoutPoleLap = '"Sprint Shootout Pole Lap | 2023 ' + actualName + ' Grand Prix"'
            Sprint = '"Sprint Highlights | 2023 ' + actualName + ' Grand Prix"'
            Race = '"Race Highlights | 2023 ' + actualName + ' Grand Prix"'


            if sprint_check == "No":
                raceStages = [FP1name,FP2name,FP3name,Quali,PoleLap,Race]
            else:
                raceStages = [FP1name,Quali,PoleLap,SprintShootout,SprintShootoutPoleLap,Sprint,Race]


            for stage in raceStages:
                if not YTsearch2(stage):
                    stage = stage.replace('"',"'")
                    if not YTsearch2(stage):    
                        stage = stage.replace("'","")
                        YTsearch2(stage)

            for item in allVideoLinks:
                st.write(item)
            








def YTsearch2(search_keyword):
    search = CustomSearch(search_keyword, VideoUploadDateFilter.thisYear, limit = 2)


    for video in search.result()['result']:
        title = video['title']

        search_keyword = search_keyword.replace('"',"")
        search_keyword = search_keyword.replace("'","")


        if "Pole" in title:
            if search_keyword in title:
                if "Shootout" in title:
                    lineToPrint = "Shootout pole lap video - " + video['link']
                    allVideoLinks.append(lineToPrint)
                    return lineToPrint
                else:
                    lineToPrint = "Qualifying pole lap video - " + video['link']
                    allVideoLinks.append(lineToPrint)
                    return lineToPrint
            else:
                pass
        else:
            if search_keyword == '"'+title+'"':
                lineToPrint = title + " - " + video['link']
                allVideoLinks.append(lineToPrint)
                return lineToPrint
            elif search_keyword == title:
                lineToPrint = title + " - " + video['link']
                allVideoLinks.append(lineToPrint)
                return lineToPrint 
            else:
                return None

            







getAllRaces(gp_schedule)

#for item in allVideoLinks:
#    st.write(item)



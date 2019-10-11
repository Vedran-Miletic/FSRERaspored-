import bs4
import requests
from datetime import datetime
from db.model import Termin, session

def parsiraj (studij):
    res = requests.get(studij.url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    divs = soup.select('.appointment > div.h4 > span')
    styles = soup.select('.appointment[style]')
    scripts = soup.select('script')
    lines = scripts[18].string.split("\n")
    appointments = {}
    for idx, line in enumerate(lines):
        #print(line)
        if line.startswith("FActivityArray") and "[\"id\"]" in line:
            id = line.replace(";", "").split(" = ")[1].replace("\"", "").replace("\r", "")

            startDateTime = lines[idx + 5].replace(";", "").split(" = ")[1].replace("\"", "").replace("\r", "")
            starTime1 = lines[idx + 5].replace(";", "").split(" = ")[1].replace("\"", "").replace("\r", "").split(',')[1].split(":")

            startTime=starTime1[0]+":"+starTime1[1]

            endDateTime = lines[idx + 4].replace(";", "").split(" = ")[1].replace("\"", "").replace("\r", "")
            endTime1 = lines[idx + 4].replace(";", "").split(" = ")[1].replace("\"", "").replace("\r", "").split(',')[1].split(":")
            endTime=endTime1[0]+":"+endTime1[1]
            startDateTime =  datetime.strptime(startDateTime, "%Y-%m-%d,%H:%M:%S").date()
            month=startDateTime.month;
            day=startDateTime.day;
            startDateTime2=str(day) +"."+str(month)
            endDateTime = datetime.strptime(endDateTime, "%Y-%m-%d,%H:%M:%S")



            appointments[id] = {
                'id': id,
                'date': startDateTime2,
                'duration': 1,
                'endDateTime': endTime,
                'startTime': startTime,
                'studiji.id': studij.godina
            }

    for id, div in enumerate(divs):
        style = {}
        for attr in styles[id]['style'].split(";"):
            if (len(attr.split(":")) == 2):
                key, value = attr.split(":")
                style[key] = value
        termin = Termin()
        appointment = appointments[divs[id]['id'].replace("_vertraulich", "")]
        termin.title = divs[id].text
        termin.date = appointment['date']
        termin.duration = appointment['duration']
        termin.startTime = appointment['startTime']
        termin.endTime = appointment['endDateTime']
        termin.studiji_id = studij.id
        session.add(termin)
        session.commit()
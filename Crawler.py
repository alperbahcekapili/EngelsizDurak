"""
Crawl the latest route information with the bus number

"""
import requests
from bs4 import BeautifulSoup


def crawlRoute(number: str):
    resp = requests.get(f"https://www.ego.gov.tr/hareketsaatleri?hat_no={number}&kalkis=&varis=")
    page = BeautifulSoup(resp.text)
    hareket_saatleri =  page.find_all("div", {"class": "hareket-saatleri"})[0].find_all("td")

    hatfaici = [] 
    ctesi = [] 
    pazar = []

    templist = []
    for time in hareket_saatleri:
        cols = [ele.text.strip() for ele in time]
        templist.append([ele.split()[0] for ele in cols if ele]) # Get rid of empty values
        # .replace("-","").strip()
    hatfaici = templist[0]
    ctesi = templist[1]
    pazar = templist[2]


    return (hatfaici, ctesi, pazar)

from datetime import datetime

def getClosestTime(routes):
    now = datetime.now()    
    daynum = now.strftime('%w')
    """
    0 -> pazar
    1-5 -> hici
    6- > ctesi
    """

    (hici, ctesi, pazar)  = routes
    now_hour_min = str(now.hour) + ":" +str(now.minute)
    diffs = []
    if daynum == 0:
        for time1 in pazar:
            diffs.append(getDiffBetweenHours(time1, now_hour_min))
    elif daynum == 6:
        for time1 in ctesi:
            diffs.append(getDiffBetweenHours(time1, now_hour_min))
    else:
        for time1 in hici:
            diffs.append(getDiffBetweenHours(time1, now_hour_min))
    mindif = min(diffs)
    # iki tane esit zaman olan olabilir mi ?

    if mindif > 50:
        return -1
    #servis disi demek
    else: 
        minsindex = diffs.index(mindif)
        if daynum == 0:
            return pazar[minsindex]
        elif daynum == 6:
            return ctesi[minsindex]
        else:
            return hici[minsindex]
    

def getDiffBetweenHours(time1, time2):
    [hour1, minute1] = time1.split(":")
    [hour2, minute2] = time2.split(":")

    return abs((int(hour1)*60+int(minute1)) - (int(hour2)*60+int(minute2)))

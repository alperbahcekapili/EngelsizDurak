from gtts import gTTS
import os

from Otobus import Otobus


templates = [None  for _ in range(2)]



def checkTextExists(text):

    key_values = []
    with open(os.path.join(os.getcwd(), "Voices", "keyvalues"), "r", encoding="utf-8") as f:
        key_values = f.readlines()

    latest_key = key_values[-1].strip()

    #increase this key if 
    for line in key_values[:-1]:
        key = line.split(",")[0]
        value = ",".join(line.split(",")[1:])
        if value.strip() == text:
            return (True, key)
    

    newkey = int(latest_key)+1


    
    key_values = key_values[:-1]
    key_values.append(f"{newkey},{text}\n")
    key_values.append( str(newkey))
    with open(os.path.join(os.getcwd(), "Voices", "keyvalues"), "w", encoding="utf-8") as f:
        f.writelines(key_values)

    return (False, newkey)


def play(key):
    from playsound import playsound

    playsound(f"{os.path.join(os.getcwd(), 'Voices', f'{key}.mp3')}")


def inform(text):
    ( exists, key ) = checkTextExists(text)
    mp3_path = os.path.join(os.getcwd(), "Voices", f"{key}.mp3")
    if not exists:
      
        myobj = gTTS(text=text, lang="tr", slow=False)
        myobj.save(mp3_path)
    
    play(key)
    return mp3_path



def generateText(state: int, cur_station_no ,bus:Otobus, time):
    #0:  kalkis, 1: servis disi

    buscode = bus.no
    cur_station_index = bus.duraklar["numaralar"].index(cur_station_no)
    if cur_station_index + 3 < len(bus.duraklar["numaralar"]):
        following_stations = bus.duraklar["isimler"][cur_station_index: cur_station_index+3]
    else:
        following_stations = bus.duraklar["isimler"][cur_station_index: ]
    

    template = ""
    print(time)
    if state == 0:
        if templates[state] == None: 
            # then retrieve kalkis template from file
            with open(os.path.join(os.getcwd(), "Templates", "kalkis"), "r", encoding="utf-8") as f:
                template = f.readline()
            template = template.split("X")
            templates[state] = template
        else:
            template = templates[state]            
        # duraklari ekle
        return str(buscode)  + " " +  template[1] + " " + time + " " + template[2] + ",".join(following_stations)



    else:
        if templates[state] == None: 
            # then retrieve kalkis template from file
            with open(os.path.join(os.getcwd(), "Templates", "servis_disi"), "r", encoding="utf-8") as f:
                template = f.readline()
            template = template.split("X")
            templates[state] = template            
        else:
            template = templates[state]            

        return template[0]

    
    



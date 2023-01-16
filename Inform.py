from gtts import gTTS
import os


templates = [None  for _ in range(2)]



def checkTextExists(text):

    key_values = []
    with open(os.path.join(os.getcwd(), "Voices", "keyvalues"), "r", encoding="utf-8") as f:
        key_values = f.readlines()

    latest_key = key_values[-1].strip()

    #increase this key if 
    for line in key_values[:-1]:
        [key, value] = line.split(",")
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
    os.system(f"start {os.path.join(os.getcwd(), 'Voices', f'{key}.mp3')}")


def inform(text):
    ( exists, key ) = checkTextExists(text)
    if not exists:
      
        myobj = gTTS(text=text, lang="tr", slow=False)
        myobj.save(os.path.join(os.getcwd(), "Voices", f"{key}.mp3"))
    
    play(key)



def generateText(state: int, buscode, time):
    #0:  kalkis, 1: servis disi
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

        return buscode  + " " +  template[1] + " " + time + " " + template[2]



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

    
    



"""

1.1- Read image from camera periodically(1 sec)
1.2- Read image from camera when a bus is expected(-5mins&+5mins)(0.5 sec)

2- Scan QR from image and validate bus code

3- Check buses latest information update if higher than 1hour update 

4- Anounce the route information/if not planned anounce this bus is not planned


Questions?

Do we need to store these informations in a database?   Future

* We may need to store the delays and update the system accordingly
* We may not need for MVP.  



We may need to detect the number plate for accurate authorization   Future


* Kod parçaları birleştirilecek
* Güvenlik kısımları çözülecek
* Sesli okuma kısmını daha güzel okuyacak bir teknoloji


"""



"""
1- qr
2- crawl
3- inform 
"""


import traceback
import threading
import time
from Crawler import crawlRoute, getClosestTime
from Inform import generateText, inform

from QR import getBusCode, readImageFromCamera


try:
    while True:
        
        
        time.sleep(1)
        # 1 saniye uyusun

        frame = readImageFromCamera()
        print("sa")
        buscode = getBusCode(frame)
        # qr okundu ve otobus kodu alindi

        if buscode == -1:
            continue

        print(buscode)

        (hici, ctesi, pazar) = crawlRoute(buscode)
        # guncel sefer saatleri alindi
        print(buscode)

        closest_time = getClosestTime((hici, ctesi, pazar))
        state = 1 if closest_time == -1 else 0
        print(buscode)

        generated_text = generateText(buscode=buscode, state=state, time = closest_time)
        inform(generated_text)
except Exception as e:
    print(traceback.format_exc())
    print("TODO: implement a error logging system")
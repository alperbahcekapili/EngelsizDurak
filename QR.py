import sklearn
import cv2

from Authorization import verifyQr

qcd = cv2.QRCodeDetector()
cam = cv2.VideoCapture("rtsp://admin:Pimser_123_@192.168.1.64:554/Streaming/Channels/1/")



# C:\\Users\\alper\\OneDrive\\Resimler\\EngelsizDurak\\qrsample.png



def readFromFile(file_path):
    return cv2.imread(filename=file_path)



def getBusCode(frame):
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(frame)
    
    # >1 qr or invalid qr, only 1 valid qr assumed
    if retval:
        for text in decoded_info:
            if verifyQr(text):
                return "".join(text.split("-")[1:])
    
    return -1



def readImageFromCamera():
    ret, frame = cam.read()
    return frame


def realtimeFromCam():
    vid = cam
    while(True):
        ret, frame = vid.read()

        retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(frame)

        try:
            img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)
        except:
            img = frame
            
        cv2.imshow("qr",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()

    cv2.destroyAllWindows()



# frame = readFromFile("C:\\Users\\alper\\OneDrive\\Resimler\\EngelsizDurak\\101.png")
# buscode = getBusCode(frame)
# print(buscode)





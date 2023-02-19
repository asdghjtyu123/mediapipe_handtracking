import cv2
import mediapipe as mp
import time
import pyfirmata

def map( x,  in_min,  in_max,  out_min,  out_max): 
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
time.sleep(2.0)
comport='COM5'
board=pyfirmata.Arduino(comport)

servoPin = board.get_pin('d:13:s')
servoPin2 = board.get_pin('d:12:s')
servoPin3 = board.get_pin('d:8:s')
mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands
tipIds=[4,8,12,16,20,0]
tipIds2=[8,12,16,20]
tipIds1=[5,9,13,17]
video=cv2.VideoCapture(0)

# servoPin3.write(100)
with mp_hand.Hands(min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while True:
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]
        
        if len(lmList)!=0:   
            servoPin2.write(0)
 
            x=map(lmList[tipIds[5]][1],0,400,0,130)
            print(x)

            servoPin.write(x)
            # print(lmList[tipIds[5]][2],"y")

            y=map(lmList[tipIds[5]][2],0,470,0,180)
            print(x,y)
            servoPin3.write(y)
            for ids in range(0,4):
                if lmList[tipIds1[ids]][2] < lmList[tipIds2[ids]][2]:
                    servoPin2.write(80)
        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if cv2.waitKey(5) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()


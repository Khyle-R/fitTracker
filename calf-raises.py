import cv2
import mediapipe as mp
import numpy as np
from playsound import playsound
from tkinter import *
import customtkinter
import tkinter

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

cap = cv2.VideoCapture(0)

# Curl counter variables
# counter = 0
# if counter == 0:
file1 = open('counter.txt', 'w')
file1.write('0')
file1.close()
customtkinter.set_appearance_mode("Dark")

#prepares the window
app = tkinter.Tk()
app.geometry("300x140")
app.configure(bg='#3c3c3c')
app.title('Enter count number')

#prints the current value of counter
# print(f"initial counter value: {counter}")

#declares value tkinter variable
value = tkinter.IntVar()
haveValue = tkinter.BooleanVar()

def getvalue():
    a = dialog.get()
    print(a)
    value.set(a)
    counter = value.get()
    file = open('counter.txt', 'w')
    file.write(a)
    file.close()
    print(f"counter after button press: {counter}")
    app.quit()
    

dialog = customtkinter.CTkEntry(master=app, width=200, placeholder_text = "Enter amount of counter")
dialog.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="SUBMIT", command=getvalue)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()

fileopen = open('counter.txt','r')
var = fileopen.readline()
if var.isspace() or var == '':
    quit()
else:
    counter = int(var)
fileopen.close()
if counter == 0:
    quit()
stage = None

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
            index = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]

            rknee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            rheel = [landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]
            rindex = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]

            # Calculate angle
            angle = calculate_angle(knee, heel, index)
            rangle = calculate_angle(rknee, rheel, rindex)
            
            # Visualize angle
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(heel, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
            cv2.putText(image, str(rangle), 
                           tuple(np.multiply(rheel, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
            
            
            # Curl counter logic
            if angle > 130 and rangle > 130:
                stage = "up"
            if angle < 120 and rangle < 120 and stage =='up':
                stage="down"
                counter -=1
                playsound('sounds/beep.wav')
                print(counter)
            if counter == 0:
                playsound('sounds/success.mp3')
                break
                       
        except:
            pass
        
        # Render curl counter
        # Setup status box
        cv2.rectangle(image, (0,0), (300,90), (245,117,16), -1)
        
        # Rep data
        cv2.putText(image, 'COUNTS', (15,20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Stage data
        cv2.putText(image, 'STATUS', (100,20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (100,80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Calf raises', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
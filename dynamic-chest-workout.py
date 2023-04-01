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
            
            # Get coordinates of the left arms doing the folding
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            # Calculate left angle
            left_angle = calculate_angle(shoulder, elbow, wrist)
        
            # Visualize left angle
            cv2.putText(image, str(left_angle), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            # Get coordinates of the right arms doing the folding
            rshoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            relbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            rwrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate left angle
            right_angle = calculate_angle(rshoulder, relbow, rwrist)
        
            # Visualize left angle
            cv2.putText(image, str(right_angle), 
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            #Track if the arms are above 90 degrees
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

            #calculate if the arms are up
            lift_left_angle = calculate_angle(left_elbow, left_shoulder, left_hip)
            lift_right_angle = calculate_angle(r_elbow, r_shoulder, r_hip)

            # Visualize angle
            cv2.putText(image, str(lift_left_angle), 
                           tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            cv2.putText(image, str(lift_right_angle), 
                           tuple(np.multiply(r_shoulder, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            #folding logic
            if (lift_left_angle > 50) and (lift_right_angle > 50):
                if (left_angle > 150) and (right_angle > 150):
                    stage="open"
                if (left_angle < 45) and (right_angle < 45) and (stage == "open"):
                    stage = "closed"
                    counter -= 1
                    playsound('sounds/beep.wav')
                    print(counter)
            if (counter == 0):
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
        
        cv2.imshow('Dynamic Chest Workout', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
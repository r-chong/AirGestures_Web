import cv2
import streamlit as st
import mediapipe as mp
import numpy as np
import uuid
import os
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Function to capture video from the webcam
def capture_video():
    # we need a placeholder so that streamlit doesn't keep adding an image to the bottom of the page, stopmotion style
    placeholder = st.empty()

    # videocapture object
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            
            frame = cv2.flip(frame, 1)

            #BGR 2 RGB
            
            #set flag
            image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            image.flags.writeable=False
            
            #detections
            results = hands.process(image)
            
            #set flag to true
            image.flags.writeable=True 
            
            #RGB 2 BGR
            image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            
            #detections
            print(results)
            
            #rendering results
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
                
            # cv2.imshow('Hand Tracking', image)
            placeholder.image(image, channels="BGR", use_column_width=True)
    
    # Release the VideoCapture object and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Main function
def main():
    # this is streamlit markdown styling
    # you can do st.markdown and just use markdown styles within the page (vs <p>)
    st.title("GangAcademy")
    st.markdown(("we making it out of the hood through our studies :sunglasses:"))
    
    st.write("This app captures video from your webcam and displays it as an image.")
    
    # capture video function
    capture_video()

# Run the main function
if __name__ == '__main__':
    main()
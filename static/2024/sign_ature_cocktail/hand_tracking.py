import cv2
import mediapipe as mp
import numpy as np
import joblib
import time
import os

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)  
mpDraw = mp.solutions.drawing_utils

# Load the saved ASL fingerspelling model
model = joblib.load('asl_fingerspelling_model.pkl')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Initialization of the sentence variables
left_hand_symbol = ""
last_left_hand_symbol = ""
sentence = ""
right_hand_status = "Nothing"
last_record_time = 0  # Time of the last recorded symbol
shaboom_detected = False
shaboom_time = 0

left_hand_points = []
right_hand_points = []

# Function to save the letter to a file
def append_letter_to_file(letter, filename):
    with open(filename, 'a') as file:
        file.write(letter)

# Function to delete the last saved letter from the file
def remove_last_letter_from_file(filename='saved_letters.txt'):
    with open(filename, 'r') as file:
        content = file.read()
    content = content[:-1]  # Remove the last character
    with open(filename, 'w') as file:
        file.write(content)

# Function to check if the hand is making an "OK" sign
def is_okay_sign(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    thumb_index_distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2 + (thumb_tip.z - index_tip.z) ** 2)

    # Ensure other fingers are extended
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    if (thumb_index_distance < 0.05 and
        middle_tip.y < landmarks[9].y and
        ring_tip.y < landmarks[13].y and
        pinky_tip.y < landmarks[17].y):
        return True
    return False

# Function to check if the hand is making a fist
def is_fist(landmarks):
    for idx in [8, 12, 16, 20]:  # Tips of index, middle, ring, and pinky fingers
        if landmarks[idx].y < landmarks[idx - 2].y:  # If the tip of the finger is above the PIP joint
            return False
    return True

# Function to check the SHABOOM condition
def check_shaboom_condition(left_landmarks, right_landmarks):
    left_thumb_tip = left_landmarks[4]
    left_index_tip = left_landmarks[8]
    right_thumb_tip = right_landmarks[4]
    right_index_tip = right_landmarks[8]

    index_distance = np.sqrt((right_index_tip.x - left_index_tip.x) ** 2 + 
                             (right_index_tip.y - left_index_tip.y) ** 2 + 
                             (right_index_tip.z - left_index_tip.z) ** 2)
    thumb_distance = np.sqrt((right_thumb_tip.x - left_thumb_tip.x) ** 2 + 
                             (right_thumb_tip.y - left_thumb_tip.y) ** 2 + 
                             (right_thumb_tip.z - left_thumb_tip.z) ** 2)

    return index_distance < 0.05 and thumb_distance < 0.05

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    current_time = time.time()  # Current time

    if results.multi_hand_landmarks:
        left_hand_landmarks = None
        right_hand_landmarks = None

        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_data_point = []
            landmarks = hand_landmarks.landmark
            for landmark in landmarks:
                min_x = min([landmark.x for landmark in landmarks])
                max_x = max([landmark.x for landmark in landmarks])
                min_y = min([landmark.y for landmark in landmarks])
                max_y = max([landmark.y for landmark in landmarks])

                # Width & Height of the Hand Bounding Box
                bbox_width = max_x - min_x
                bbox_height = max_y - min_y

                # Normalize x / y landmarks coordinates within the bounding box
                normalized_x = (landmark.x - min_x) / bbox_width
                normalized_y = (landmark.y - min_y) / bbox_height
                z = landmark.z
                hand_data_point.extend([normalized_x, normalized_y, z])

            hand_data_points = np.array(hand_data_point)
            hand_data_points = hand_data_points.reshape(1, -1)

            # Draw hand landmarks
            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
            handedness = results.multi_handedness[idx].classification[0].label
            hand_label = "Left" if handedness == "Left" else "Right"

            if hand_label == "Left":  # Only process left hand data for ASL symbols
                left_hand_landmarks = landmarks
                prediction = model.predict(hand_data_points)
                left_hand_symbol = prediction[0]
                left_hand_points.append(hand_data_point)

                if left_hand_symbol != last_left_hand_symbol:
                    append_letter_to_file(left_hand_symbol, 'current_letters.txt')
                    last_left_hand_symbol = left_hand_symbol
            else:  # Check gestures for the right hand
                right_hand_landmarks = landmarks
                if is_okay_sign(landmarks):
                    right_hand_status = "Okay Sign"
                    # Cooldown check before adding symbol to sentence
                    if current_time - last_record_time > 1:
                        if left_hand_symbol == "space":
                            left_hand_symbol = " "  # Replace "space" with a space character
                        sentence += left_hand_symbol
                        append_letter_to_file(left_hand_symbol, "saved_letters.txt")  # Append the letter to the file
                        last_record_time = current_time

                elif is_fist(landmarks):
                    right_hand_status = "Fist"
                    # Cooldown check before deleting the last symbol from the sentence
                    if current_time - last_record_time > 1:
                        if sentence:
                            sentence = sentence[:-1]
                            remove_last_letter_from_file()  # Remove the last letter from the file
                        last_record_time = current_time

                else:
                    right_hand_status = "Nothing"
                
                right_hand_points.append(hand_data_point)

        # Check for SHABOOM condition
        if left_hand_landmarks and right_hand_landmarks and check_shaboom_condition(left_hand_landmarks, right_hand_landmarks):
            shaboom_detected = True
            shaboom_time = time.time()

        if shaboom_detected and time.time() - shaboom_time <= 1:
            shaboom_text = "SHABOOM"
            (text_width, text_height), _ = cv2.getTextSize(shaboom_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            cv2.putText(frame, shaboom_text, ((frame.shape[1] - text_width) // 2, (frame.shape[0] + text_height) // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Save hand points to file
    with open('left_hand_points.txt', 'w') as left_file:
        for points in left_hand_points:
            left_file.write(','.join(map(str, points)) + '\n')

    with open('right_hand_points.txt', 'w') as right_file:
        for points in right_hand_points:
            right_file.write(','.join(map(str, points)) + '\n')

    # Display the current symbol for the left hand in the top-left corner
    font_scale = 1  # Adjust this based on your video size
    thickness = 2  # Adjust this based on your preference
    color = (0, 0, 255)  # Color RED
    cv2.putText(frame, f"Left Hand: {left_hand_symbol}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    # Display the status of the right hand in the top-right corner
    text = f"Right Hand: {right_hand_status}"
    (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    cv2.putText(frame, text, (frame.shape[1] - text_width - 10, 40), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    # Display the sentence on the video frame
    (text_width, text_height), _ = cv2.getTextSize(sentence, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    x = (frame.shape[1] - text_width) // 2
    y = int(frame.shape[0] - 50)  # Adjust the Y position as needed
    cv2.putText(frame, sentence, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    # Show the video frame
    cv2.imshow('ASL Interpreter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

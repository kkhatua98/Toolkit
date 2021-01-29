# importing the required packages 
import pyautogui 
import cv2 
import numpy as np
import os
from PIL import Image  # Will need to make sure PIL is installed
import mss


os.chdir("C:\\Users\\kkhatua\\Desktop\\Toolkit\\Captures\\Videos")

# Specify resolution 
resolution = (1920, 1080) 

# Specify video codec 
codec = cv2.VideoWriter_fourcc(*"XVID")

filename = input("Give File Name\n")
# Specify name of Output file 
#filename = "Recording.avi"
filename = filename + ".avi"

# Specify frames rate. We can choose any 
# value and experiment with it 
fps = 30.0

monitor = int(input("Which monitor to capture 1 or 2?\n"))


# Creating a VideoWriter object 
out = cv2.VideoWriter(filename, codec, fps, resolution) 

# Create an Empty window 
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 

# Resize this window 
cv2.resizeWindow("Live", 480, 270)



with mss.mss() as mss_instance:
    monitor_1 = mss_instance.monitors[monitor]

    while True:
        screenshot = mss_instance.grab(monitor_1)

        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write it to the output file
        out.write(frame)

        # Optional: Display the recording screen
        cv2.imshow('Live', frame)

        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            # Release the Video writer
            out.release()

            # Destroy all windows
            cv2.destroyAllWindows()

            break




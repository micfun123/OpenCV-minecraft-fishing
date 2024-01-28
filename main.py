import cv2
import numpy as np
import pyautogui
import time
import keyboard
import os

# Function to find the fishing bobber using OpenCV
def find_bobber(templates, screenshot_path):
    screenshot = cv2.imread(screenshot_path, 0)

    best_match = None
    best_loc = None
    best_val = -1

    for template in templates:
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > best_val:
            best_val = max_val
            best_loc = max_loc
            best_match = template

    threshold = 0.7  # 1 is the best match, 0 is the worst match

    if best_val > threshold:
        return best_loc, best_match
    else:
        return None, None


# Paths to the template images of the fishing bobber
templates_paths = os.listdir('templates')
templates_paths = ['templates/' + path for path in templates_paths]
print(templates_paths)
# Load the templates
templates = [cv2.imread(path, 0) for path in templates_paths]

# Main loop for fishing automation
while True:
    # Capture screenshot asynchronously (non-blocking)
    screenshot_path = 'screenshot.png'  # Take a screenshot of the Minecraft window
    # Assuming x, y, width, and height are the coordinates and dimensions of the region
    pyautogui.screenshot(screenshot_path, region=(400, 100, 900, 600))


    # Find the bobber
    bobber_location, best_match = find_bobber(templates, screenshot_path)

    if bobber_location:
        # Perform actions when the bobber is found
        x, y = bobber_location
    else:
        # Right click
        pyautogui.click(button='right')
        time.sleep(0.1)  # Adjust this delay if necessary
        pyautogui.click(button='right')
        time.sleep(0.7)  # Adjust this delay if necessary

    # Press 's' to quit the program
    if keyboard.is_pressed('s'):
        break

    # Adjust the delay based on your game settings
    time.sleep(0.2)  # Adjust this delay if necessary

# OpenCV Minecraft Fishing Bot

This project automates the fishing process in Minecraft using OpenCV for image recognition. The bot identifies the bobber on-screen and reacts when it detects changes (such as the bobber sinking), which usually indicates a fish has been caught.

## Features

- Detects Minecraft fishing bobber using OpenCV template matching.
- Automates the fishing rod cast and catch process based on visual cues.
- Flexible template matching allows for different bobber appearances.

## Requirements

Make sure you have the following installed:

- Python 3.x
- requirements (`pip install -r requirements.txt`)
- A screenshot tool for capturing and cropping the bobber

## Usage

### Step 1: Prepare Bobber Images

1. Take screenshots of your Minecraft fishing bobber in various states (normal floating and possibly while sinking if needed). Try to capture it with different backgrounds or lighting conditions for better accuracy.
2. Crop these screenshots to just the bobber and the background block it's floating over.
3. Save these cropped images inside the `templates/` folder of the project.

### Step 2: Setup

1. Cast your fishing rod in Minecraft and make sure the bobber is visible on screen.
2. Ensure the game window is in focus and running in a resolution where the bot can easily detect the bobber.
3. Run the Python script: `python3.9 main.py`
4. Tweek the region in the while loop to match where your bobber is landing

### Step 3: Tweaking for Accuracy

You may need to adjust the sensitivity of the template matching or threshold settings in the script for better performance, depending on your Minecraft setup (resolution, texture packs, etc.).
If the bot fails to detect the bobber, try adding more template images to the templates/ folder to cover a wider range of scenarios (e.g., different times of day, weather, or background blocks).

### How it Works

Template Matching: OpenCV's matchTemplate function is used to scan the screen and compare it with the bobber images you provided in the templates/ folder.
Detection: The script repeatedly checks for the bobber’s presence. When the bobber disappears or sinks (i.e., the template no longer matches), the bot simulates a mouse click to reel in the catch.
Automation: PyAutoGUI is used to automate mouse clicks or other input commands to cast and reel in the fishing rod.

### Troubleshooting

False Positives: If the bot clicks too early or too late, try improving the template images or adjusting the match threshold in the script.


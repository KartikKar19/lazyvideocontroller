# lazyvideocontroller
lazy video controller which uses my webcam feed to detect hand gestures in real time and based on the number of fingers raised stimulates specific keyboard keys using python libraries. 
lazyvideocontroller is a hand gesture recognition system that uses your webcam feed to detect hand gestures in real-time. Based on the number of fingers raised, the system simulates specific keyboard actions, like arrow keys or the spacebar, using Python libraries. This project utilizes machine learning and computer vision to make gesture-based interaction possible with minimal setup.

Features
Real-Time Gesture Recognition: Detects hand gestures and counts the number of fingers raised.
Keyboard Simulation: Maps each gesture (based on the number of fingers) to a specific keyboard key (e.g., arrow keys, spacebar).
Easy Setup: Requires only a webcam and Python libraries to get started.
Requirements
Before running the project, make sure you have the following installed:

Python 3.x: Download Python
Required Python Libraries:
OpenCV: A library for computer vision tasks.
Install using: pip install opencv-python
MediaPipe: A framework for machine learning-based hand tracking.
Install using: pip install mediapipe
PyAutoGUI: A library that simulates keyboard and mouse events.
Install using: pip install pyautogui
time: This is part of the Python standard library for handling time-based events.
To install all dependencies at once, you can use the provided requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
Installation
Clone the repository to your local machine:
bash
Copy
Edit
git clone https://github.com/KartikKar19/lazyvideocontroller.git
cd lazyvideocontroller
Install the necessary libraries:
bash
Copy
Edit
pip install -r requirements.txt
Run the script:
bash
Copy
Edit
python lazy.py
Usage
Once you run the script, your webcam feed will be activated, and the system will start detecting hand gestures. Based on the number of fingers raised, the following actions will occur:

1 finger: Simulates the "right" arrow key press.
2 fingers: Simulates the "left" arrow key press.
3 fingers: Simulates the "up" arrow key press.
4 fingers: Simulates the "down" arrow key press.
5 fingers: Simulates the "space" key press.
Example
To run the script and see the gesture recognition in action:

bash
Copy
Edit
python lazy.py
You should see a webcam window pop up, and when you raise the specified number of fingers, the corresponding keyboard action will be triggered.

Contributing
Feel free to fork the repository, submit issues, or make pull requests. Contributions are always welcome!

License
This project is open-source and available under the MIT License.

Links
OpenCV: https://opencv.org/
MediaPipe: https://mediapipe.dev/
PyAutoGUI: https://pyautogui.readthedocs.io/

from ev3dev2.motor import OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
import time
import threading

# Initialize the touch sensors
touch_left = TouchSensor(INPUT_1)  # Adjust if connected to a different port
touch_right = TouchSensor(INPUT_4)  # Adjust if connected to a different port

# Initialize the sound module
sound = Sound()

# Print that the script is running
print("Script is running...")

# Flag to control the running state of the script
running = True

# Function to check sensor input
def check_sensors():
    global running
    while running:
        if touch_left.is_pressed or touch_right.is_pressed:
            sound.speak("ouch whats your problem")
            time.sleep(0.5)  # Small delay to avoid multiple rapid triggers

# Function to listen for 'exit' command
def listen_for_exit():
    global running
    while running:
        command = input()
        if command.lower() == 'exit':
            running = False
            print("Exiting script...")

# Start the sensor checking and exit listening in separate threads
sensor_thread = threading.Thread(target=check_sensors)
exit_thread = threading.Thread(target=listen_for_exit)

sensor_thread.start()
exit_thread.start()

sensor_thread.join()
exit_thread.join()

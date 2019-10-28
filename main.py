from inputs import devices
from inputs import GamePad
from inputs import get_gamepad
import pyscreenshot as ImageGrab
import time
import pygetwindow as gw
import re

counter = 0
game_pad = None

def record_game_pad():
    global counter

    steering_x_captured = None
    steering_y_captured = None
    throttle_captured = None
    brake_captured = None

    while steering_x_captured == None or steering_y_captured == None or (brake_captured == None and throttle_captured == None):
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_Z" and event.state != None and brake_captured == None:
                brake_captured = event.state
            if event.code == "ABS_RZ" and event.state != None and throttle_captured == None:
                throttle_captured = event.state
            if event.code == "ABS_X" and event.state != None and steering_x_captured == None:
                steering_x_captured = event.state
            if event.code == "ABS_Y" and event.state != None and steering_y_captured == None:
                steering_y_captured = event.state

    print("  - game-pad : OK")

    brake_captured = 0 if brake_captured == None else brake_captured
    throttle_captured = 0 if throttle_captured == None else throttle_captured

    file = open("data/" + str(counter) + "_inputs.txt", "w+")
    file.write("Steering: (x: " + str(steering_x_captured) + ", y: " + str(steering_y_captured) + ")\n")
    file.write("Pedals: (gas: " + str(throttle_captured) + ", brake: " + str(brake_captured) + ")")
    file.close()

def capture_screen(screen_top, screen_left, screen_width, screen_height):
    global counter

    box = (screen_top, screen_left, screen_top + screen_width, screen_left + screen_height)
    im = ImageGrab.grab(bbox=box)
    im.save('data/' + str(counter) + '_image.png')

    counter += 1
    print("  - screen : OK")

def tests_before_launch():
    global game_pad

    windows_list = gw.getWindowsWithTitle('Forza Horizon 4')
    if len(windows_list) == 0:
        exit("You need to launch Forza Horizon 4...")
    else:
        print("Forza Horizon 4 window detected.")
    
    for device in devices:
        if type(device) == GamePad and device != None:
            game_pad = device
            break
    
    if game_pad != None:
        print("Gamepad detected.")
    else:
        exit("You need to use a controller for now, sorry :(")
    
    print()

def run():
    forzaScreen = gw.getWindowsWithTitle('Forza Horizon 4')[0]
    forzaScreen.resizeTo(1024, 768)

    screen_top = forzaScreen.top
    screen_left = forzaScreen.left
    screen_width = forzaScreen.width
    screen_height = forzaScreen.height

    while True:
        print("[" + str(counter) + "] new capture")
        record_game_pad()
        capture_screen(screen_left + 27, screen_top + 33, screen_width - (27 * 2), screen_height - (33 * 2))
        time.sleep(1)

if __name__ == '__main__':
    tests_before_launch()

    counter = int(input("Last data index: "))

    print("Prepare to drive! Starting in 10 seconds.")
    time.sleep(10)
    run()
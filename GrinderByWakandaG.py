import pyautogui
import keyboard
import time
from pynput.mouse import Button, Controller
from pynput.mouse import Listener as MouseListener
from threading import Thread

mouse = Controller()
clicking = False
ws_loop_active = False


def on_click(x, y, button, pressed):
    global clicking
    if pressed:
        if button == Button.right:
            clicking = not clicking
            if clicking:
                print("Mouse clicking started.")
            else:
                print("Mouse clicking stopped.")


def mouse_click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(0.01)
        else:
            time.sleep(0.1)


def wasd_loop():
    global ws_loop_active
    try:
        while True:
            if ws_loop_active:
                keyboard.press('w')
                time.sleep(1 / 5)
                keyboard.release('w')
                time.sleep(0.1)

                keyboard.press('s')
                time.sleep(1 / 5)
                keyboard.release('s')
                time.sleep(0.1)
            else:
                time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")


def toggle_wasd_loop():
    global ws_loop_active
    ws_loop_active = not ws_loop_active
    if ws_loop_active:
        print("WASD loop started.")
    else:
        print("WASD loop stopped.")


if __name__ == "__main__":

    mouse_listener = MouseListener(on_click=on_click)
    mouse_listener.start()


    mouse_thread = Thread(target=mouse_click_loop)
    mouse_thread.daemon = True
    mouse_thread.start()


    wasd_thread = Thread(target=wasd_loop)
    wasd_thread.daemon = True
    wasd_thread.start()

    print("Press 'P' to start/stop the WASD loop. Press 'Q' to quit.")


    keyboard.add_hotkey('p', toggle_wasd_loop)

    keyboard.wait('q')
    print("Program terminated.")

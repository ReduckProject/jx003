from pynput import keyboard

def on_key_event(key):
    try:
        if key == keyboard.Key.esc:
            print("ESC key pressed. Exiting...")
            return False  # Returning False stops the listener
        else:
            print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

# Set up the listener
listener = keyboard.Listener(on_press=on_key_event)

# Start the listener
listener.start()

# Keep the script running
listener.join()
import threading
import time
import tkinter as tk
import playsound

# Create the Tkinter window
window = tk.Tk()
window.title("Audio Player")

# Create the canvas
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack()

# Initialize the color index to 0
color_index = 0

# Define a list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def play_audio():
    # Play the audio file in a separate thread
    thread = threading.Thread(target=playsound.playsound, args=('audio.mp3',))
    thread.start()

def update_canvas():
    # Update the canvas background color
    global color_index
    canvas.configure(bg=colors[color_index])

    # Increment the color index
    color_index = (color_index + 1) % len(colors)

    # Schedule the next update
    window.after(1000, update_canvas)

# Create the audio button
audio_button = tk.Button(window, text="Play audio", command=play_audio)
audio_button.pack()

# Start the canvas updates
update_canvas()

# Run the Tkinter event loop
window.mainloop()

import numpy as np  #pip install numpy
import sounddevice as sd #pip install sounddevice
import playsound #pip install playsound
#create sine wave
def sine(f,d):
    #f = frequency
    d = d/1000 #duration in milliseconds
    #w = wait
    fs = 44100
    t = np.arange(0,d,1/fs)
    y = np.sin(2*np.pi*f*t)
    sd.play(y,fs)
    sd.wait()
def square(f,d):
    #f = frequency
    d = d/1000 #duration in milliseconds
    #w = wait
    fs = 44100
    t = np.arange(0,d,1/fs)
    y = np.sign(np.sin(2*np.pi*f*t))
    sd.play(y,fs)
    sd.wait()

#death sound
sine(600, 200)
square(400, 200)
sine(50, 400)
#background music
playsound.playsound('lady-of-the-80x27s-128379.mp3')
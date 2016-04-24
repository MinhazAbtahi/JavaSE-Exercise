
import cv2
from Tkinter import *
from tkFont import *
from PIL import Image, ImageTk

# VideoCapture dimension
width = 400
height = 400

# Initializes VideoCapture
capture = cv2.VideoCapture(0)

# Sets VideoCapture Dimension
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Initiazlizes and sets GUI
root_window = Tk()
root_window.title('ROBOT MONITORING GUI')
root_window.minsize(width = 480, height = 320)
root_window.configure(background = 'black')

# Monitor frame
monitor_frame = Frame(root_window, width = 100, height = 200, bg = 'black')
monitor_frame.pack(side = LEFT, padx = 10)

# Video frame
video_frame = Frame(root_window, width = 500, height = 300, bg = 'black')
video_frame.pack(side = RIGHT)

# Frames title font
title_font = Font(family = 'consolas', size = 15, underline = True, weight = BOLD)

# Monitor title 
monitor_title_label = Label(monitor_frame, text = 'SENSOR DATA:', fg = 'green', bg = 'black')
monitor_title_label.pack(side = TOP, pady = 50)
monitor_title_label.configure(font = title_font)

# Temparature widgets
temparature_label = Label(monitor_frame, text = 'Temparature: ', fg = 'green', bg = 'black')
temparature_label.pack()
temparature_entry = Entry(monitor_frame, bd = 4)
temparature_entry.pack()

# Humidity widgets
humidity_label = Label(monitor_frame, text = 'Humidity: ', fg = 'green', bg = 'black')
humidity_label.pack()
humidity_entry = Entry(monitor_frame, bd = 4)
humidity_entry.pack()

# Smoke widgets
smoke_label = Label(monitor_frame, text = 'Smoke: ', fg = 'green', bg = 'black')
smoke_label.pack()
smoke_entry = Entry(monitor_frame, bd = 4)
smoke_entry.pack()

# Fire widgets
fire_label = Label(monitor_frame, text = 'Fire: ', fg = 'green', bg = 'black')
fire_label.pack()
fire_entry = Entry(monitor_frame, bd = 4)
fire_entry.pack()

# Video stream title
video_title_label = Label(video_frame, text = 'VIDEO STREAM:', fg = 'green', bg = 'black')
video_title_label.pack()
video_title_label.configure(font = title_font)

# Video stream label
video_label = Label(video_frame, bg = 'green')
video_label.pack()

def show_frame():
	# Captures frame by frame
	retval, frame = capture.read()
	
	# Gets captured image
	cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	pil_image = Image.fromarray(cv2_image)
	pil_imagetk = ImageTk.PhotoImage(image = pil_image)
	
	# Streams captured video frame by frame in video_label
	video_label.pil_imagetk = pil_imagetk
	video_label.configure(image = pil_imagetk)
	video_label.after(10, show_frame)

# Streams captured video	
show_frame()	
# root_window mainloop
root_window.mainloop()
# Realease VideoCapture
capture.release()
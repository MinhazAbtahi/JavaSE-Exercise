import cv2
from random import randrange
from Tkinter import *
from tkFont import *
from PIL import Image, ImageTk
import serial

# Arduino Serial Communication 
ser = serial.Serial('COM4', 9600)

# VideoCapture dimension
width = 500
height = 400

# Initializes VideoCapture
capture = cv2.VideoCapture(0)

# Sets VideoCapture Dimension
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Initiazlizes and sets GUI
root_window = Tk()
root_window.title('ROBOT MONITORING GUI')
root_window.minsize(width = 640, height = 500)
root_window.resizable(0,0)
root_window.configure(background = "gray5")

# Monitor frame
monitor_frame = Frame(root_window, width = 100, height = 400, bg = 'gray8')
monitor_frame.pack(side = LEFT, padx = 10)

# Video frame
video_frame = Frame(root_window, width = 540, height = 400, bg = 'gray9')
video_frame.pack(side = RIGHT, padx = 10 )

# Frames title font
title_font = Font(family = 'consolas', size = 15, underline = True, weight = BOLD)

# Navigation title 
monitor_title_label = Label(monitor_frame, text = 'ROBOT NAVIGATION:', fg = 'SpringGreen4', bg = 'gray5')
monitor_title_label.pack(side = TOP, pady = 20)
monitor_title_label.configure(font = title_font)

# Navigation Button
forward_button = Button(monitor_frame, text = 'FORWARD(W)', command= lambda: send_command('w'))
forward_button.pack()
backward_button = Button(monitor_frame, text = 'BACKWARD(S)', command= lambda: send_command('s'))
backward_button.pack()
right_button = Button(monitor_frame, text = 'RIGHT(D)', command= lambda: send_command('d'))
right_button.pack()
left_button = Button(monitor_frame, text = 'LEFT(A)', command= lambda: send_command('a'))
left_button.pack()
stop_button = Button(monitor_frame, text = 'STOP(X)', command= lambda: send_command('x'))
stop_button.pack()

# Navigation Button For Arm title 
monitor_title_label = Label(monitor_frame, text = 'ROBOTIC ARM NAVIGATION:', fg = 'SpringGreen4', bg = 'gray5')
monitor_title_label.pack(side = TOP, pady = 20)
monitor_title_label.configure(font = title_font)

#Navigation Button For Arm
arm_start_button = Button(monitor_frame, text = 'ARM START(K)', command= lambda: send_command('k'))
arm_start_button.pack()
base_forward_button = Button(monitor_frame, text = 'BASE FORWARD(B)', command= lambda: send_command('b'))
base_forward_button.pack()
base_backward_button = Button(monitor_frame, text = 'BASE BACKWARD(N)', command= lambda: send_command('n'))
base_backward_button.pack()
manipulator_forward_button = Button(monitor_frame, text = 'MANIPULATOR FORWARD(G)', command= lambda: send_command('g'))
manipulator_forward_button.pack()
manipulator_backward_button = Button(monitor_frame, text = 'MANIPULATOR BACKWARD(H)', command= lambda: send_command('h'))
manipulator_backward_button.pack()
gripper_open_button = Button(monitor_frame, text = 'GRIPPER OPEN(T)', command= lambda: send_command('t'))
gripper_open_button.pack()
gripper_close_button = Button(monitor_frame, text = 'GRIPPER CLOSE(Y)', command= lambda: send_command('y'))
gripper_close_button.pack()
arm_stop_button = Button(monitor_frame, text = 'ARM STOP(L)', command= lambda: send_command('l'))
arm_stop_button.pack()

# Video stream title
video_title_label = Label(video_frame, text = 'VIDEO STREAM:', fg = 'SpringGreen4', bg = 'gray5')
video_title_label.pack(side = TOP, pady = 20)
video_title_label.configure(font = title_font)

# Video stream label
video_label = Label(video_frame, bg = 'gray17')
video_label.pack()

# Monitor title 
monitor_title_label = Label(video_frame, text = 'SENSOR DATA:', fg = 'SpringGreen4', bg = 'gray5')
monitor_title_label.pack(side = TOP, pady = 20)
monitor_title_label.configure(font = title_font)

# Temparature widgets
temparature_label = Label(video_frame, text = 'TEMPARATURE: ', fg = 'PaleGreen3', bg = 'gray5')
temparature_label.pack(side=LEFT)
temparature_entry = Entry(video_frame, bd = 4)
temparature_entry.pack(side=LEFT, padx = 3)

# Humidity widgets
humidity_label = Label(video_frame, text = 'HUMIDITY: ', fg = 'PaleGreen3', bg = 'gray5')
humidity_label.pack(side=LEFT)
humidity_entry = Entry(video_frame, bd = 4)
humidity_entry.pack(side=LEFT)

# Smoke widgets
smoke_label = Label(video_frame, text = 'SMOKE: ', fg = 'PaleGreen3', bg = 'gray5')
smoke_label.pack(side=LEFT)
smoke_entry = Entry(video_frame, bd = 4)
smoke_entry.pack(side=LEFT, pady = 10)

# Button callback
def send_command(command):
	ser.flush()	# flush serial buffer
	ser.write(command) # writting to arduino serial
	print(str(command) + ' pressed!')
	
"""
# predefine data change
def temp_change():
	temp = randrange(27, 30)
	temparature_entry.delete(0, END)
	temparature_entry.insert(0,"                 "+ str(temp) + '*C')
	temparature_entry.after(1000, temp_change)

def humd_change():
	humd = randrange(93, 96)
	humidity_entry.delete(0, END)
	humidity_entry.insert(0,"                  "+ str(humd) + '%')
	humidity_entry.after(1000, humd_change)
	
def smoke_change():
	smoke = randrange(0, 50)
	smoke_entry.delete(0, END)
	smoke_entry.insert(0,"          "+ str(smoke) + '  normal<500')
	smoke_entry.after(1000, smoke_change)
"""
# Video streamer
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

# Main	
def main():
	# Streams captured video	
	show_frame()	
	#temp_change()
	#humd_change()
	#smoke_change()

	# Tkinter mainloop
	root_window.mainloop()
	# Realease VideoCapture
	capture.release()
	
if __name__ == '__main__':
	main()

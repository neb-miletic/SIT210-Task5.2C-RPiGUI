from tkinter import *
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

GPIO.output(16,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)

def blinky(value):
    
    if(value == 1):
      GPIO.output(16,GPIO.HIGH)
      GPIO.output(20,GPIO.LOW)
      GPIO.output(21,GPIO.LOW)
    elif(value == 2):
      GPIO.output(20,GPIO.HIGH)
      GPIO.output(16,GPIO.LOW)
      GPIO.output(21,GPIO.LOW)
    elif(value == 3):
      GPIO.output(21,GPIO.HIGH)
      GPIO.output(16,GPIO.LOW)
      GPIO.output(20,GPIO.LOW)
               
root = Tk()
root.geometry('100x100')
r = IntVar()
r.get()


            

R1 = Radiobutton(root,variable = r,value = 1,command =lambda: blinky(r.get()))

R1.pack(anchor = N)

R2 = Radiobutton(root,variable = r,value = 2,command =lambda: blinky(r.get()))
R2.pack( anchor = N )
R3 = Radiobutton(root,variable = r,value = 3,command = lambda: blinky(r.get()))

R3.pack(anchor = N)


exit = Button(text = "Exit",command = root.destroy)
exit.pack(anchor = N)



label = Label(root)
label.pack()

root.mainloop()
GPIO.cleanup()

try:
    import tkinter as tk #Tkinter for the UI
    import socket as so #Socket for the communication
except:
    print("Check the Packages, something went wrong! :/")  # Debugging
print("Packages loaded")  # Debugging

ip = None
port = 65432

def sendmsg(msg):
    s.send(msg)

def ABS_up():
    sendmsg(b'ABS+')

def ABS_down():
    sendmsg(b'ABS-')

def TC1_up():
    sendmsg(b'TC1+')

def TC1_down():
    sendmsg(b'TC1-')

def TC2_up():
    sendmsg(b'TC2+')

def TC2_down():
    sendmsg(b'TC2-')

def ING():
    sendmsg(b'ING')

def LIGHT():
    sendmsg(b'LIGHT')
def Startup():

    def end():
        global ip
        ip = ip_st.get()
        print(ip)
        startup_window.destroy()

    startup_window = tk.Tk() #Initialise Startupwindow
    startup_window.geometry("400x200") #Configuration of the size
    ip_st = tk.StringVar(startup_window) #var for the window
    #First screen/Info
    text = "test1" #Text for the Header
    textheader_startwindow = tk.Label(startup_window,text=text, font=(("Arial",20))).pack() #Text Header for the Info
    text2 = "Diese Software..." #Text for the Body
    text_startwindow = tk.Label(startup_window,text=text2, font=(("Arial", 15))).pack() #Text Body for the Info

    #IP eingabe
    IP_entry = tk.Entry(startup_window,textvariable=ip_st).pack() #Eingabefeld für die IP
    IP_done = tk.Button(startup_window,text="Continue", command=end).pack() #Button to continue

    startup_window.mainloop()#Run the Startupwindow


Startup() #open the Startup

#Connecting to server/System on which the python file "Server.py" is running
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((ip, port))

root = tk.Tk() #initiliseing of the Mainwindow named root
root.geometry("400x400") #confi root
root.resizable(height=False, width=False) #confi root

#Button ABS_up
ABS_up_Button = tk.Button(text='ABS+', command=ABS_up).pack()

#Button ABS_down
ABS_up_Button = tk.Button(text='ABS-', command=ABS_down).pack()

#Button TC1_up
ABS_up_Button = tk.Button(text='TC1+', command=TC1_up).pack()

#Button TC1_down
ABS_up_Button = tk.Button(text='TC1-', command=TC1_down).pack()

#Button TC2_up
ABS_up_Button = tk.Button(text='TC2+', command=TC2_up).pack()

#Button TC2_down
ABS_up_Button = tk.Button(text='TC2-', command=TC2_down).pack()

#Button ING
ABS_up_Button = tk.Button(text='ING', command=ING).pack()

#Button LIGHT
ABS_up_Button = tk.Button(text='LIGHT', command=LIGHT).pack()
root.mainloop()
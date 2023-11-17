try:
    import tkinter as tk #Tkinter for the UI
    import socket as so #Socket for the communication
except:
    print("Check the Packages, something went wrong! :/")  # Debugging
print("Packages loaded")  # Debugging

ip = None
port = 65432

def sendmsg(msg): #The sending command in a function for calling
    s.send(msg)
    return

def ABS_up(): #Function which the buttons call
    sendmsg(b'ABS+')
    return

def ABS_down(): #Function which the buttons call
    sendmsg(b'ABS-')
    return

def TC1_up(): #Function which the buttons call
    sendmsg(b'TC1+')
    return

def TC1_down(): #Function which the buttons call
    sendmsg(b'TC1-')
    return

def TC2_up(): #Function which the buttons call
    sendmsg(b'TC2+')
    return

def TC2_down(): #Function which the buttons call
    sendmsg(b'TC2-')
    return



def LIGHT(): #Function which the buttons call
    sendmsg(b'LIGHT')
    return

def ING_confirm(): #A small confirm window to aviod that you accedentialy kill the engien with the ING button
    def return_true(): #Return function for the confirm button
        def ING():  # Function for sending the ING command
                sendmsg(b'ING')  # ING ist for the word ignition
                return
        ING() #Call the command after the confirmation
        confirm.destroy() #close the confirm window
        return
    def return_false(): #Return function for the cancel button
        confirm.destroy() #close the confirm window
        return False
    confirm = tk.Tk() #open the confirm window
    confirm.geometry("200x200") #Size of the confirm window
    confirm.resizable(width=False, height=False) #Make the window not resizeble

    #Text
    text = tk.Label(confirm, text='Bitte bestätige das du die\nZündung betätigen willst').pack()
    #Button to confirm the Ingniton call
    confirm_button = (tk.Button(confirm, text='Bestätigen', background='green', command=return_true, width=12, height=5)
                      .pack())
    #Button to cancel the ingniton call
    cancel_button = (tk.Button(confirm, text='Abbrechen', background='red', command=return_false, width=12, height=5)
                     .pack())



def Startup(): #The Startupwindow which is required to connect to the server.py
    def end(): #Fuction to close the Startupwindow
        global ip #Global the var IP to edit it, befor it's a None
        ip = ip_st.get() #Getting the input the Entry
        print(ip) #Debugging
        startup_window.destroy() #Close the Startupwindow

    startup_window = tk.Tk() #Initialise Startupwindow
    startup_window.geometry("450x200") #Configuration of the size
    ip_st = tk.StringVar(startup_window) #var for the window

    #First screen/Info
    text = "Racing Button Box" #Text for the Header
    textheader_startwindow = tk.Label(startup_window,text=text, font=(("Arial",20))).pack() #Text Header for the Info
    # Text for the Body
    text2 = "Im Feld unten die IP Adresse des Computers\nwelcher die \"Sever.py\" ausführt eingeben.\n\n"
    text_startwindow = tk.Label(startup_window,text=text2, font=(("Arial", 15))).pack() #Text Body for the Info

    #IP input
    IP_entry = tk.Entry(startup_window,textvariable=ip_st).pack() #Inputfield fo the IP
    IP_done = tk.Button(startup_window,text="Continue", command=end).pack() #Button to continue

    startup_window.mainloop()#Run the Startupwindow


Startup() #open the Startup

#Connecting to server/System on which the python file "Server.py" is running
s = so.socket(so.AF_INET, so.SOCK_STREAM) #opening the Socket for the connection
s.connect((ip, port)) #connect to the host

root = tk.Tk() #initiliseing of the Mainwindow named root
w, h= root.winfo_x(), root.winfo_y() #Var's for the fullscreen
root.attributes('-fullscreen', True) #Fullscreen
root.geometry("%dx%d+0+0" % (w,h)) #IDK is from Stackoverflow but without it don't work
root.bind("<Escape>", lambda e: root.quit()) #Function to close the window with escape


#Button ABS_up
ABS_up_Button = tk.Button(text='ABS+', command=ABS_up, font=(('Ariel',20)), width=10, height=8).grid(column=0, row=0)

#Button ABS_down
ABS_up_Button = tk.Button(text='ABS-', command=ABS_down, font=(('Ariel',20)), width=10, height=8).grid(column=0, row=1)

#Button TC1_up
ABS_up_Button = tk.Button(text='TC1+', command=TC1_up, font=(('Ariel',20)), width=10, height=8).grid(column=1, row=0)

#Button TC1_down
ABS_up_Button = tk.Button(text='TC1-', command=TC1_down, font=(('Ariel',20)), width=10, height=8).grid(column=1, row=1)

#Button TC2_up
ABS_up_Button = tk.Button(text='TC2+', command=TC2_up, font=(('Ariel',20)), width=10, height=8).grid(column=2, row=0)

#Button TC2_down
ABS_up_Button = tk.Button(text='TC2-', command=TC2_down, font=(('Ariel',20)), width=10, height=8).grid(column=2, row=1)

#Button ING
ABS_up_Button = (tk.Button(text='ING', command=ING_confirm, font=(('Ariel',20)), width=10, height=8).
                 grid(column=3, row=0))

#Button LIGHT
ABS_up_Button = tk.Button(text='LIGHT', command=LIGHT, font=(('Ariel',20)), width=10, height=8).grid(column=3, row=1)

root.mainloop() #End of the root window

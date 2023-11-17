try:
    import socket as so #import of the socket to create a connection with the client
    import pyautogui as pg #Import for the key input
except:
    print("Check the Packages, something went wrong! :/") #Debugging
print("Packages loaded") #Debugging

def data_manager(data): #Management function for the recived data form the client
    valid_data = [b'ABS+', b'ABS-', b'TC1+', b'TC1-', b'TC2+', b'TC2-', b'ING', b'LIGHT'] #List of valid commands
    if data in valid_data: #checking if the command is vaild
        print(data, ' is a valid command') #Debugging
        if data == b'ABS+':
            pg.hotkey('g')
            return
        if data == b'ABS-':
            pg.hotkey('r')
            return
        if data == b'TC1+':
            pg.hotkey('w')
            return
        if data == b'TC1-':
            pg.hotkey('k')
            return
        if data == b'TC2+':
            pg.hotkey('j')
            return
        if data == b'TC2-':
            pg.hotkey('d')
            return
        if data == b'ING':
            pg.hotkey('s')
            return
        if data == b'LIGHT':
            pg.hotkey('q')
            return
    else:
        print(data, 'is a invalid command') #Debugging

Host = "127.0.0.1" #Placeholder for the IP
Port = 65432 #Portnummber

server = so.socket(so.AF_INET, so.SOCK_STREAM) #TCP Socket is created
server.bind((Host, Port)) #Binding the Server on the IP and Port
server.listen() #Open the connection

conn, addr = server.accept() #ip and host form the client
with conn: #opening the connection to the client
    print(f'Connected by {addr}') #Debugging
    while True:
        data = conn.recv(1024) #Data which recived the server
        print(data) #Debugging
        data_manager(data) #Calling the data management function
        if not data:
            break #stop the program if conection get lost
import threading
from threading import Thread
import bluetooth
import time
import NeoSpectraMicro as ns
import os
import struct

bool = True

while bool:
    os.system("sudo sdptool add SP")
    port = 1
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind(("", port))
    s.listen(1)
    print("Waiting for connection ...")
    try:
        client, clientAddress = s.accept()
        if client:
            print("connecté a {} ".format(clientAddress))
        while True:
            data = client.recv(8192)
            data = str(data, 'utf-8')
            print(data)
            if data == '5':
                (wav, abs) = ns.runAbsorbance()
                client.sendall(str(wav))
                client.send(",")
                client.sendall(str(abs))
                print(abs)
            elif data == '4':
                ns.runBackground()
            elif data == '1':
                id = ns.readModuleID()
                client.send(str(id))
            elif data == '2':
                ns.checkBoard()
    except:
        print("Socket fermé ")
        client.close()
        s.close()
        bool = False

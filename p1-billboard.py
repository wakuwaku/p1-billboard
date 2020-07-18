# python 3 version
#  p1-billboard reads from Domoticz host and shows power usage numbers with tkinter
#  prerequisite: P1 cable connected and activated in Domoticz. Domoticz idx for power counter. 
#  Also shows costs per 24 hours and the current time 
#  example p1 meter uitlezen http://10.0.1.122:8080/json.htm?type=devices&rid=343

import tkinter as tk
import time
import urllib.request
import base64
import json
import sys

if len(sys.argv) == 1 :
    dhost = '10.0.1.122' # Domoticz host ip address
    dport = '8080' # Domoticz port
    devid = '343' # Domoticz idx 
    kwhprijs = 0.21 # Kwh price
else:
    dhost = sys.argv[1]
    dport = sys.argv[2]
    devid = sys.argv[3]
    kwhprijs = sys.argv[4]
    kwhprijs=float(kwhprijs)
for f in sys.argv:
    print("arguments used: "+ f)

url = 'http://' + str(dhost) + ":" + str(dport) + "/json.htm?type=devices&rid=" + str(devid)
print("web api string used: " + url)
authKey = base64. b64encode(b'username:password',altchars=None) 
# base64.b64encode("username:password")
headers = {b"Content-Type":b"application/json", b"Authorization":b"Basic " + authKey}
data = { "param":"value"}


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.clock = tk.Label(self, text="")
        self.clock.pack()
        # start the clock "ticking"
        self.update_clock()
        
    def update_clock(self):
        request = urllib.request.Request(url, None, headers)
        for key,value in headers.items():
            request.add_header(key,value)

        response = urllib.request.urlopen(request)
        
        data = response.read().decode()
        #print(data)
        obj =json.loads(data)
        # print(obj["result"][0]["Usage"])
        # print(obj["result"][0]["Data"])
        # Lees het Data value uit. Dit is een ; separated lijst. stop de  waardes in een array
        array = obj["result"][0]["Data"].split(";")
        # print(array[4]) # array[4] is de wattage
        # kosten per 24 uur = watts/1000 * kwh prijs van 0.21 * 24 uur(NUON 2016)
        k = float(array[4])/1000 * kwhprijs * 24
        # round k back to 2 digits and convert to string object
        kosten_per_24uur =  str(format( k ,'.2f'))
        # Haal de Wattage  waarde uit dit object
        inGebruik = obj["result"][0]["Usage"]
        # print("Huidige verbuik is: "+ inGebruik)
        now = time.strftime("%H:%M:%S" , time.localtime())
        self.clock.configure(text="\n" + inGebruik  + "\n\n" + u"\u20AC " +  kosten_per_24uur + " per dag"  + "\n\ntijd " + now , font=("Arial", 72))
        # call this function again in one second
        self.after(1000, self.update_clock)
if __name__== "__main__":
    #app = tk.Tk()

    app = SampleApp()
    app.mainloop()

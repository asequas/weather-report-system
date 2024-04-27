import pandas as pd
from time import sleep
import pyrebase
import time
import http.client, urllib

conn = http.client.HTTPSConnection("api.pushover.net:443")
#from Adafruit_IO import Client, Feed
run_count = 0
#ADAFRUIT_IO_KEY = 'key'
#ADAFRUIT_IO_USERNAME = 'user'
#aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
config = {
  "apiKey": "apikey",
  "authDomain": "http://project-968cf.firebaseapp.com",
  "databaseURL": "https://project-968cf-default-rtdb.firebaseio.com",
  "storageBucket": "http://project-968cf.appspot.com"
}
firebase = pyrebase.initialize_app(config)
f=0
while True:
   database = firebase.database()   
   RGBControlBucket = database.child("weather")
   light = RGBControlBucket.child("temp").get().val()
   RGBControlBucket = database.child("weather")
   count = RGBControlBucket.child("hum").get().val()
   RGBControlBucket = database.child("weather")
   humi = RGBControlBucket.child("rain").get().val()
   #print(light,count,humi)
   tempi=int(light)
   #print("Fahrenheit:"+str(tempi*9/5+32))
   #aio.send_data('a',temp)
   print(tempi)
   if(tempi>32):
       print("summer")
   if(tempi<32):
       print("winter")
   if(tempi>30):
        if(f==0):
            conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": "token",
                "user": "user",
                "title": "Weather report",
                "message": "turn on the ac",
                "url": "",
                "priority": "0" 
            }), { "Content-type": "application/x-www-form-urlencoded" })

            f=1
        else:
            continue
        
        
   elif(tempi<26):
        if(f==1):
            conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": "token",
                "user": "user",
                "title": "Weather report",
                "message": "turn off the ac",
                "url": "",
                "priority": "0" 
            }), { "Content-type": "application/x-www-form-urlencoded" })

            f=0
        else:
            continue
   
    
   #time.sleep(3)
   #aio.send_data('b',humi)
   #time.sleep(3)
   #aio.send_data('e',count)
   #time.sleep(3)
   #aio.send_data('c',light)
   #time.sleep(3)
   #stri=KNN.predict([[temp,humi,light]])
   #print(stri[0])
   #database.child("PROJECT").update({"RES":stri[0]})
   #aio.send_data('j',stri[0])

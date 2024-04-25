import pandas as pd
from time import sleep
import pyrebase
import time

# Initialize Firebase configuration
config = {
  "apiKey": "AIzaSyC5Q-66lWOj5kZCl1q7KvYD9ZO9pecFHkw",
  "authDomain": "test-d3894.firebaseapp.com",
  "databaseURL": "https://test-d3894-default-rtdb.firebaseio.com",
  "storageBucket": "test-d3894.appspot.com"
}
firebase = pyrebase.initialize_app(config)

# Loop to continuously read data from Firebase database
while True:
   # Connect to Firebase database
   database = firebase.database()

   # Read temperature, humidity, and rainfall data from Firebase
   RGBControlBucket = database.child("weather")
   temp = RGBControlBucket.child("temp").get().val()
   count = RGBControlBucket.child("hum").get().val()
   humi = RGBControlBucket.child("rain").get().val()

   # Convert temperature from Celsius to Fahrenheit
   temp_fahrenheit = int(temp) * 9/5 + 32
   print("Temperature (Fahrenheit): " + str(temp_fahrenheit))

   # Here, you can include additional functionalities such as data analysis, data visualization, or sending data to other services.
   # For example, you can uncomment the lines below to send data to Adafruit IO:
   # aio.send_data('a', temp)
   # aio.send_data('b', count)
   # aio.send_data('e', humi)
   # aio.send_data('c', temp_fahrenheit)

   # Uncomment the lines below if you have additional processing or data analysis tasks
   # For example, using machine learning models like KNN for prediction.
   # stri = KNN.predict([[temp, humi, light]])
   # print(stri[0])
   # database.child("PROJECT").update({"RES": stri[0]})
   # aio.send_data('j', stri[0])

   # Delay for a few seconds before reading data again
   time.sleep(3)

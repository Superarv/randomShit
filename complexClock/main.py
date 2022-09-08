import re, time, os, keyboard, pytz
from datetime import datetime as dt


print("Welcome to the complex clock app.")
print()
print("Command To Set A Timer: '/timer {minutes} : {seconds}'")
print("Command To Start A Stopwatch: '/stopwatch'")
print("Command To Check World Time: '/time {region} / {city/area}'")
print("(go to https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568 for a list of acceptable time zones.)")
print()
print("Code for project: github.com/Superarv/randomShit")

def timer(user_input):
  vals = re.split(':', user_input)
  minutes = float(vals[0])
  seconds = float(vals[1])
  while seconds >= 1 and minutes >= 0:
    seconds -= 1
    if seconds <= 0:
      minutes -= 1
      seconds += 59
    if minutes <= -1 and seconds <= 59:
      time.sleep(1)
      print("Timer completed")
      break
    if seconds > 9:
      print(str(int(minutes)) + ":" + str(int(seconds)))
    if seconds <= 9:
      print(str(int(minutes)) + ":0" + str(int(seconds)))
    
    
    time.sleep(1)
    os.system('clear')

def stopwatch(user_input):
  minutes = 0
  seconds = 0
  while True:
    seconds += 1
    if seconds >= 60:
      minutes += 1
    if seconds <= 9:
      print(str(int(minutes)) + ":0" + str(int(seconds)))
    if seconds > 9:
      print(str(int(minutes)) + ":" + str(int(seconds)))
    time.sleep(1)
    os.system('clear')
    
def world_time(user_input):
  tzs = pytz.all_timezones_set

  if user_input in tzs:
    tz = pytz.timezone(user_input)
    city_region = re.split('/', user_input)
    city = city_region[1]
    region = city_region[0]
    
    
    print("The local time in", city, "is", dt.now(tz).strftime("%H:%M:%S"))
  elif user_input == "":
    print("Local time is", dt.now().strftime("%H:%M:%S"))
    


user = input("Enter command: ")
user = user.replace(' ', '')

if '/timer' in user:
  user = user.replace("/timer", "")
  os.system('clear')
  timer(user)

if '/stopwatch' in user:
  user = user.replace("/stopwatch", "")
  os.system('clear')
  stopwatch(user)

if '/time' in user:
  user = user.replace("/time", "")
  os.system('clear')
  world_time(user)



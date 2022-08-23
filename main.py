from colorama import init, Fore, Back, Style
from pystyle import Colorate, Colors, Write
from replit import db
init()

print(Fore.GREEN + f"===============================================================\n 🍃 Welcome To The EcoMeter | Made By Astro3000 🍃\n===============================================================" + Fore.RESET)
print(Fore.GREEN + "To Get Started Choose One: \n 1. Log In \n 2. Sign Up" + Fore.RESET)
signuporlogin = input()
if signuporlogin == "1":
  uname = input(Fore.GREEN + "Username: " + Fore.RESET)
  pword = input(Fore.GREEN + "Password: " + Fore.RESET)
  if uname+"pword" in db:
    if db[uname+"pword"] == pword:
      print(Fore.GREEN + "Success" + Fore.RESET)
    else:
      print(Fore.GREEN + "Username Or Password Incorrect" + Fore.RESET)
      exit()
elif signuporlogin == "2":
  uname = input(Fore.GREEN + "Username: " + Fore.RESET)
  pword = input(Fore.GREEN + "Password: " + Fore.RESET)
  if uname not in db:
    db[uname] = uname
    db[uname+"pword"] = pword
    db[uname+"points"] = 0
    print(Fore.GREEN + "Signed Up" + Fore.RESET)
  else:
    print(Fore.GREEN + "User Already Exists" + Fore.RESET)
    exit()
  
else:
  print(Fore.GREEN + "You Did Not Select One Of The Two" + Fore.RESET)
  exit()
print(Fore.GREEN + f"===============================================================\n👋 Hello {uname} | Points: {db[uname+'points']}" + Fore.RESET)
def home():
  
  points = db[uname+"points"]
  print(Fore.GREEN + f" Options:\n 1. Do your daily EcoCheck\n 2. View your stats\n 3. Look Up A User\n 4. Change your password\n 5. Log Out" + Fore.RESET)
  homescreeninput = input()
  if homescreeninput == "1":
    print(Fore.GREEN + "Welcome To The Daily EcoCheck!\n" + Fore.RESET)
    print(Fore.GREEN + "Question #1:\n Did you drive today? (y/n)" + Fore.RESET)
    driveinput = input()
    if driveinput.lower() == "y":
      drivetime = int(input(Fore.GREEN + "How long for? (Minutes)" + Fore.RESET))
    else:
      drivetime = 0
      print(Fore.GREEN + "Question #2:\n Did you order takeout today? (y/n)" + Fore.RESET)
      takeoutinput = input()
      if takeoutinput == "y":
        print(Fore.GREEN + "How many times?" + Fore.RESET)
        takeouttimes = int(input())
        print(Fore.GREEN + "How many people?" + Fore.RESET)
        takeoutppl = int(input())
      else:
        takeoutppl = 0
        takeouttimes = 0
      print(Fore.GREEN + "Question #3:\n Did you use a laptop and/or phone today? (y/n)" + Fore.RESET)
      screensinput = input()
      if screensinput.lower() == "y":
        print(Fore.GREEN + "How long for? (Minutes)" + Fore.RESET)
        screentime = int(input())
      else:
        screentime = 0
    wattsused = screentime*0.0985
    litresperminute = 0.01
    gasused = litresperminute*drivetime
    foodandplasticwaste = 15*takeoutppl*takeouttimes
    print(Fore.GREEN + f"You used {gasused} litres of gas today, and made about {foodandplasticwaste} grams of packaging/plastic waste today. You also used {wattsused} watts.\n**Please Note That This Is Based On Averages**")
    if foodandplasticwaste <= 100:
      points += 10
    elif foodandplasticwaste <= 150:
      points += 5
    elif foodandplasticwaste <= 200:
      points += 3
    else:
      points -= 3

    if gasused <= 0.7:
      points += 10
    elif gasused <= 3:
      points += 5
    elif gasused <= 5:
      points += 1
    else:
      points -= 1
    if wattsused <= 30:
      points += 10
    elif wattsused <= 20:
      points += 5
    db[uname+"points"] = points
    print(Fore.GREEN + "You now have" + str(db[uname+"points"]) + " points" + Fore.RESET)
  elif homescreeninput == "2":
      print(Colorate.Horizontal(Colors.blue_to_green, f"🍃 {uname} | Points: {db[uname+'points']} 🍃"))
  elif homescreeninput == "3":
    print(Fore.GREEN + "Who would you like to lookup?" + Fore.RESET)
    lookup = input()
    if lookup in db:
      print(Colorate.Horizontal(Colors.blue_to_green, f"🍃 {db[lookup]} | Points: {db[lookup+'points']} 🍃"))
    else:
      print(Fore.GREEN + "User Does Not Exist" + Fore.RESET)
  elif homescreeninput == "4":
    print(Fore.GREEN + "Enter Previous Password:" + Fore.RESET)
    prevpword = input()
    if prevpword == db[uname+"pword"]:
      print(Fore.GREEN + "Enter new password:" + Fore.RESET)
      newpword = input()
      db[uname+"pword"] = newpword
    else:
      print(Fore.GREEN + "Password Incorrect" + Fore.RESET)
  elif homescreeninput == "5":
    exit()





while 1 == 1:
  home()
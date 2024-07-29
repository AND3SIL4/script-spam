import time
import pyautogui as auto
import webbrowser as web

#User inputs
phone_number = int(input("Type the phone number destination (only the number): "))
message = input("Type the spam message: ")
number_of_messages = int(input("Number of message to send (only number):" ))

url_whatsapp = f"https://web.whatsapp.com/send?phone=+57{phone_number}"
web.open(url_whatsapp)

time.sleep(15) #Wait for 145 seconds

try:
    if isinstance(number_of_messages, int) and isinstance(phone_number, int):
        for i in range(number_of_messages):
            auto.typewrite(message)
            auto.press("enter")
    else:
        print("The information is not correct 😟")
except TypeError:
    print("The information is not correct 😟")
    
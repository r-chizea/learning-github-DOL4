timeMenu = [
    "1. add 2 times",
    "2. Find the difference between 2 times", 
    "3. convert to hours", 
    "4. convert to minutes", 
    "5. convert minutes to time",
    "6. convert hours to time", 
    "7. convert days to time", 
    "8. exit"
]

print(timeMenu)

operation = input("please choose an option from the menu: ")

if operation == 1:
    time1 = input("please enter a time in DD:HH:MM format: ")
    time2 = input("please enter a second time in DD:HH:MM format: ")
    time1_list = time1.split(":")
    time2_list = time2.split(":")
    
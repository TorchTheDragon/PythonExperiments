# Car Game
command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started")
        else:
            print("Car has been started")
            car_started = True
        
    elif command == "stop":
        if car_started:
            print("The car has been stopped")
            car_started = False
        else:
            print("The car wasn't even moving")
    elif command == "help":
        print("""
Help - Brings up the help page
Start - Starts the car
Stop - Stops the car
Quit - Quits the game
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand your command, try using the Help command")
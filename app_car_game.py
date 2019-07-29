"""
A Car game simulation
"""
command = ""
#command = input("> ").lower()
started = False

while True:
    command = input("> ").lower()

    if command == "help" or command == "hi":
        print("""
start   - to start the car
stop    - to stop the car
quit    - to exit
        """)

    elif command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started, ready to go!")

    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped")

    elif command == "quit":
        print("Thank you for using Car Simulation Game. Goodbye")
        break

    else:
        print("I don't understand that....")

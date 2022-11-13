command = ''
while command.lower() != "quit":
    command = input('>')
    if command.lower() == "start":
        print("Car started... ready to go")
    elif command.lower() == "stop":
        print("Car stopped")
    elif command.lower() == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to terminate the program")
    elif command.lower() == "quit":
        print("Process terminated")
    else:
        print("I don't understand")
        break

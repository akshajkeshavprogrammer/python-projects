print("Welcome to car simulation game! Type (help) to start!")
is_start = False
while True:
    a = input("> ").upper()
    if a == "HELP":
        print('''Commands=>
            Start- To start the car
            Stop- To stop the car  
            Quit- To quit the game''')
    elif a == "START":
        if is_start:
            print("The car is already on! What are you doing!?")
        else:
            print("Car started... Ready to go!")
        is_start = True
    elif a == "STOP":
        if is_start == False:
            print("The car is already off! What are you doing!?")
        else:
            print("Car stopped")
        is_start = False
    elif a == "QUIT":
        print("Game over")
        break
    else:
        print("I don't understand you...")






    

    
    




command= input("Enter a command: (start/stop/restart) ")

match command:
    case "start":
        print("System Starting.....")
    case "stop":
        print("System Shutting Down.....")
    case "restart":
        print("System Restarting.....")
    case _ :
        print("Unknown Command")
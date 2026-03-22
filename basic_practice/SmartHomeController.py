device = input("Enter Devices = ")

match device.lower():
    case "fan":
        print("Turn on Fan")
    case "light":
        print("Turn on Light")
    case "ac":
        print("Starting AC")
    case _:
        print("Device not Recognize")
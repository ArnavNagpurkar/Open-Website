import webbrowser

while True:
    start = int(input("Enter 1 to open a website and 0 to exit: "))
    if start == 1:
        url = input("Enter the name of the website eg(youtube.com) to open: ")
        if "." not in url:
            print("Not a valid website!")
            print("Try again!")

        else:
            splitSite = url.split(".")
            webName = splitSite[0]
            webExtension = splitSite[1]
            webbrowser.open(f"https://www.{webName}.{webExtension}/")
            print(f"Opening {webName}")
            break

    elif start == 0:
        print("Thanks for using website Opener!")
        break

    elif str in start:
        print("Invalid Input, Try again!")

    else:
        print("Invalid Input, Try again!")


import os

def makeDir(dirName):
    os.mkdir(dirName)

def deleteDir(dirName):
    os.rmdir(dirName)

def ipScanner(network):
    ip = network.split(".")[-1]
    while ip < 256:
        os.system(f"ping {network}")
        

while True:
    a_commands = [
                  "exit exits the program", 
                  "help to get a list of all commands", 
                  "hello test the shell", 
                  "ld lists you directories", 
                  "credir creates a directory", 
                  "deldir deletes a directory",
                  "shutdown shuts the computer down"
                  ]
    comm = input("shell> ")

    if comm == "exit": #exits the shell
        break
    elif comm == "help": #print all available commands
        print("\n".join(a_commands))
    elif comm == "hello": #print a command, you see when the shell works
        print("hello, if you see this, your shell works")
    elif comm == "ld": #lists the directories and files in your dir
        print(os.listdir())
    elif comm == "credir": # creates directory
        name = input("what is the name of your directory: ")
        if name == "":
            print("enter valid name")
        else:
            makeDir(name)
            print("your directory has been createt")
    elif comm == "deldir":
        name = input("what is the name of the directory you want to delete: ")
        if name == "":
            print("enter valid name")
        else:
            deleteDir(name)
            print("your directory has been deletet")
    elif comm == "shutdown":
        when = input("In wie viel sekunden soll heruntergefshren werden: ")
        if when == "":
            print("enter valid time")
        else:
            os.system(f"shutdown /s /t {when}")
            print(f"your system is shutting down in {when} seconds. to cancel press c and ENTER")
            a = input()
            if a == "c" or "C":
                os.system("shutdown /a")
                print("Shutdown canceled")
    elif comm == "IP" or comm == "Ip" or comm == "ip":
        ip = os.system("ipconfig")
        print(ip)
    elif comm == "scan":
        ipToScan = input("The Network IP you want to scan: ")
        print("you are going to scan the Network", ipToScan)
        yn = input("If correct press: y, else press n: ")
        if yn == "y":
            ipScanner(ipToScan)
    


import math
import time
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1
Run = True

while Run == True:
    print("\n"*60)
    print("""
Prime Generator
Version: 0.3.3
By Joss Bird
CC 2016""")
    print("Menu:")
    print("1. Continue calculating primes")
    print("2. Test a specific number")
    print("3. View largest know prime number in a generated file")
    print("4. Update Log")
    print("5. prime number calculator method 2 (Significantly faster)")
    print("9. Quit")
    Operation = input("Select>")
    if Operation == "1":
        newprimes = 0
        print("If the file you specify does not exist one will be created for you")
        file_name = ""
        while file_name == "":
            file_name = input("File Name>")
        if "." in file_name:
            print("Extenstion found doing nothing!")
        else:
            print("Error: no extension found!")
            decision = input("Would you like to make your a file a text file? (y/n) >")
            if decision.lower() == "y":
                print("Now treating file as a text file")
                file_name = file_name + ".txt"
            else:
                print("Okay doing nothing")
        try:
            f = open(file_name,"r+")
        except FileNotFoundError:
            print("Error: Prime Number list not found generating one as: '",file_name,"'")
            t = time.time()
            f = open(file_name,"w")
            m = "2\n"
            f.write(m)
            print("Done in:",(time.time()-t),"Seconds")
            f.close()
        length = file_len(file_name)
        f = open(file_name,"r+")
        t = time.time()
        lines = []
        for line in f:
            lines.append(line)
        print("Done in:",(time.time()-t),"Seconds")
        print("Note: as of Version: 0.1.8 prime numbers are no longer found on screen and can be seen on the main menu or in the specified file")
        print("Largest known prime at the moment is:",lines[length-1])
        print("Press Ctrl+C to quit")
        print("Now calculating primes!")
        t = time.time()
        try:
            Primes = [1,2]
            NumberTry = int(lines[length-1])+1
            time.sleep(3)
            while True:
                Loop = 2
                trying = True
                AmmountTry = int(2+math.sqrt(NumberTry))
                while trying == True:
                    if Loop < AmmountTry:
                            if (NumberTry/Loop)==int(NumberTry/Loop):
                                trying = False
                                Prime = False
                                break
                            else:
                                Loop = Loop + 1
                    else:
                        Prime = True
                        trying = False
                if Prime == True:
                    Primes.append(NumberTry)
                    f = open(file_name,"a")
                    m = str(NumberTry)+"\n"
                    f.write(m)
                    f.close
                    newprimes = newprimes + 1
                NumberTry = NumberTry + 1
        except KeyboardInterrupt:
                print("\nStopping...")
                print("Time spent calculating: ",int((time.time()-t)),"Seconds")
                f = open(file_name,"r+")
                lines = []
                for line in f:
                    lines.append(line)
                length = file_len(file_name)
                print("New largest known prime at the moment is:",lines[length-1])
                print("Average primes per second was:",newprimes/(time.time()-t))
                input("Press enter to continue...")

    elif Operation == "2":
            Loop = 2
            trying = True
            NumberTry = int(input("Which number would you like to test?>"))
            AmmountTry = int(2+math.sqrt(NumberTry))
            while trying == True:
                if Loop < AmmountTry:
                        if (NumberTry/Loop)==int(NumberTry/Loop):
                            trying = False
                            Prime = False
                            break
                        else:
                            Loop = Loop + 1
                else:
                    Prime = True
                    trying = False
            if Prime == True:
                print(NumberTry,"is prime")
                input("Press enter to continue...")
    elif Operation == "3":
        file_name = input("File Name>")
        try:
            f = open(file_name,"r+")
            length = file_len(file_name)
            f = open(file_name,"r+")
            lines=f.readlines()
            print("Largest known prime at the moment is:",lines[length-1])
        except FileNotFoundError:
            print("Error: file not found!")
            print("Suggestion: Make sure you have included the extension and is in the same folder as this code")
        input("Press enter to continue...")
    elif Operation == "4":
        print("*"*60)
        print("""Update Log:
Version: 0.1.7:
+ Started keeping update log
+ Started using files as storage
Version: 0.1.8:
+ Custom file names
+ Testing individual numbers
Version: 0.1.9:
+ Finding largest prime in a generated document by this program
Version: 0.2.0:
+ Timer for time spent calculating prime numbers
Version: 0.2.1:
* Rounded calculation timer
+ A pause to see tbe calculation timer
Version: 0.2.2:
* Corrected grammar and spelling mistakes
+ A pause for individual prime number tester
Version: 0.2.3:
+ New largest prime number text
Version: 0.2.4:
* Corrected largest prime number total at the end of calculation
Version: 0.3.0:
+ New way of calculating primes (Experimental)
Version: 0.3.1:
+ Time taken for importing primes
Version: 0.3.2:
* Corrected the way primes are imported from files to avoid memory errors
* Stopped file names being blank
Version: 0.3.3:
* Decided the new way of calculating primes was stable""")
        input("Press enter to continue...")
    elif Operation == "5":
        newprimes = 0
        print("If the file you specify does not exist one will be created for you")
        file_name = ""
        while file_name == "":
            file_name = input("File Name>")
        if "." in file_name:
            print("Extenstion found doing nothing!")
        else:
            print("Error: no extension found!")
            decision = input("Would you like to make your a file a text file? (y/n) >")
            if decision.lower() == "y":
                print("Now treating file as a text file")
                file_name = file_name + ".txt"
            else:
                print("Okay doing nothing")
        try:
            f = open(file_name,"r+")
        except FileNotFoundError:
            print("Error: Prime Number list not found generating one as: '",file_name,"'")
            t = time.time()
            f = open(file_name,"w")
            m = "2\n"
            f.write(m)
            m = "3\n"
            f.write(m)
            m = "5\n"
            f.write(m)
            print("Done in:",(time.time()-t),"Seconds")
            f.close()
        primes = []
        t = time.time()
        print("Importing prime numbers... (this may take a while)")
        length = file_len(file_name)
        f = open(file_name,"r+")
        lines=f.readlines()
        f = open(file_name,"r+")
        i = 0
        while i < length:
            primes.append(int(f.readline()))
            i = i + 1
        print("Done in:",(time.time()-t),"Seconds")
        print(len(primes),"primes imported.")
        print("Note: as of Version: 0.1.8 prime numbers are no longer found on screen and can be seen on the main menu or in the specified file")
        print("Largest known prime at the moment is:",lines[length-1])
        print("Press Ctrl+C to quit")
        print("Now calculating primes!")
        t = time.time()
        try:
            i = 0
            NumberTry = int(lines[length-1])+1
            while True:
                testingnumber = primes[i]
                Loop = 0
                trying = True
                AmmountTry = int(3+math.sqrt(NumberTry))
                while trying == True:
                    if testingnumber < AmmountTry:
                            if (NumberTry/testingnumber)==int(NumberTry/testingnumber):
                                trying = False
                                Prime = False
                                break
                            else:
                                i = i + 1
                                testingnumber = primes[i]
                    else:
                        Prime = True
                        trying = False
                if Prime == True:
                    primes.append(NumberTry)
                    f = open(file_name,"a")
                    m = str(NumberTry)+"\n"
                    f.write(m)
                    f.close
                    newprimes = newprimes + 1
                NumberTry = NumberTry + 1
                i = 0
        except KeyboardInterrupt:
                print("\nStopping...")
                print("Time spent calculating: ",int((time.time()-t)),"Seconds")
                f = open(file_name,"r+")
                lines = []
                for line in f:
                    lines.append(line)
                length = file_len(file_name)
                print("New largest known prime at the moment is:",lines[length-1])
                print("Average primes per second was:",newprimes/(time.time()-t))
                print("Largest number tried was: ",NumberTry)
                input("Press enter to continue...")
    elif Operation == "9":
        Run = False

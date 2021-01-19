try:
    spd = float(input("\nEnter the speed of the vehicle in mph: "))
    hrs = int(input("Enter the number of hours traveled: "))
   
    
    # Prints continuous range up to user input
    # Formats via modulo operator
    print("\nHour   Distance Traveled")
    print("--------------------------")
    for t in range(1, hrs+1):
        print("%d      %.1f" % (t, t*spd))
      

except:
    print("\nInvalid entry (whole hours only)")
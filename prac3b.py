def Tower_of_Hanoi(disk,src,aux,dest):
    if disk == 1:
        print(f"Move Disk 1 from source {src} to Destination {dest}")
        return 1
    steps1= Tower_of_Hanoi(disk-1,src,aux,dest)
    print(f"Transfer of disk {disk} from source {src} to destination {dest}")
    steps2= Tower_of_Hanoi(disk-1,aux,dest,src)
    return steps1 + 1 + steps2

disk= int(input("For how many rings do you want to perform tower of hanoi?"))
Total_steps=Tower_of_Hanoi(disk,"A","B","C")
print("\nThe total number of moves required are:", Total_steps,"\n")

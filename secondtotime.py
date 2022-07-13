time=int(input("enter seconds = "))
Hour=time/3600
time=time%3600
minutes=time/60
Seconds=time%60
print(round(Hour),':',round(minutes),':',Seconds)
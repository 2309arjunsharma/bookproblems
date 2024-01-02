i = 0
total = 0
while(i<15):
    a = float(input("Enter the temperature in C*: "))
    total = total + a
    i = i + 1

avg = total/i
F = avg*9/5+32
print("The temperature of 15 days is",F,"*Fahrenheit")

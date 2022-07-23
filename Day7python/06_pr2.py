# write a function to find the celcius to farhanite

def farh(cel):
    return (cel * (9/5)) + 32


c = int(input("Enter the temperature of your aria ? : "))
f = farh(c)
print("Fahreheit Temperature is " + str(f))

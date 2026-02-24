# Problem 1

# convert to celsius

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print("Temperature in Celsius:", c)

if c <= 0:
    print("Ice")

if c > 0:
    if c <= 100:
        print("Liquid")

if c > 100:
    print("Gas")

print()

def tempratire_conversion():
    print("select the conversion type:")
    print("1. celsius to fahrenheit")
    print("2. fahrenheit to celsius")
conversion = input(" enter 1 or 2:")

if conversion == '1':
    celsius= float(input(" input temprature in celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equal to {fahrenheit}F")
elif conversion == '2':
   fahrenheit = float(input(" input temprature in fahrenheit:"))
   celsius = (fahrenheit - 32) * 5/9
   print(f"{fahrenheit}F is equal to {celsius}C")

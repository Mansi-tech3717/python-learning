def fer(f):
    return 5*(f-32)/9
f= int(input("Enter the temperature in Fahrenheit: "))
c= fer(f)
print("The temperature in Celsius is:",round(c,2),"c")
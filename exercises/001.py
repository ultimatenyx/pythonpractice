# Program to convert Celsius to Farenheit

def convertCToF(dc):
    return float(dc)*9/5+32

degree = input("Enter the value in Degree Celsius:")
print("The temperature in degree Farenheit is "+str(convertCToF(degree)))
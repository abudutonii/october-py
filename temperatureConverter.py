def unitsToConvert():
    units = int(input('''
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
-- '''))
    return units



def celsiusToFahrenheit(tempValue):
    F = ((9/5) * tempValue) + 32
    return F

def fahrenheitToCelsius(tempValue):
    C = (tempValue - 32) * (5/9)
    return C

def celsiusToKelvin(tempValue):
    K = tempValue + 273
    return K

def kelvinToCelsius(tempValue):
    C = tempValue - 273
    return C

def fahrenheitToKelvin(tempValue):
    K = fahrenheitToCelsius(tempValue) + 273
    return K

def kelvintoFahrenheit(tempValue):
    F = celsiusToFahrenheit(tempValue - 273)
    return F



conversion = unitsToConvert()

tempToConvert = int(input('\nEnter Temperature to convert:\n'))

if conversion==1:
    print(f'\n{celsiusToFahrenheit(tempToConvert)} °F')
elif conversion==2:
    print(f'\n{fahrenheitToCelsius(tempToConvert)} °C')
elif conversion==3:
    print(f'\n{celsiusToKelvin(tempToConvert)} °K')
elif conversion==4:
    print(f'\n{kelvinToCelsius(tempToConvert)} °C')
elif conversion==5:
    print(f'\n{fahrenheitToKelvin(tempToConvert)} °K')
elif conversion==6:
    print(f'\n{kelvintoFahrenheit(tempToConvert)} °F')
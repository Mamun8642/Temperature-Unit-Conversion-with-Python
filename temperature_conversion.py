def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    print("Hello there")
    print("Select the input temperature unit you want to convert:")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    
    input_unit = int(input("Enter the number corresponding to the input unit: "))
    if input_unit not in [1, 2, 3]:
        print("Invalid input. Please restart the program.")
        return

    temp_value = float(input("Enter the temperature value: "))

    print("Select the output temperature unit:")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    
    output_unit = int(input("Enter the number corresponding to the output unit: "))
    if output_unit not in [1, 2, 3]:
        print("Invalid output. Please restart the program.")
        return

    if input_unit == 1:  
        if output_unit == 2:
            print(f"{temp_value} Celsius is {celsius_to_fahrenheit(temp_value):.2f} Fahrenheit.")
        elif output_unit == 3:
            print(f"{temp_value} Celsius is {celsius_to_kelvin(temp_value):.2f} Kelvin.")
        else:
            print(f"{temp_value} Celsius remains {temp_value} Celsius.")
    elif input_unit == 2:  # Fahrenheit
        if output_unit == 1:
            print(f"{temp_value} Fahrenheit is {fahrenheit_to_celsius(temp_value):.2f} Celsius.")
        elif output_unit == 3:
            print(f"{temp_value} Fahrenheit is {fahrenheit_to_kelvin(temp_value):.2f} Kelvin.")
        else:
            print(f"{temp_value} Fahrenheit remains {temp_value} Fahrenheit.")
    elif input_unit == 3:  # Kelvin
        if output_unit == 1:
            print(f"{temp_value} Kelvin is {kelvin_to_celsius(temp_value):.2f} Celsius.")
        elif output_unit == 2:
            print(f"{temp_value} Kelvin is {kelvin_to_fahrenheit(temp_value):.2f} Fahrenheit.")
        else:
            print(f"{temp_value} Kelvin remains {temp_value} Kelvin.")


temperature_converter()

celsius_input = float(input("Enter temperature in Celsius: "))
degree_f = (celsius_input * 9 / 5) + 32
degree_k = celsius_input + 273.15

print("Welcome to the Temperature Converter!")
print(f"The temperature you have entered is {celsius_input} degree Celsius.")
print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
print("Thank you for using the Temperature Converter!")

unit = input("Enter temperature unit to convert from (C, K, or F): ").upper()
temp_value = float(input("Enter temperature value: "))
if unit == "C":
    converted_f = (temp_value * 9 / 5) + 32
    converted_k = temp_value + 273.15
    print(f"{temp_value} C is {converted_f} F and {converted_k} K")
elif unit == "K":
    converted_c = temp_value - 273.15
    converted_f = (converted_c * 9 / 5) + 32
    print(f"{temp_value} K is {converted_c} C and {converted_f} F")
elif unit == "F":
    converted_c = (temp_value - 32) * 5 / 9
    converted_k = converted_c + 273.15
    print(f"{temp_value} F is {converted_c} C and {converted_k} K")
else:
    print("Invalid unit.")

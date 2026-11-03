is_true = 5 > 4
print(is_true)

age = 25
is_in_age_range = age > 20 and age < 30
print(is_in_age_range)

age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
print(f"The age group is {age_group}")

age = 15
age_group = "child"
if age > 18:
    age_group = "adult"
print(f"The age group is {age_group}")

wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

wind_speed = 5
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

grade = 55
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

temperature1 = 20
temperature2 = 25
if temperature1 == temperature2:
    print("The temperatures are equal")
else:
    print("The temperatures are not equal")

city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list[2])
print(city_list[1:3])

city_list.append("Manchester")
city_list[1] = "Birmingham"
print(city_list)

colours = ["blue", "red", "green"]
print(colours)
print(colours[1])
colours[0] = "yellow"
print(colours)
print(len(colours))
if "red" in colours:
    print("Red is in the list")
selected_colours = colours[1:3]
print(selected_colours)

i = 0
while i < 5:
    print(i)
    i += 1

for city in city_list:
    print(city)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)

sum_of_squares = 0
for i in range(1, 6):
    sum_of_squares += i ** 2
print(sum_of_squares)

countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Liftoff!")

user_age = int(input("Enter your age: "))
if user_age < 18:
    print("You are a minor.")
elif user_age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

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

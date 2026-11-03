def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")


greet_user("John", "Smith")
greet_user("John", "Smith", "UWS London")
greet_user(last_name="Smith", first_name="John", university="UWS London")

friend_list = ["John", "Jane", "Jack"]


def greet_friends(friends):
    for friend in friends:
        print(f"Hello {friend}!")


greet_friends(friend_list)


def add_numbers(num1, num2):
    result = num1 + num2
    return result


result = add_numbers(5, 10)
print(result)


def add_and_multiply_numbers(num1, num2):
    total_sum = num1 + num2
    product = num1 * num2
    return total_sum, product


total_sum, product = add_and_multiply_numbers(5, 10)
print(total_sum)
print(product)


def calculate_tax(income, tax_rate):
    return income * tax_rate


print(calculate_tax(50000, 0.2))
print(calculate_tax(35000, 0.15))
print(calculate_tax(80000, 0.4))


def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    total_for_the_year = principal
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year} £")
    return int(total_for_the_year)


final_amount = compound_interest(1000, 5, 0.03)
print(final_amount)

my_new_variable = 0


def new_function():
    my_new_variable = 5


new_function()
print(my_new_variable)

assert compound_interest(1000, 5, 0.03) == 1159
assert 5 > 2, "5 should be greater than 2"

try:
    assert 2 > 5, "2 is not greater than 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

print("Hello, World!")

favorite_color = "Blue."
print("My favorite color is", favorite_color)

number1 = 5
number2 = 3
result = number1 + number2
print("The sum is:", result)

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

time = 11
if time < 12:
    print("Good morning!")

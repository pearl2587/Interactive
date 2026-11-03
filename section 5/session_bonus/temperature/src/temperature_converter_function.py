scales = ["C", "F", "K"]


def convert(temperature_scale: str = "C", temperature_input: str = "0"):
    scale = temperature_scale.strip().upper()
    if scale not in scales:
        raise ValueError("Invalid scale. Please enter 'C', 'F', or 'K'.")

    value = float(temperature_input)

    if scales.index(scale) == 0:
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15 C).")
        degree_celcius = value
        degree_fahrenheit = (degree_celcius * 9 / 5) + 32
        degree_kelvin = degree_celcius + 273.15
    elif scales.index(scale) == 1:
        if value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67 F).")
        degree_fahrenheit = value
        degree_celcius = (degree_fahrenheit - 32) * 5 / 9
        degree_kelvin = (degree_fahrenheit + 459.67) * 5 / 9
    elif scales.index(scale) == 2:
        if value < 0.0:
            raise ValueError("Temperature cannot be below absolute zero (0 K).")
        degree_kelvin = value
        degree_celcius = degree_kelvin - 273.15
        degree_fahrenheit = (degree_kelvin - 273.15) * 9 / 5 + 32

    return degree_celcius, degree_fahrenheit, degree_kelvin


if __name__ == "__main__":
    prompt = "Enter the temperature scale you want to convert from: \n 'C' Celcius \n 'F' Fahrenheit \n 'K'. Kelvin \n"
    temperature_scale = input(prompt).strip().upper()
    if temperature_scale not in scales:
        print("Invalid scale. Please enter 'C', 'F', or 'K'.")
        exit()
    temperature_input = input(f"Enter the temperature in {temperature_scale}: ")

    degree_celcius, degree_fahrenheit, degree_kelvin = convert(temperature_scale, temperature_input)

    print("Temperature Conversion Results:")
    print(f"{degree_celcius} degree Celsius")
    print(f"{degree_fahrenheit} degree Farenheit")
    print(f"{degree_kelvin} degree Kelvin")
    print("Thank you for using the Temperature Converter!")

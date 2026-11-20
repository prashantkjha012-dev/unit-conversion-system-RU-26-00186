kM_TO_MILES = 0.621371
METER_TO_FEET = 3.28084
KG_TO_POUND = 2.20462
import math


# ---------- One function per conversion type ----------
def convert_length(option, value):
    """Return (result, from_unit, to_unit) or None for a bad option."""
    if option == 1:
        return value * kM_TO_MILES, "km", "miles"
    elif option == 2:
        return value / kM_TO_MILES, "miles", "km"
    elif option == 3:
        return value * METER_TO_FEET, "m", "feet"
    elif option == 4:
        return value / METER_TO_FEET, "feet", "m"
    else:
        return None


def convert_weight(option, value):
    if option == 1:
        return value * 1000, "kg", "g"
    elif option == 2:
        return value / 1000, "g", "kg"
    elif option == 3:
        return value * KG_TO_POUND, "kg", "pounds"
    elif option == 4:
        return value / KG_TO_POUND, "pounds", "kg"
    else:
        return None


def convert_temperature(option, value):
    if option == 1:
        return (value * 9 / 5) + 32, "C", "F"
    elif option == 2:
        return (value - 32) * 5 / 9, "F", "C"
    elif option == 3:
        return value + 273.15, "C", "K"
    elif option == 4:
        return value - 273.15, "K", "C"
    else:
        return None


def convert_time(option, value):
    if option == 1:
        return value * 60, "hours", "minutes"
    elif option == 2:
        return value / 60, "minutes", "hours"
    elif option == 3:
        return value * 3600, "hours", "seconds"
    elif option == 4:
        return value * 24, "days", "hours"
    else:
        return None


# ---------- Menus ----------
CATEGORIES = {
    1: ("Length", convert_length,
        ["km to miles", "miles to km", "meters to feet", "feet to meters"]),
    2: ("Weight", convert_weight,
        ["kg to g", "g to kg", "kg to pounds", "pounds to kg"]),
    3: ("Temperature", convert_temperature,
        ["C to F", "F to C", "C to K", "K to C"]),
    4: ("Time", convert_time,
        ["hours to minutes", "minutes to hours", "hours to seconds", "days to hours"]),
}


def show_main_menu():
    print("\n===== UNIT CONVERSION SYSTEM =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("0. Exit")


def read_choice(prompt, low, high):
    """Read an integer in [low, high]. Return None if invalid."""
    text = input(prompt).strip()
    if text.isdigit():
        number = int(text)
        if low <= number <= high:
            return number
    return None


def read_value():
    """Read a number. Return None if the input is not a valid number."""
    text = input("Enter value: ").strip()
    try:
        number = float(text)
    except ValueError:
        return None
    if not math.isfinite(number):   # rejects 'nan' and 'inf'
        return None
    return number


def run_conversion(category_number):
    name, converter, options = CATEGORIES[category_number]

    print("\n--- " + name + " conversions ---")
    for i, text in enumerate(options, start=1):
        print(str(i) + ". " + text)

    option = read_choice("Select conversion (1-4): ", 1, 4)
    if option is None:
        print("Invalid choice. Select 1 to 4.")
        return

    value = read_value()
    if value is None:
        print("Invalid value. Enter a number.")
        return

    result, from_unit, to_unit = converter(option, value)
    print("%g %s = %.2f %s" % (value, from_unit, result, to_unit))


def main():
    while True:
        show_main_menu()
        choice = read_choice("Select category: ", 0, 4)

        if choice is None:
            print("Invalid choice. Select 1 to 4.")
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            run_conversion(choice)


if __name__ == "__main__":
    main()
# Mohammad Qureshi
# PSID 1789301
# LAB 12.7


# FUNCTION TO INPUT AGE AND SET ERROR MESSAGES
def get_age():
    input_age = int(input())
    if input_age < 18:
        raise ValueError("Invalid age.")
    if input_age > 75:
        raise ValueError("Invalid age.")
    return input_age

# CALCULATE HEART RATE
def fat_burning_heart_rate(age):  # function to calculate heart rate
    heart_rate = (((220 - age) * 70) / 100)
    return heart_rate

# MAIN FUNCTION
if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, heart_rate))
    except ValueError as errormsg:
        print(errormsg)
        print("Could not calculate heart rate info.")
        print()

def calculate_delivery_charge(location, weight):
    location = location.lower()
    
    if location == 'ibeju-lekki':
        if weight >= 10:
            return 5000
        else:
            return 3500
    elif location == 'epe':
        if weight >= 10:
            return 10000
        else:
            return 5000
    else:
        return None

# Get user input
location = input("Enter your delivery location (Ibeju-Lekki or Epe): ")
try:
    weight = float(input("Enter the weight of your package in kg: "))
except ValueError:
    print("Invalid weight input. Please enter a number.")
    exit()

# Calculate charge
charge = calculate_delivery_charge(location, weight)

if charge is not None:
    print(f"The delivery charge is ₦{charge}")
else:
    print("Sorry, delivery is not available to that location.")

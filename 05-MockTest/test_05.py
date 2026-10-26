distance = int(input("Enter distance in km: "))
energy_consumption = float(input("Enter energy consumption (kWh/100km): "))
price = float(input("Enter price per 1 kWh: "))

energy_used = (distance*energy_consumption)/100
cost = energy_used*price

print(f'Energy used: {energy_used} kWh')
print(f'Cost of the trip: {round(cost,2)} PLN')
height = input("Enter your height: ") #Pobranie wartości od uytkowanila
weight = input("Enter your weight: ")
height = int(height); #Konwersja na liczbę
weight = int(weight);
bmi = weight/(height/100)**2
bmi = round(bmi,2 ) #zaokrąglenie
print("Your Bmi is: ", bmi)
print("It was calculated based on your height-",height," and weight-",weight);
if bmi <= 18:
    print(f"Your BMI is too low!")
elif bmi >18 and bmi <= 25:
    print(f"Your BMI level is good")
elif bmi > 25:
    print("Your BMI is too high!")

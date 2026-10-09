height = input("Enter your height: ") #Pobranie wartości od uytkowanila
weight = input("Enter your weight: ")
height = int(height); #Konwersja na liczbę
weight = int(weight);
bmi = weight/(height/100)**2
bmi = round(bmi,2 ) #zaokrąglenie
print("Your Bmi is: ", bmi)
print("It was calculated based on your height-",height," and weight-",weight);
if bmi<19:
    print("Your BMI is too low")
if bmi >=19 and bmi<24:
    print("Your BMI is perfect")
if bmi >=24:
    print("Your BMI is too big")
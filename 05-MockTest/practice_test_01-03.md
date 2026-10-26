# PRACTICE TEST – Subjects 01, 02, 03

> **Kolokwium próbne** przygotowane do samodzielnej powtórki (nie jest to materiał prowadzącego).
>
> **Zasady:**
> * Czas: **90 minut**. Ustaw minutnik i nie zaglądaj do starych plików ani do internetu.
> * Każde zadanie z kodem zapisz w osobnym pliku, np. `test_01.py`, `test_02.py`, …
> * Zadania „bez komputera” (2 i 11) rozwiąż najpierw na kartce, dopiero potem sprawdź w trybie interaktywnym.
> * Punkty: razem **50 pkt**. Skala: 0–25 → 2.0 · 26–30 → 3.0 · 31–35 → 3.5 · 36–40 → 4.0 · 41–45 → 4.5 · 46–50 → 5.0
> * Po skończeniu wpisz `/sprawdz 05-MockTest/test_XX.py` – omówimy błędy.

---

## 1. Git and Course Introduction (3 pts)

1. You have cloned your repository from GitHub and created a new file `hello.py`. Put the following commands in the correct order so that the file appears in your repository on GitHub. Then, explain in one sentence what each command does.

    ```
    git push
    git add hello.py
    git status
    git commit -m "Add hello.py"
    ```

    Additionally, answer the question: what is the difference between `git commit` and `git push`?

## 2. Operators and Data Types (4 pts)

1. Calculate the values of the expressions **without using a computer**. Write down both the value and its data type (int, float, str or bool). Then, check your results in interactive mode.

    1. 17 // 5 * 2 + 17 % 5
    1. 2 ** 3 ** 2
    1. 10 / 4
    1. 10 // 4
    1. '3' + '4'
    1. '3' * 3
    1. int('3') + 4
    1. 7 > 5 and not 3 == 3
    1. 15 % 4 % 2
    1. 1 + 2 * 3 ** 2 // 4

    What happens if you try to calculate `'3' + 4`? Explain why.

## 3. String Operations (3 pts)

1. Write a program that reads time in the format hh:mm:ss from the keyboard and prints how many seconds have passed since midnight. Use string slicing (indexes), not the `split()` method. Sample result:

    ```
    Enter time (hh:mm:ss): 01:02:05
    Seconds since midnight: 3725
    ```

    ```python
    ###
    # A program that reads time (hh:mm:ss) and prints
    # the number of seconds since midnight.
    #
    time = input('Enter time (hh:mm:ss): ')
    hours = int(time[...])
    minutes = ...
    seconds = ...
    total = ...
    print(f'Seconds since midnight: {...}')
    ```

## 4. The Division Operators (4 pts)

1. Write a program that reads a three-digit number from the keyboard (as int). Then, the program prints the sum of its digits and the number written backwards. Use only the operators `//` and `%` – do not convert the number to a string. Sample result:

    ```
    Enter a three-digit number: 472
    Sum of digits: 13
    Reversed number: 274
    ```

    > Hint: what is the result of 472 % 10? And 472 // 10?

## 5. Practice Makes Perfect – Formulas (3 pts)

1. An electric car uses a certain amount of energy (in kWh) per 100 km. Write a program that reads the distance in km, energy consumption in kWh per 100 km and the price of 1 kWh. The program calculates and prints the total energy used and the total cost of the trip, rounded to 2 decimal places. Sample result:

    ```
    Enter distance in km: 250
    Enter energy consumption (kWh/100km): 16.5
    Enter price per 1 kWh: 0.89
    Energy used: 41.25 kWh
    Cost of the trip: 36.71 PLN
    ```

    ```python
    ###
    # The program calculates the cost of a trip by an electric car.
    #
    distance = int(input('Enter distance in km: '))
    consumption = float(input(...))
    price = ...
    total_energy = ...
    total_cost = ...
    print(...)
    ```

## 6. Binary Operations (3 pts)

1. Write a program that reads an integer from the keyboard and prints it in binary and hexadecimal form **without** the prefixes `0b` and `0x`. Additionally, the program prints how many ones (1) the binary number contains. Sample result:

    ```
    Enter an integer: 45
    Binary: 101101
    Hexadecimal: 2d
    Number of ones: 4
    ```

    > Hint: the functions bin() and hex() return a string. What can you do with a string?

## 7. Decision Statement – Debugging (3 pts)

1. The program converts exam points (0–100) into a grade. Unfortunately, for 95 points the program prints 3.0. Find out why and modify the program so that it works correctly. Use debugging mode to follow the program's statements step by step.

    ```python
    points = 95

    if points >= 50:
        grade = 3.0
    elif points >= 60:
        grade = 3.5
    elif points >= 70:
        grade = 4.0
    elif points >= 80:
        grade = 4.5
    elif points >= 90:
        grade = 5.0
    else:
        grade = 2.0

    print(f'Points: {points}, grade: {grade}')
    ```

## 8. Multiple Conditions – Debugging (4 pts)

1. The program is a simple calculator. It contains **three** errors. Run the program for the data given below, find all errors and fix them.

    * 8, 2, `*` → should print `8 * 2 = 16`
    * 8, 0, `/` → should print `Division by zero!`
    * 8, 2, `x` → should print `Wrong symbol!` (and nothing else, no error)

    ```python
    ###
    # Simple calculator
    #
    number1 = input('Enter first number: ')
    number2 = int(input('Enter second number: '))
    operator = input('Enter operator (+,-,*,/): ')

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2
    else:
        print('Wrong symbol!')

    print(f'{number1} {operator} {number2} = {result}')
    ```

## 9. Logical Operators (3 pts)

1. A student receives a scholarship if the student has an average grade of at least 4.5 and has not failed any exam. A student who is a member of the university sports team receives the scholarship already with an average of at least 4.0 (but also without failed exams). Write a program that reads the data from the keyboard and prints True or False. Use logical type variables: `failed_exam` and `athlete`. Sample result:

    ```
    Average grade: 4.2
    Failed any exam? (y/n): n
    University sports team member? (y/n): y
    Scholarship: True
    ```

    > Hint: you do not need an if statement to create a logical variable. What is the value of `answer == 'y'`?

## 10. Conditional Iteration (4 pts)

1. The following program counts how many numbers from 1 to N are divisible by 3 or by 7. Modify the program. Replace the 'for' statement with a 'while' statement. Check your program: for N = 20 the result is 8.

    ```python
    ###
    # Counts numbers from 1 to N that are divisible by 3 or by 7
    #
    N = int(input('Enter N: '))
    count = 0

    for number in range(1, N + 1):
        if number % 3 == 0 or number % 7 == 0:
            count += 1

    print(f'Numbers divisible by 3 or 7 in <1,{N}>: {count}')
    ```

    Then, answer the question: what happens if you put the statement that increases the loop variable **inside** the if block? Explain why.

## 11. Iteration Over a Sequence (4 pts)

1. Without using a computer, write down what the programs print. Then, check your answers.

    ```python
    for i in range(0, 3):
        print(i, end=' ')
    ```

    ```python
    for i in range(1, 10, 3):
        print(i, end=' ')
    ```

    ```python
    for i in range(10, 0, -3):
        print(i, end=' ')
    ```

    ```python
    for i in range(5, 5):
        print('Hello')
    print('End')
    ```

    ```python
    x = 1
    while x < 50:
        x = x * 3
    print(x)
    ```

    Additionally, answer the question: how many times will the following loop ask for a PIN if the user always enters a wrong one? Why?

    ```python
    for attempt in range(0, 3):
        pin = input('Enter PIN: ')
    ```

## 12. Practice Makes Perfect – Sequences (4 pts)

1. Write a program that prints the first fifteen terms of the Lucas sequence and the sum of these terms. The sequence is defined as follows: the first term is equal to 2, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result:

    ```
    2 1 3 4 7 11 18 29 47 76 123 199 322 521 843
    Sum: 2206
    ```

    > Hint: you need to remember only two previous terms. Check on paper what happens to both variables in each step of the loop.

## 13. Practice Makes Perfect – Number Systems (4 pts)

1. Write a program that converts a decimal number into an octal number (base 8). Do not use the oct() function. To convert a decimal number to octal, follow these steps:

    1. Read a decimal number from the keyboard.
    1. Divide the number by 8 and note the remainder.
    1. Divide the quotient obtained by 8 and note the remainder.
    1. Repeat the same process till we get 0 as the quotient.
    1. Write the values of all the remainders starting from the bottom to the top. That will be the required octal number.

    Sample result:

    ```
    Enter a decimal number: 100
    Octal number: 144
    ```

    Then, check your result using the oct() function.

## 14. Practice Makes Perfect – Time Format (4 pts)

1. Write a program that allows you to convert time in 12-hour format to 24-hour format. The time in 12-hour format (h:mmam or h:mmpm) is read from the keyboard. Do not use 12 or 24 if statements – try to use as few conditions as possible. Sample results:

    ```
    Enter time (12-hour format): 4:32pm
    Time in 24-hour format: 16:32
    ```

    ```
    Enter time (12-hour format): 12:05am
    Time in 24-hour format: 0:05
    ```

    ```
    Enter time (12-hour format): 12:40pm
    Time in 24-hour format: 12:40
    ```

    > Hint: the last two characters of the string tell you whether it is am or pm. What is the result of 12 % 12?

## 15. Practice Makes Perfect – Patterns (bonus, not included in the total)

1. Write a program that reads a number n from the keyboard and prints a hollow square made of stars with the side n. Sample result:

    ```
    Enter n: 5
    * * * * *
    *       *
    *       *
    *       *
    * * * * *
    ```

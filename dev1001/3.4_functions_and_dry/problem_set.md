**CREATE Phase: Homework Problem Set**

**Problem 1: Simple Temperature Converter**
*   **Task:** Write a Python script that includes two functions:
    1.  `celsius_to_fahrenheit(celsius)`: Takes a temperature in Celsius (float) and returns the equivalent in Fahrenheit (float). Formula: `F = C * 9/5 + 32`.
    2.  `fahrenheit_to_celsius(fahrenheit)`: Takes a temperature in Fahrenheit (float) and returns the equivalent in Celsius (float). Formula: `C = (F - 32) * 5/9`.
*   **Main Script:**
    *   Prompt the user to enter a temperature and its unit (C or F).
    *   Call the appropriate function to convert it.
    *   Print the original and converted temperatures neatly.
    *   Example: "25.0°C is 77.0°F" or "68.0°F is 20.0°C".

**MY ANSWER:**

    def celsius_to_farenheit():
    c_temp = input("What is the temperature in celsius today? e.g. 10.0C\nEnter Temp: ").strip('C')
    if True:
        celsius = float(c_temp) * 9/5 + 32
        print(f"{c_temp}°C is {celsius}°F")
    return celsius

def farenheit_to_celsius():
    f_temp = input("What is the temperature in farenheit today? e.g. 10.0\nEnter Temp: ").strip('F')
    if True:
        farenheit = (float(f_temp) - 32) * 5/9
        print(f"{f_temp}°F is {farenheit}°C")
    return farenheit

**ALTERNATIVE**

    def celsius_to_farenheit(celsius):
        return celsius * 9/5 + 32

    converted_temperature = celsius_to_farenheit(float(input("What is the temperature in celsius today? e.g. 10.0C\nEnter Temp: ").strip('C')))

    print(f"That is {converted_temperature}°F")

    - Problem with this is getting the user's input into the print

**Problem 2: Basic Library Book Checkout Message**
*   **Task:** Create a function `generate_checkout_message(book_title, member_name, due_days=14)`.
    *   `book_title` (string): The title of the book.
    *   `member_name` (string): The name of the library member.
    *   `due_days` (int, optional): Number of days until the book is due. Defaults to 14 days.
*   The function should return a formatted string like:
    `"Dear [member_name], thank you for checking out '[book_title]'. It is due back in [due_days] days. Happy reading!"`
*   **Main Script:**
    *   Call this function at least three times with different inputs to demonstrate:
        *   Using only positional arguments (and the default `due_days`).
        *   Using keyword arguments for all parameters.
        *   Using a mix and overriding the `due_days` (e.g., for a short-loan item, `due_days=3`).
    *   Print the returned message for each call.

***MY ANSWER**

    book_title1 = 'Charlie and the Chocolate Factory'
    member_name1 = 'Roald Dahl'

    book_title2 = 'The Prince'
    member_name2 = 'Beta Chad'

    book_title3 = 'Hungry Hungry Catepillar'
    member_name3 = 'Kosmo Cat'

    def generate_checkout_message(book_title, member_name, due_days=14):
            print(f"Dear {member_name}, thank you for checking out {book_title}.  It is due back in {due_days} days. Happy reading!")


    member1 = generate_checkout_message(book_title1, member_name1)

    member2 = generate_checkout_message(book_title=book_title2, member_name=member_name2, due_days=10)

    member3 = generate_checkout_message(book_title3, member_name3, due_days='Now you fat shit. Cough it up in 0')

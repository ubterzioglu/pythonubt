# 50 PYTHON APPS: ZERO TO HERO
# Progress from beginner to advanced with these practical examples

# ============================================
# LEVEL 1: ABSOLUTE BEGINNER (Apps 1-10)
# ============================================

# 1. Hello World
print("Hello, World!")

# 2. Personal Greeting
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to Python!")

# 3. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")

# 4. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# 5. Even or Odd Checker
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 6. Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print(f"You are {age} years old")

# 7. Simple Interest Calculator
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time (years): "))
interest = (principal * rate * time) / 100
print(f"Simple Interest: ${interest:.2f}")

# 8. Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 9. Sum of N Numbers
n = int(input("How many numbers to sum? "))
total = sum(range(1, n + 1))
print(f"Sum of first {n} numbers: {total}")

# 10. Factorial Calculator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


# ============================================
# LEVEL 2: BEGINNER (Apps 11-20)
# ============================================

# 11. Grade Calculator
score = float(input("Enter your score (0-100): "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# 12. Vowel Counter
text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {count}")

# 13. Palindrome Checker
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome")

# 14. List Operations
numbers = [10, 25, 30, 15, 45, 20]
print(f"List: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# 15. Password Validator
password = input("Enter a password: ")
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
is_long = len(password) >= 8

if has_upper and has_lower and has_digit and is_long:
    print("Strong password!")
else:
    print("Weak password. Include uppercase, lowercase, digits, and 8+ characters")

# 16. Shopping List Manager
shopping_list = []
while True:
    action = input("Add item, View list, or Quit (a/v/q)? ").lower()
    if action == 'a':
        item = input("Enter item: ")
        shopping_list.append(item)
    elif action == 'v':
        print("Shopping List:", shopping_list)
    elif action == 'q':
        break

# 17. Number Guessing Game
import random
secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed in {attempts} attempts")
        break

# 18. Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Word count: {len(words)}")
print(f"Character count: {len(sentence)}")

# 19. Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 20. Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")


# ============================================
# LEVEL 3: INTERMEDIATE (Apps 21-35)
# ============================================

# 21. Contact Book
contacts = {}
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# 22. BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 23. Rock Paper Scissors
import random
choices = ['rock', 'paper', 'scissors']
user = input("Choose (rock/paper/scissors): ").lower()
computer = random.choice(choices)
print(f"Computer chose: {computer}")
if user == computer:
    print("Tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")

# 24. Currency Converter
rates = {'USD': 1, 'EUR': 0.85, 'GBP': 0.73, 'JPY': 110}
amount = float(input("Enter amount in USD: "))
currency = input("Convert to (EUR/GBP/JPY): ").upper()
converted = amount * rates.get(currency, 1)
print(f"${amount} USD = {converted:.2f} {currency}")

# 25. Todo List with File Storage
import json
def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

# 26. Word Frequency Counter
text = input("Enter text: ")
words = text.lower().split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")

# 27. Password Generator
import random
import string
length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print(f"Generated password: {password}")

# 28. Simple Text Encryptor (Caesar Cipher)
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
encrypted = caesar_cipher(text, shift)
print(f"Encrypted: {encrypted}")

# 29. Dice Roller Simulator
import random
def roll_dice(sides=6, count=1):
    return [random.randint(1, sides) for _ in range(count)]

sides = int(input("Number of sides: "))
count = int(input("Number of dice: "))
results = roll_dice(sides, count)
print(f"Results: {results}, Total: {sum(results)}")

# 30. Simple Quiz Game
questions = [
    {"question": "What is 2+2?", "answer": "4"},
    {"question": "Capital of France?", "answer": "paris"},
    {"question": "Color of sky?", "answer": "blue"}
]
score = 0
for q in questions:
    answer = input(q["question"] + " ")
    if answer.lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer was {q['answer']}")
print(f"Final score: {score}/{len(questions)}")

# 31. File Search Tool
import os
def search_files(directory, extension):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matches.append(os.path.join(root, file))
    return matches

# 32. Simple Calculator with Functions
def calculator():
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error"
    }
    num1 = float(input("First number: "))
    op = input("Operation (+,-,*,/): ")
    num2 = float(input("Second number: "))
    result = operations[op](num1, num2)
    print(f"Result: {result}")

# 33. Email Validator
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

email = input("Enter email: ")
print("Valid email" if is_valid_email(email) else "Invalid email")

# 34. URL Shortener (Simple Dictionary-based)
url_mapping = {}
import random
import string
def shorten_url(long_url):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_mapping[short_code] = long_url
    return f"short.url/{short_code}"

# 35. Markdown to HTML Converter (Basic)
def markdown_to_html(text):
    # Headers
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


# ============================================
# LEVEL 4: ADVANCED (Apps 36-50)
# ============================================

# 36. Web Scraper (Basic)
# Note: Requires 'requests' and 'beautifulsoup4' libraries
"""
import requests
from bs4 import BeautifulSoup
url = input("Enter URL to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('h1')
for title in titles:
    print(title.get_text())
"""

# 37. REST API Client
"""
import requests
def get_user_data(user_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    return response.json()
"""

# 38. SQLite Database Manager
import sqlite3
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# 39. Log File Analyzer
def analyze_logs(filename):
    stats = {'errors': 0, 'warnings': 0, 'info': 0}
    with open(filename, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                stats['errors'] += 1
            elif 'WARNING' in line:
                stats['warnings'] += 1
            elif 'INFO' in line:
                stats['info'] += 1
    return stats

# 40. CSV Data Processor
import csv
def process_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# 41. JSON API Server (Flask)
"""
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from API!'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({'received': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
"""

# 42. Image Downloader
"""
import requests
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")
"""

# 43. PDF Generator
"""
from reportlab.pdfgen import canvas
def create_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()
"""

# 44. Command Line Argument Parser
import argparse
def create_cli():
    parser = argparse.ArgumentParser(description='Process some data')
    parser.add_argument('--input', help='Input file')
    parser.add_argument('--output', help='Output file')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()
    return args

# 45. Automated Email Sender
"""
import smtplib
from email.mime.text import MIMEText
def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'password')
    server.send_message(msg)
    server.quit()
"""

# 46. File Backup System
import shutil
import datetime
def backup_file(source, backup_dir):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{backup_dir}/backup_{timestamp}_{os.path.basename(source)}"
    shutil.copy2(source, backup_name)
    print(f"Backed up to {backup_name}")

# 47. Data Visualization
"""
import matplotlib.pyplot as plt
def create_chart(data, labels):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data)
    plt.title('Data Visualization')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('chart.png')
    plt.show()
"""

# 48. Multi-threaded Downloader
import threading
def download_worker(url, filename):
    # Simulated download
    print(f"Downloading {filename} from {url}")

def multi_download(urls):
    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_worker, args=(url, f"file_{i}.txt"))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# 49. Expense Tracker with Analytics
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, amount, category, description):
        self.expenses.append({
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.datetime.now()
        })
    
    def get_total(self):
        return sum(e['amount'] for e in self.expenses)
    
    def get_by_category(self, category):
        return [e for e in self.expenses if e['category'] == category]
    
    def get_statistics(self):
        categories = {}
        for expense in self.expenses:
            cat = expense['category']
            categories[cat] = categories.get(cat, 0) + expense['amount']
        return categories

# 50. Machine Learning Predictor (Simple)
"""
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict(model, X_new):
    return model.predict(X_new)

# Example usage:
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = train_model(X, y)
prediction = predict(model, np.array([[6]]))
print(f"Prediction for 6: {prediction}")
"""

# ============================================
# NOTES:
# - Apps marked with triple quotes need external libraries
# - Install libraries with: pip install requests beautifulsoup4 flask matplotlib scikit-learn reportlab
# - Some apps are simplified versions - expand them for production use
# - Practice by modifying and combining these examples
# ============================================
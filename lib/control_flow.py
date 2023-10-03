#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" or username == "ADMIN":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # your code here
    response = None
    if temperature < 40:
        return "brisk"
    elif temperature >=40 and temperature <=65:
        return "a little chilly"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"
    
# function howsTheWeather(temperature) {
#   let response;
#   if (temperature < 40) {
#     response = "brisk";
#   } else if (temperature >= 40 && temperature <= 65) {
#     response = "a little chilly";
#   } else if (temperature > 85) {
#     response = "too dang hot";
#   } else {
#     response = "perfect";
#   }
#   return `It's ${response} out there!`;
# }
def fizzbuzz(num):
    # your code here
    if  num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "num"



def calculator(operation, num1, num2):
    # your code here
    if operation ==  "+":
         return num1 + num2
    elif operation ==  "-":
         return num1 - num2
    elif operation ==  "*":
         return num1 * num2
    elif operation ==  "/":
         return num1 / num2
    else:
        print("Invalid operation!")
    


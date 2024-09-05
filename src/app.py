# src/app.py
from src.utils import get_time_of_day

def greet(name):
    time_of_day = get_time_of_day()
    return f"Good {time_of_day}, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

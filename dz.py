import threading
import requests
from random import randint

def get_data(i):
    response = randint(1,100)
    with open(f"new_{i}", "w") as file:
        file.write(str(response))

if __name__ == "__main__":
    for i in range(1, 101):
        t = threading.Thread(target=get_data, args=(i,))
        t.start()
from bs4 import BeautifulSoup
import requests

def drink():
    print("Enter a URL.")
    url = input()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print("Here is what i fetched for this website: \n" + soup + "Starting AI...")
from bs4 import BeautifulSoup
from keras.layers import Dense
import tensorflow as tf
import requests

def drink():
    
    print("Enter a URL.")
    url = input()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print("Here is what i fetched for this website: \n" + soup + "Starting AI...")

def ai():
    tensor = ([[5, 1, 2, 6], [4, 9, 3, 5]])
    oli = tf.keras.Sequential([tf.keras.layers.Dense(units=64, activation="relu", input_shape=tensor.shape)
                               tf.keras.layers.Dense(units=64, activation="relu")
                               tf.keras,layers.Dense(units=1)])
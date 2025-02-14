#!/usr/bin/python3  

import os  

#prompts for input 
FAV_ALBUM = input("What is your favorite album? ")
FAV_ANIMAL = input("What is your favorite animal? ")
FAV_CITY = input("What is your favorite city? ")

#store inputs as vars
os.environ["FAV_ALBUM"] = FAV_ALBUM
os.environ["FAV_ANIMAL"] = FAV_ANIMAL
os.environ["FAV_CITY"] = FAV_CITY

#print response
print("\nStored Environment Variables:")
print(os.getenv("FAV_ALBUM"))
print(os.getenv("FAV_ANIMAL"))
print(os.getenv("FAV_CITY"))


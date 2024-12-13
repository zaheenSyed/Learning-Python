## this is the main executable file for the udemy project

import sys

def main():
    print("Hello World")
    print(sys.path)

if __name__=="__main__":
    main()
    name= input("enter your name:")
    print("Hello", name)

    age= int(input("enter your age:"))
    print("You will be 50 years old in the year", 2020+(100-age))
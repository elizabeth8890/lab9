#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:26:04 2024

@author: elizabethkallman
"""
def encode(password):
    list_password = list(password) 
    password2 = []
    for i in range(len(list_password)):
        i_tmp = str(int(list_password[i]) + 3)
        password2.append(i_tmp)
        x = "".join(password2)
    
    return(x)

def decode(password):
    pass

def main():
    
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")  
        my_option = input("\nPlease enter an option: ")
        if my_option == 1:
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif my_option == 2:
            pass
        elif my_option == 3:
            break

if __name__ == "__main__":
    main()

        
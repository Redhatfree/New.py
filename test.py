# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:36:34 2025

@author: Rouzbeh
"""
import pandas as pd
df = pd.read_csv(r'C:\Users\Rouzbeh\Desktop\sample_ecommerce_data.csv')

# Fill numeric columns with their mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("DataFrame After Replacing Null Values with Mean:")
print(df.isnull().sum())
print(df.head())


def print_big_rouzbeh():
    big_letters = {
        'R': [
            "RRRRR ",
            "R   R ",
            "RRRRR ",
            "R  R  ",
            "R   R "
        ],
        'O': [
            " OOO  ",
            "O   O ",
            "O   O ",
            "O   O ",
            " OOO  "
        ],
        'U': [
            "U   U ",
            "U   U ",
            "U   U ",
            "U   U ",
            " UUU  "
        ],
        'Z': [
            "ZZZZZ ",
            "   Z  ",
            "  Z   ",
            " Z    ",
            "ZZZZZ "
        ],
        'B': [
            "BBBB  ",
            "B   B ",
            "BBBB  ",
            "B   B ",
            "BBBB  "
        ],
        'E': [
            "EEEEE ",
            "E     ",
            "EEE   ",
            "E     ",
            "EEEEE "
        ],
        'H': [
            "H   H ",
            "H   H ",
            "HHHHH ",
            "H   H ",
            "H   H "
        ]
    }

    name = "ROUZBEH"
    for i in range(5):  # 5 lines tall
        line = ""
        for letter in name:
            line += big_letters[letter][i] + "  "
        print(line)

# Run it
print_big_rouzbeh()


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:48:27 2023

@author: Amir_Fazil
"""


def playfair_converter(text):
    text = text.upper()
    # text="datasecurityjournal"
    new_text = text
    array = list(text)
    for i in range(0, len(array)):
        if (array[i] == 'J'):
            array[i] = 'I'
            new_text = new_text.replace('J', 'I')

    return array, new_text

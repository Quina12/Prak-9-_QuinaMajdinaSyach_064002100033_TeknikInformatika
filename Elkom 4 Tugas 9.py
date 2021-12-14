# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:14:34 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

def hitung_string():
    jumlah = 0
    List = ['Quina', '678', '1010101', '5abcd5', 'SyachS']
    print("\nList string: ", List)
    for c in List:
        if c[0] == c[len(c) -1]:
            print("-", c)
            jumlah += 1
    print("Terdapat", (jumlah), "string yang memenuhi kriteria")       
hitung_string()
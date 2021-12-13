# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:23:00 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

def hasil_kali_list():
    jumlah = 1
    List = [9, -19, 67]
    print("\nList: ", List)
    for i in List:
        jumlah *= i
    print("Hasil kali value: ", jumlah)
hasil_kali_list()
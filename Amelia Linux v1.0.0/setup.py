import os
import sys
def installation():
    os.system('pip3 install pyfiglet')
    os.system('pip3 install colorama')
    os.system('pip install rsap')
print("""
      ___           ___           ___           ___                   ___
     /\  \         /\__\         /\  \         /\__\      ___        /\  \  
    /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::\  \ 
   /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:/\:\  \ 
  /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/  /       /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\ 
 \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/ \:\  \    /\/:/  /    \/__\:\/:/  /
      \::/  /        /:/  /   \:\ \:\__\    \:\  \   \::/__/          \::/  /
      /:/  /        /:/  /     \:\ \/__/     \:\  \   \:\__\          /:/  /
     /:/  /        /:/  /       \:\__\        \:\__\   \/__/         /:/  /
     \/__/         \/__/         \/__/         \/__/                 \/__/

""")

print("\n\t [sys] amelia > Welcome to Amelia ChatBot Setup.")
print("\n\t [sys] amelia > Press Enter to start installation")
print("\n\t\t Developed by: Kavin Jindal and PGamerX")
print("\n\t\t Early Access Version for Linux (1.0.0) ")

installation()
print("\n\t\t [sys] amelia > Installation complete, running the application")
os.system('python3 main.py')

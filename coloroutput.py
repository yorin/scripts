#!/usr/bin/python

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')

print('\033[31m' + 'some text')
print('\033[95m' + 'some text')
print('\033[94m' + 'some text')
print('\033[92m' + 'some text')
print('\033[93m' + 'some text')
print('\033[91m' + 'some text')
print('\033[0m'  + 'some text')
print('\033[1m'  + 'some text')
print('\033[4m'  + 'some text')
#print('\033[30m' + 'some text')

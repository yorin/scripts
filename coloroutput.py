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
#print('\033[30m' + 'some text') #turns text to black

#http://www.siafoo.net/snippet/88
print '\033[1;30mGray like Ghost\033[1;m'
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;32mGreen like Grass\033[1;m'
print '\033[1;33mYellow like Yolk\033[1;m'
print '\033[1;34mBlue like Blood\033[1;m'
print '\033[1;35mMagenta like Mimosa\033[1;m'
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;37mWhite like Whipped Cream\033[1;m'
print '\033[1;38mCrimson like Chianti\033[1;m'
print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
print '\033[1;43mHighlighted Brown like Bear\033[1;m'
print '\033[1;44mHighlighted Blue like Blood\033[1;m'
print '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
print '\033[1;47mHighlighted Gray like Ghost\033[1;m'
print '\033[1;48mHighlighted Crimson like Chianti\033[1;m'

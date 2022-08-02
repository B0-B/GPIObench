#!/usr/bin/env python3
from os import path

'''
Flips the persistent stop switch to true.
'''

def stop ():
    with open(path.dirname(__file__) + '/tools/switch.txt', 'w+') as f:
        f.write('1')

if __name__ == '__main__':
    stop()
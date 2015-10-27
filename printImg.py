#!/usr/bin/env python

import sys

def printData(array):
    for byte in array:
        print byte

def getHeaderSize(array):
    result = 417
    for i in range(len(array)):
        if array[i] == 255:
            if array[i + 1] == 218:
                result = i + 2
                break
    return result

def main():
    if len(sys.argv) != 2:
        print 'Usage: printImg.py [image file]'
        sys.exit()
    try:
        with open(sys.argv[1], 'rb') as f:
            imgData = bytearray(f.read())
            headerLen = getHeaderSize(imgData)
            #print('header len: %d' % headerLen)
            printData(imgData[:headerLen])
    except IOError:
        print 'Error: file does not exist'

if __name__ == '__main__':
    main()

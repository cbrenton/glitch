#!/usr/bin/env python

from PIL import Image
import math, random, sys

def main():
    imgBytes = None
    filename = None
    iterations = None
    manualPos = None
    manualVal = None
    changed = None
    
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print('Usage: glitch [image file] [iterations]')
        sys.exit(1)
    filename = sys.argv[1]

    try:
        with open(filename, 'rb') as f:
            imgBytes = bytearray(f.read())
    except:
        print('Error: %s does not exist' % filename)
        return
        sys.exit(1)

    headerLen = getHeaderSize(imgBytes)

    #for i in range(10):
    imgBytesCopy = bytearray(imgBytes)
    if len(sys.argv) == 2:
        iterations = random.randint(1, 50)
        seed = random.random()
        amount = random.random()
        #print('iter: %d\nseed: %d\namount: %f' % (iterations, seed, amount))
        #changed = glitchArray(imgBytesCopy, headerLen, iterations)
        for i in range(iterations):
            glitchJpegBytes(imgBytesCopy, headerLen, seed, amount, i, iterations)
    if len(sys.argv) == 3:
        iterations = int(sys.argv[2])
        seed = random.random()
        amount = random.random()
        print('glitch')
        #changed = glitchArray(imgBytesCopy, headerLen, iterations)
        for i in range(iterations):
            glitchJpegBytes(imgBytesCopy, headerLen, seed, amount, i, iterations)
    if len(sys.argv) == 4:
        manualPos = int(sys.argv[2])
        manualVal = int(sys.argv[3])
        print('%d %d (%d)' % (manualPos, manualVal, imgBytesCopy[manualPos]))
        setByte(imgBytesCopy, manualPos, manualVal)

    with open('out.jpg', 'wb') as out:
        out.write(imgBytesCopy)

    outImg = Image.open('out.jpg')
    outImg.show()

def getHeaderSize(array):
    result = 417
    for i in range(len(array)):
        if array[i] == 255:
            if array[i + 1] == 218:
                result = i + 2
                break
    return result

def setByte(array, pos, val):
    if array[pos] == 0:
        return
    array[pos] = val

def glitchJpegBytes(byteArray, headerLen, seed, amount, i, iter):
    amount = random.random()
    maxIndex = len(byteArray) - headerLen - 4
    delta = maxIndex / iter
    pxMin = int(delta * i)
    pxI = int(pxMin + delta * seed)
    if pxI > maxIndex:
        pxI = maxIndex;
    index = int(math.floor(headerLen + pxI))
    newVal = int(math.floor(amount * 256))
    print('array[%d] = %d (%d)' % (index, newVal, byteArray[index]))
    setByte(byteArray, index, newVal)
 
if __name__ == '__main__':
    main()

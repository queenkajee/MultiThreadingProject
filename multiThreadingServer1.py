# import socket programming library
import socket

# import thread module
from threading import Thread
import concurrent.futures
from multiprocessing.pool import ThreadPool

#inport date module
from datetime import datetime

#import string and random for promocode
import string
import random


def promo1():
    codeName1 = random.choice(string.ascii_letters)
    codeName2 = random.choice(string.ascii_letters)
    codeName3 = random.choice(string.ascii_letters)
    codeName4 = random.choice(string.ascii_letters)
    promoLetter = codeName1 + codeName2+codeName3+codeName4
    return promoLetter

def promo2():
    data1 = []
    data2 = []
    data3 = []

    for i in range(random.randint(0, 9)):
        data1.append(random.randint(0, 9))
    for i in range(random.randint(0, 9)):
        data2.append(random.randint(0, 9))
    for i in range(random.randint(0, 9)):
        data3.append(random.randint(0, 9))

    first = 0
    second = 0
    third = 0
    for i in data1 :
        first += int(i)
        first = first%10 + first//10
    for i in data2 :
        second += int(i)
        second = second%10 + second//10
    for i in data3 :
        third += int(i)
        third = third%10 + third//10

    promoNum = str(first) + str(second)+str(third)
    return promoNum




def Main():
    proMoList = []
    #open the file.txt in write mode.
    for line in open('proMO.txt','r').readlines():
        proMoList.append(line.strip())

    promocode=""
    host = ""
    # reverse a port on your computer
	# can be anything
    port = 2001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")


    # establish connection with client
    c, addr = s.accept()

    print('Connected to :', addr[0], ':', addr[1])

    while True:
        #make thread return result by using thread pool
    	with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(promo1)
            future2 = executor.submit(promo2)
            return_value1 = future1.result()
            return_value2 = future2.result()
            promocode = return_value1 + return_value2
            if promocode not in proMoList:
                promoTxTObj = open('proMO.txt', 'w')
                promoTxTObj.write(promocode)
                break

    code = bytes(promocode, 'ascii')

    c.send(code)
    s.close()


if __name__ == '__main__':
	Main()

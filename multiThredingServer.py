# import socket programming library
import socket

# import thread module
from threading import Thread
import concurrent.futures
from multiprocessing.pool import ThreadPool

#inport date module
from datetime import datetime

#modify Human data
def people1(date):
	first = 0
	for i in date[0:8] :
		first += int(i)
		first = first%10 + first//10
	return first

def people2(date):
	second = 0
	for i in date[8:16] :
		second += int(i)
		second = second%10 + second//10
	return second

def suggestFood(date):
	sugFood=""
	food={"fire":"""Recommended foods for the fire day include bitter foods, grains,\n
	vegetables, dark leafy greens, beans and seeds. These foods tend to keep the fire at bay,\n
	avoiding an overabundance.\n
	Foods to avoid include chocolate, salt, meats, stimulants and hot spices.""",
	"wood":"""Recommended foods for the wood day include anything sour, and green foods with stalks.\n
	Make sure to exclude alcohol, processed foods, high fat foods and most dairy,\n
	as these foods can restrict the free flow of energy and blood,\n
	while wreaking havoc on the function of the wood element.""",
	"water":"""Recommended foods for the water element day include pure water (not what is contained in juices, coffee, etc.)\n
	, blue, purple and black foods, root vegetables and seaweeds and seafood.\n
	Foods to avoid include sugars, alcohol, caffeinated drinks,\n
	frozen and excessively raw foods.""",
	"earth":"""Recommended foods for the earth element day include root vegetables,\n
	leafy greens and light proteins such as legumes and fish.\n
	Foods to avoid include refined carbohydrates, dairy, iced drinks and processed foods as they gunk up the digestive system\n
	and overtax the spleen and stomach.""",
	"metal":"""Recommended foodsfor the metal element day include those that have a dispersing effect and promote energy circulation.\n
	Foods sour in nature are best for this body type.\n
	Also foods high in minerals like leafy greens and vegetables are good choices.\n
	Foods to avoid include dairy, red meat and bitter foods."""}
	dateNow = str(datetime.today().strftime('%d%m%Y'))
	dateElement=dateNow[1]
	if dateElement in '1':
		sugFood = food["water"]
	elif dateElement in '258':
		sugFood = food["earth"]
	elif dateElement in '34':
		sugFood = food["metal"]
	else:
		sugFood = food["fire"]

	return bytes(sugFood, 'ascii')

def goodDay(date):
	txtSend="\n"
	personDate1 = 0
	personDate2 = 0
	datePow = 0

	#make thread return result by using thread pool
	with concurrent.futures.ThreadPoolExecutor() as executor:
	    future1 = executor.submit(people1, date)
	    future2 = executor.submit(people2,date)
	    return_value1 = future1.result()
	    return_value2 = future2.result()
	dateNow = str(datetime.today().strftime('%d%m%Y'))
	for i in dateNow[0:8]:
		datePow += int(i)
	score1 = return_value1 - datePow
	score2 = return_value2 - datePow
	if score1 > 0 :
		txtSend = "Today is a good day for you" + txtSend
	elif score1 == 0:
		txtSend = "Today is a nor good or bad day for you" + txtSend
	else:
		txtSend = "Today is a not your day, " + txtSend
	if score2 > 0 :
		txtSend = "Today is a good day for yor parter " + txtSend
	elif score2 == 0:
		txtSend = "Today is a nor good or bad day for yor parter, " + txtSend
	else:
		txtSend = "Today is a not yor parter's day, " + txtSend
	#return today's advise by send them
	return bytes(txtSend, 'ascii')



def Horar(date) :
	#make thread return result by using thread pool
	with concurrent.futures.ThreadPoolExecutor() as executor:
	    future1 = executor.submit(people1, date)
	    future2 = executor.submit(people2,date)
	    return_value1 = future1.result()
	    return_value2 = future2.result()
	sumValue = return_value1 + return_value2

	if(sumValue)>10 :
		data = b"Good relationship :D"
	elif(sumValue)>5 :
		data = b"Normal relationship"
	else:
		data = b"not quite good relationship ;-;"

	return data



# thread function
def threaded1(c,data):

	#use horar
	data = Horar(data)
	# send back string to client
	c.send(data)


def threaded2(c,data):
	#use goodDay
	data = goodDay(data)
	# send back string to client
	c.send(data)

def threaded3(c,data):

	#use suggestFood
	data = suggestFood(data)
	# send back string to client
	c.send(data)

def Main():
	host = ""

	# reverse a port on your computer
	# can be anything
	port = 2000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	s.listen(5)
	print("socket is listening")


	# establish connection with client
	c, addr = s.accept()

	print('Connected to :', addr[0], ':', addr[1])

	# data received from client
	data = c.recv(1024)
	#decode data
	date = data.decode('ascii')
	# Start a new thread and return its identifier
	t1 = Thread(target=threaded1(c,data))
	t2 = Thread(target=threaded2(c,data))
	t3 = Thread(target=threaded3(c,data))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	s.close()


if __name__ == '__main__':
	Main()

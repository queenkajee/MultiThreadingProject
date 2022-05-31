# import socket programming library
import socket

# import thread module
from threading import Thread

#inport date module
from datetime import datetime

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

def goodDay(date,promoCode):
	txtSend=""
	personDate1 = 0
	personDate2 = 0
	datePow = 0
	for i in date[0:8]:
		personDate1 += int(i)
	for i in date[9:-1]:
		personDate2 += int(i)
	dateNow = str(datetime.today().strftime('%d%m%Y'))
	for i in dateNow[0:8]:
		datePow += int(i)
	score1 = personDate1 - datePow
	score2 = personDate2 - datePow
	if score1 > 0 :
		txtSend = txtSend+"Today is a good day for you\n"
	elif score1 == 0:
		txtSend = txtSend+"Today is a nor good or bad day for you\n"
	else:
		txtSend = txtSend+"Today is a not your day, \n"
	if promoCode in 'a':
		if score2 > 0 :
			txtSend =  txtSend+"Today is a good day for yor parter "
		elif score2 == 0:
			txtSend = txtSend+"Today is a nor good or bad day for yor parter, "
		else:
			txtSend = txtSend+"Today is a not yor parter's day, "
	else:
		txtSend = "for your parter : [You have no access to this please enter promoCode]"

	return bytes(txtSend, 'ascii')





def Horar(date) :
	first = 0
	second = 0
	for i in date[0:8] :
		first += int(i)
		first = first%10 + first//10

	for i in date[8:16] :
		second += int(i)
		second = second%10 + second//10
	sumValue = first + second
	print(sumValue)

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


def threaded2(c,data,promoCode):
	#use goodDay
	data = goodDay(data,promoCode)
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
	port = 10045
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
	promoCode = c.recv(1024)
	#decode data
	date = data.decode('ascii')
	promoCode = promoCode.decode('ascii')

	# Start a new thread and return its identifier
	t1 = Thread(target=threaded1(c,data))
	t2 = Thread(target=threaded2(c,data,promoCode))
	t3 = Thread(target=threaded3(c,data))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()


if __name__ == '__main__':
	Main()

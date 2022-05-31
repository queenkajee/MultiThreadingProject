# Import socket module
import socket
#Import GUI module
import tkinter as tk



app = tk.Tk()

def serverTCP2():
	# local host IP '192.168.0.101'
	host = '192.168.0.101'

	# Define the port on which you want to connect
	port = 10048
	s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# connect to server on local computer
	s1.connect((host,port))
	# message received from server
	promoCode = s1.recv(1024)
	# print the received message
	serverTextPromo =promoCode.decode('ascii')
	resultsShowPromo = tk.Label(app,text=serverTextPromo)
	resultsShowPromo.pack()

def serverTCP1(person):
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 10048
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# connect to server on local computer
	s.connect((host,port))
	# message you send to server
	message = person+promoCode

	# message sent to server
	s.sendall(message.encode('ascii'))

	# message received from server
	data1 = s.recv(1024)
	# print the received message
	serverText1 =data1.decode('ascii')
	resultsShow1 = tk.Label(app,text=serverText1)
	resultsShow1.pack()

	# message received from server
	data2 = s.recv(1024)
	# print the received message
	serverText2=data2.decode('ascii')
	resultsShow2 = tk.Label(app,text=serverText2)
	resultsShow2.pack()

	# message received from server
	data3 = s.recv(1024)
	# print the received message
	serverText3=data3.decode('ascii')
	resultsShow3 = tk.Label(app,text=serverText3)
	resultsShow3.pack()



	# close the connection
	s.close()
	lastRespondText = "\n\nEnd of the program"
	showTxt = tk.Label(app,text=lastRespondText)
	showTxt.pack()

def clickButton1(personData):
	print(personData)
	personData = str(personData)
	promoCode = str(promoCode)
	serverTCP1(personData)
def clickButton2()
	serverTCP2()
def Main():

	app.geometry("1000x500")
	app.title("Horo app")
	instruct1 = tk.Label(app,text="""Plase enter your birthday and then follow by your parter's birthday\n
	with this form\n0000000000000000\nfirst 8 digit please enter your birthday and follow by yourparter's birthday""")
	instruct1.pack()
	p1 = tk.Entry(app)
	p1.pack()
	instruct2 = tk.Label(app,text="""For enter Promotion code""")
	instruct2.pack()
	button1 = tk.Button(app, text="Click to proceed",command=lambda:clickButton1(p1.get()))
	button1.pack()
	button2 = tk.Button(app,text="Click to get promocode and get further info",command=lambda:clickButton2())
	app.mainloop()



if __name__ == '__main__':
	Main()

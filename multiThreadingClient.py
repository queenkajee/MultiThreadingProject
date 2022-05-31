# Import socket module
import socket
#Import GUI module
import tkinter as tk



app = tk.Tk()

def serverTCP(person,promoCode):
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 10046
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# connect to server on local computer
	s.connect((host,port))
	# message you send to server
	message = person




	# message sent to server
	s.sendall(message.encode('ascii'))
	s.sendall(promoCode.encode('ascii'))
	
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

def clickButton1(personData,promoCode):
	personData = str(personData)
	pomocode = str(promoCode)
	serverTCP(personData,promocode)
def Main():

	app.geometry("1000x500")
	app.title("Horo app")
	instruct1 = tk.Label(app,text="""Plase enter your birthday and then follow by your parter's birthday\n
	with this form\n0000000000000000\nfirst 8 digit please enter your birthday and follow by yourparter's birthday""")
	instruct.pack()
	p1 = tk.Entry()
	p1.pack()
	instruct2 = tk.Label(app,text="""For enter Promotion code""")
	p2 = tk.Entry()
	p2.pack()
	button1 = tk.Button(app, text="Click to proceed",command=lambda:clickButton1(p1.get(),p2.get()))
	button1.pack()
	app.mainloop()



if __name__ == '__main__':
	Main()

from pyCPN import PyCPN
from pyEncodeDecode import stringEncode, stringDecode
from irisMLP import IrisMLP

# Tested with Python v 3.11 and CPN Tools v 4.0.1
# Server Socket for use with ML_DevOps.cpn project

port = 8081
conn = PyCPN()
mlp = IrisMLP()


def doit():
	while True:
		word = stringDecode(conn.receive())
		if word == 'quit':
			break
		elif word == 'build':
			mlp.training()
		elif word == 'data':
			pass
			# ToDo: update the dataset with new data
		elif word == 'metrica':
			mlp.training()
			acc = mlp.getMetrica()
			conn.send(stringEncode("{}".format(acc)))		
		else:
			break
	conn.disconnect()	
	

if __name__ == "__main__":
	print("\nWait for a conection.")
	conn.accept(port)
	print('Connected to :{}'.format(conn.client_addr[0]))
	doit()
	print("Bye!\n")
import os
import socket
os.system("cls")
print "Bienvenido al programa para sacar el nombre de una PC que este conectada a tu red local y su IP\n"
print "Programa hecho por itzAlex ( https://github.com/itzAlex )\n\n"

def menu():
	print "\t\t\t\t OPCIONES DE ESTE PROGRAMA\n"
	print "\t1 - Nombre de este PC y su IP"
	print "\t2 - Nombre de otro PC (debe estar conectado a tu red local y debe ser un ordenador)"
	print "\t3 - Sacar el comando IPCONFIG de la terminal"
	print "\t4 - Salir del programa"

menu()

opcion = raw_input("\nElige la opcion con el numero de la izquierda: ")

if opcion =="1":
	ip = socket.gethostbyname(socket.gethostname())
	nombre_equipo = socket.gethostname()
	print "\nEl nombre de este equipo es: %s" %nombre_equipo 
	print "La IPv4 de este equipo es: ", ip

elif opcion =="2":

	def buscar_nombre():
		ip = raw_input("\nIndicanos la IPv4 que tiene la PC: ")
		try: 
			nombrepc = socket.gethostbyaddr(ip)
			return nombrepc[0] 
		except:
			return "** ERROR ** No se pudo resolver el nombre del Host"

	if __name__ == '__main__': 
		pcdevuelto = buscar_nombre() 
	print("\nEl nombre del PC es: %s"%(pcdevuelto))	

elif opcion =="3":
	os.system("ipconfig")

elif opcion =="4":
	print "\nGracias por utilizar mi programa :)\n"
	os.system("exit")
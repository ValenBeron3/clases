archivo=open("archivo.txt",'a')
while True:
    nombre=input("Nombre: ")
    if nombre!= "terminar":
        telefono=input("Telefono: ")
        mail=input("E-mail: ")
        archivo.write(nombre+" "+telefono+" "+mail+"\n")
    else:
        break
archivo.close()


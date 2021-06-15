def main():

    print("Opcion 1: Oracion con espacios")
    print("Opcion 2: Oracion con lineas ( - )")
    print("Opcion 3: Oracion con barra baja ( _ )")
    print("Opcion 4: Salir")
    ToConvert = input("Entre la opcion que quiere elegir (1) (2) (3) (4):  ")
    conint = int(ToConvert)
    while conint:
        if(conint == 1):
            ForConvert = input("Entre su oracion a convertir en Pascal Case : ")
            z = ""
            splt = ForConvert.split(" ")
            for i in range (0, len(splt)):
                z += splt[i].capitalize() + " "
            untd = " ".join(z.split())
            print("----------------------------")
            print("Su string en pascal case es: " + untd)
            print("----------------------------")
            conint = 0
            main()
        if(conint == 2):
            ForConvert = input("Entre su oracion a convertir en Pascal Case : ")
            z = ""
            splt = ForConvert.split("-")
            for i in range (0, len(splt)):
                z += splt[i].capitalize() + " "
            untd = "-".join(z.split())
            print("----------------------------")
            print("Su string en pascal case es: " + untd)
            print("----------------------------")
            conint = 0
            main()
        if(conint == 3):
            ForConvert = input("Entre su oracion a convertir en Pascal Case : ")
            z = ""
            splt = ForConvert.split("_")
            for i in range (0, len(splt)):
                z += splt[i].capitalize() + " "
            untd = "_".join(z.split())
            print("----------------------------")
            print("Su string en pascal case es: " + untd)
            print("----------------------------")
            conint = 0
            main()
        if(conint == 4):
            break

if __name__ == '__main__':
    main()
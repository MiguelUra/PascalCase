ToConvert = input("Entre la oracion para Pascal Case : ")
z = ""
splt = ToConvert.split(" ")
for i in range (0, len(splt)):
    z += splt[i].capitalize() + " "
untd = " ".join(z.split())
print("Su string en pascal case es: " + untd)
pw = "Kaddan"
intentos = 3
clave = input("BIENVENIDO AL SISTEMA. POR FAVOR, INSERTAR LA CLAVE DE ACCESO:")

while intentos>0:
    if pw.lower() == clave.lower():
        print("\nLA CONTRASEÑA ES CORRECTA. BIENVENIDO AL SISTEMA.")
        intentos = 0
    else:
        intentos -=1
        if intentos==0:
            print("SE HAN ACABADO TUS INTENTOS. POR FAVOR, NO VUELVA HASTA SABER LA CLAVE DE ACCESO.")
        else:
            print(f"\nLA CONTRASEÑA ES INCORRECTA. TE QUEDAN {intentos} INTENTOS.")
            clave = input("POR FAVOR, INSERTAR LA CLAVE DE ACCESO:")
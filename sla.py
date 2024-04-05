gago = True

while gago == True:
    heitor = (input("Gago é tanga?"))
    if heitor == "sim":
        print("Gênio")
    else:
        print("Dumb")
    resposta = (input("para continuar digite 'SIM'"))
    if resposta != 'SIM':
        gago == False
    
    

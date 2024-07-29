# # #Eje 1 - Nivel 1
# for i in range(1,11):
#     mi_cadena = "#"*i
#     print(mi_cadena)

# # #Eje 2 - Nivel 1
# for i in range(1,11):
#     mi_cadena = "# # # # # # # #"
#     print(mi_cadena)

# # #Eje 3 - Nivel 1
# for i in range(0,11):
#     mi_cadena = str(i) + " x " + str(i) + " = " + str(i*i)
#     print(mi_cadena)    

# #Eje 1 - Nivel 2
# resultado = 0
# for i in range(0,101):
#     valor_actual = i
#     resultado = resultado + int(valor_actual)

# print(resultado)

# #Eje 2 - Nivel 2
suma_pares = 0
suma_inpares = 0
for i in range(0,101):
    valor_actual = i
    if i % 2 == 0:
        suma_pares = suma_pares + int(i)
    else:
        suma_inpares = suma_inpares + int(i)
        
print("suma_inpares = " + str(suma_inpares))
print("suma_pares = " + str(suma_pares))

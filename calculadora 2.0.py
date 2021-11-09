num1 = float(input("Ingresa un número:"))
op = input ("ingresa un operador:")
num2 = float(input("Ingresa otro numero:"))

if op == "+":
    res = num1 + num2
    print("la suma es: "+ str(res))
elif op =="-":
    res = num1 - num2
    print ("La resta es: "+ str(res))
elif op == "*":
    res = num1 * num2
    print("La multiplicación es: " + str(res) )
elif op == "/":
    res = num1 / num2 
    print("La división es: " + str(res))
elif op == "**":
    res = num1 ** num2 
    print("La potencia es: " + str(res))
else:
    print("sistaxsis error")    


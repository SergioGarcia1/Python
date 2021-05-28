from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return  render_template("index.html")

@app.route("/user/<username>")
def hello(username):
    return "Hola {}, Como estas?"  .format(username)


@app.route("/Problema1/<int:n1>/<int:n2>")
def Problema1(n1,n2):
    if n1 > n2:
        return "El mayor es {}" .format(n1)
    elif n1==n2:
        return "Los numeros {} y {} son iguales" .format(n1,n2)
    else:
        return "El mayor es {}" .format(n2)



@app.route("/Problema2/<int:n1>/<int:n2>/<int:n3>")
def Problema2(n1,n2,n3):
    if n1 > n2 and n1>n3 :
        return "El mayor es {}" .format(n1)
    elif n2 > n1 and n2 > n3:
        return "El mayor es {}" .format(n2)
    else:
        return "El mayor es {}" .format(n3)

    
@app.route("/Problema4/<string:n1>/")
def Problema4(n1):
    if n1 == "a" or n1 == "e" or n1 == "i" or n1== "o" or n1 == "u":

        return "Es vocal {}" .format(n1)

    elif n1 == "A" or n1 == "E" or n1 == "I" or n1 == "O" or n1 == "U":
        return "Es vocal {}" .format(n1)
    else:
        return "No es vocal {}" .format(n1)


@app.route("/Problema6/<string:n1>/")
def Problema6(n1):
    resultado=""
    for letra in n1:
        resultado = letra+resultado

    return resultado


@app.route("/Problema7/<string:n1>/")
def Problema7(n1):
    resultado=""
    for letra in n1:
        resultado = letra+resultado
        
    if n1 == resultado:
        return "Es palindromo "
    else:
        return "No es palindromo " 


@app.route("/Problema9/<int:n1>/<string:n2>/")
def Problema9(n1,n2):
        return n1 * n2



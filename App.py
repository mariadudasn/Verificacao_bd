from flask import Flask, render_template, request, url_for, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect (
    host = "127.0.0.1", 
    user = "root",
    password = "",
    database = "Usuarios"
)

@app.route("/")
def login():  
    return render_template("main.html")

@app.route("/homepage")
def homepage():  
    return render_template("homepage.html")

@app.route("/login", methods=['POST'])
def verificação():
    if request.method == 'POST':
        email = request.form['Email']
        senha = request.form['Senha']

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Usuario WHERE email = %s and senha = %s", (email, senha))
        resultados = cursor.fetchall()

        if resultados: 
            cursor.close()
            conexao.close()
            return redirect(url_for('homepage'))
        else:
            return render_template('main.html', show_alert=True, alert="Usuário ou senha incorretos")
    else:
        return render_template('main.html', show_alert=True, alert="Usuário ou senha incorretos")

    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


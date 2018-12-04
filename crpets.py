from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('mydb')
    allpets = mysql.query_db('SELECT * FROM table2;')
    print(allpets)
    return render_template("cr_pets.html", pets = allpets)

@app.route("/make_pet", methods=["POST"])
def add_pet():
    query = "INSERT INTO table2 (name, type) VALUES (%(na)s, %(ty)s);"
    data = {
        'na': request.form['name'],
        'ty': request.form['type']
        }
    db = connectToMySQL("mydb")
    name = db.query_db(query, data)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

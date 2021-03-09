from postgres import * 
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def welcome(): 
    return render_template("index.html")

@app.route('/inc')
def increment(): 
     cursor.execute("UPDATE MaTable SET ID = ID + 1")
     conn.commit()
     return "Successfully incremented!"

@app.route('/id')
def show_id(): 
    cursor.execute("SELECT ID FROM MaTable")
    conn.commit()
    result = cursor.fetchall()

    return str(result[0][0])

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)

from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
import sqlite3
app = Flask(__name__)
taskCount = 0
finished = 0
data=[]

connection = sqlite3.connect("data.db",  check_same_thread=False );

c = connection.cursor();

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task =request.form.get("task")
        if task != "":
            c.execute("INSERT INTO taskmaster(task, datetime) VALUES(? , ?)", (task , datetime.now())) 
            connection.commit();
        return redirect('/')

    else:
        data = []
        id = []
        dataObj = c.execute("SELECT task,id FROM taskmaster")
        for x in dataObj:
            data.append((x[0] , "/"+str(x[1])))
        taskCount = len(data)
        return render_template("index.html", data = data, taskCount = taskCount, id = id, finished = finished)

@app.route('/delete/<rowid>', methods=['POST','GET'])
def delete(rowid):
    c.execute("DELETE FROM taskmaster WHERE id=?", (rowid,))
    return redirect('/')

@app.route('/edit/<rowid>', methods=['POST','GET'])
def edit(rowid):
    inputText = request.args.get("value")
    if(inputText != ""):
        c.execute("UPDATE taskmaster SET task=? WHERE id=?", (inputText, rowid));
    return redirect('/')


@app.route('/deleteAll', methods=['POST','GET'])
def deleteAll():
    c.execute("DELETE FROM taskmaster");
    connection.commit();
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
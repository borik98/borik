from flask import Flask, request, redirect, abort, render_template

app = Flask(name)
people = [{'name': 'Lol', 'surname': 'Lolovich', 'id': 0},
          {'name': 'Man', 'surname': 'Manovich', 'id': 1},
          {'name': 'User', 'surname': 'Userov', 'id': 2}]

@app.route('/')
def homes():
    return render_template('index.html', people=people)

@app.route('/user/<int:id>')
def find_his_id(id):
    response = f"{people[id]['name']} <br> {people[id]['surname']}<br>"
    return response

@app.route('/')
def users():
    return redirect('/users')

@app.route('/home')
def home():
    return redirect('/')

if name == 'main':
    app.run()

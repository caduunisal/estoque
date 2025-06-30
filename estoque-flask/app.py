from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['estoque']
collection = db['produtos']

@app.route('/')
def index():
    produtos = list(collection.find())
    return render_template('index.html', produtos=produtos)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    quantidade = int(request.form['quantidade'])
    collection.insert_one({'nome': nome, 'quantidade': quantidade})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

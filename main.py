from turtle import title
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return render_template('base.html', title='ИДИОТ')
@app.route('/<varia>')
@app.route('/index/<varia>')
def index(varia):
    return render_template('base.html', title=varia)
@app.route('/profession/<prof>')
def profi(prof):
    t = ''
    if 'инженер' in prof or 'строитель' in prof:
        t = 'Технарь'
    else:
        t = 'Научник'
    return render_template('base.html', title=prof, profession=t)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.dojos import Dojo

from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/dojo/new', methods=['POST'])
def add_dojo():
    Dojo.update(request.form)
    return redirect ('/dojos')

@app.route('/ninjas')
def ninjas():
    dojos=Dojo.get_all()
    return render_template("ninjas.html", ninjas=Ninja.get_ninjas(), dojos=dojos)


@app.route('/ninja/new')
def new_ninja():
    dojos=Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/ninjas/add',methods=['POST'])
def create_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/ninjas')

@app.route('/showdojo/<int:id>')
def dojo_ninjas(id):
    data = {
        'id' : id
    }
    return render_template("show_dojo.html", dojo=Dojo.get_dojo_w_ninjas(data))


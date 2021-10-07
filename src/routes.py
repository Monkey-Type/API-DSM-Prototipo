from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route('/home')
def main():
    return render_template('home.html')


@routes.route('/config')
def config():
    return render_template('config.html')


@routes.route('/editar')
def edit():
    return render_template('editar.html')


@routes.route('/arquivos')
def archive():
    return render_template('arquivos.html')

# Rotas login


@routes.route('/')
def login():
    return render_template('login.html')
    

#sucesso e codigo correto

@routes.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')


@routes.route('/codigo-correto')
def codigo_correto():
    return render_template('codigo-correto.html')

# Importa a classe Flask para criar uma aplicação web.
from flask import Flask, render_template, request, redirect, url_for
# Importa o MongoClient para se conectar ao MongoDB.
from pymongo import MongoClient

# Cria uma instância da aplicação Flask.
app = Flask(__name__)

# Configuração para se conectar ao banco de dados MongoDB no localhost na porta 27017.
client = MongoClient('mongodb://localhost:27017/')

# Conecta ao banco de dados 'Usuarios'.
db = client['Usuarios']
# Cria uma coleção chamada 'Clientes' no banco de dados.
collection = db['Clientes']

# Define uma rota padrão para a página inicial.
@app.route('/')
def index():
    return render_template('index.html')

# Define a rota '/consultar' que pode lidar com os métodos GET e POST.
@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')


        query = {"name": name, "email": email} if name and email else {}

        people = list(collection.find(query))

        return render_template('mostrar_dados.html', data=people)
    return render_template('consultar.html')

# Define a rota '/adicionar' que pode lidar com os métodos GET e POST.
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':

        data = request.form.to_dict()

        name = data.get('name')
        email = data.get('email')


        existing_user = collection.find_one({"name": name, "email": email})
        if existing_user:
            error_message = "Usuário com nome e email já cadastrados."
            return render_template('adicionar.html', error_message=error_message)


        collection.insert_one(data)


        return redirect(url_for('index'))

    return render_template('adicionar.html')

# Define a rota '/remover' que pode lidar com os métodos GET e POST.
@app.route('/remover', methods=['GET', 'POST'])
def remover():
    mensagem = None
    erro = None

    if request.method == 'POST':

        dados = request.form.to_dict()

        nome = dados.get('name')
        email = dados.get('email')

        if nome and email:
            try:

                resultado = collection.delete_one({"name": nome, "email": email})
                if resultado.deleted_count > 0:
                    mensagem = "Usuário excluído com sucesso."
                else:
                    mensagem = "Usuário não encontrado para exclusão."
            except Exception as e:
                erro = f"Erro ao excluir o usuário: {str(e)}"

    return render_template('remover.html', mensagem=mensagem, erro=erro)

# Define a rota '/atualizar' que pode lidar com os métodos GET e POST.
@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    mensagem = None
    erro = None

    if request.method == 'POST':

        nome_antigo = request.form.get('old_name')
        email_antigo = request.form.get('old_email')

        if nome_antigo and email_antigo:

            user = collection.find_one({"name": nome_antigo, "email": email_antigo})

            if user:

                return redirect(url_for('atualizar_usuario', user_id=user['_id']))
            else:
                mensagem = "Usuário não encontrado."

    return render_template('atualizar.html', mensagem=mensagem, erro=erro)

# Define a rota '/atualizar_usuario' que pode lidar com o método POST.
@app.route('/atualizar_usuario', methods=['POST'])
def atualizar_usuario():
    mensagem = None
    erro = None

    if request.method == 'POST':

        old_name = request.form.get('old_name')
        old_email = request.form.get('old_email')
        novo_nome = request.form.get('new_name')
        novo_email = request.form.get('new_email')

        if old_name and old_email and novo_nome and novo_email:

            user = collection.find_one({"name": old_name, "email": old_email})

            if user:
              
                collection.update_one({"name": old_name, "email": old_email}, {"$set": {"name": novo_nome, "email": novo_email}})
                mensagem = "Dados atualizados com sucesso."
            else:
                erro = "Usuário não encontrado."

    return render_template('atualizar.html', mensagem=mensagem, erro=erro)


# Inicia a aplicação Flask em modo de depuração.
if __name__ == "__main__":
    app.run(debug=True)

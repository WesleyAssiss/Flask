
É utilizado Flask para um serviço WEB que gerencia uma lista de nomes e e-mails de pessoas. Perceba que o armazenamento dos dados é baseado em JSON e apenas leitura e escrita simples de arquivos.

Métodos para interação por terminal com o serviço:

Consultar - GET: curl -H "Content-Type: application/json" -XGET http://127.0.0.1:5000/?name=charles

Adicionar - POST: curl -H "Content-Type: application/json" -XPOST http://127.0.0.1:5000/ -d '{"name": "teste", "email": "teste@email.com"}'

Atualizar - PUT: curl -H "Content-Type: application/json" -XPUT http://127.0.0.1:5000/ -d '{"name": "teste", "email": "teste@email.com"}'

Remover - DELETE: curl -H "Content-Type: application/json" -XDELETE http://127.0.0.1:5000/ -d '{"name": "teste", "email": "teste@email.com"}'

Você tem duas atividades:
Implementar uma interface gráfica amigável para interação com esse sistema. A interface deve permitir o usuário executar por um navegador todas as funções (GET, POST, PUT, DELETE) de interação com o sistema;
As informações devem ser armazenadas em um banco de dados não relacional. Faça uma busca e escolha uma base de dados NoSQL de sua preferência.

Se preferir, pode escolher outra linguagem de programação e frameworks para resolver essa atividade prática.

# PI_III

###Os códigos apresentado descreve um sistema web de controle de estoque e 
agendamento de serviços. Ele é composto por uma API desenvolvida em FastAPI e um 
frontend em HTML, CSS e JavaScript. O sistema possui funcionalidades para 
gerenciar usuários, produtos e agendamentos, integrados com um banco de dados 
MySQL.
 
 Requisitos:
 Para executar sua aplicação FastAPI, você precisará dos seguintes requisitos:
 
 #####1. Python:
 • Versão: Python 3.7 ou superior (recomenda-se a versão mais recente). 
• Motivo: FastAPI utiliza recursos e sintaxe disponíveis apenas em versões 
recentes do Python. 
<h5>2. Gerenciador de Pacotes pip:
• Motivo: pip é usado para instalar as dependências do seu projeto. 
• Observação: Geralmente, o pip já vem instalado com o Python.</h5>

3. Ambiente Virtual (Recomendado):
 • Ferramenta: venv (módulo padrão do Python) ou virtualenv (pacote externo). 
• Motivo: Ambientes virtuais isolam as dependências do seu projeto, evitando 
conflitos com outras bibliotecas instaladas no sistema. 
4. Dependências do Projeto (Listadas no requirements.txt):
 • Instalar as bibliotecas contidas em requirements.txt
 5. Banco de Dados MySQL:
 • Motivo: Sua aplicação utiliza um banco de dados MySQL para armazenar dados 
de usuários, agendamentos e produtos. 
• Requisitos: Um servidor MySQL em execução e as credenciais de acesso 
(host, usuário, senha, nome do banco de dados). 
6. Navegador Web:
 • Motivo: Para acessar a interface web da sua aplicação e testar os 
endpoints da API. 
7. Editor de Código (Opcional, mas Recomendado):
 • Exemplos: VS Code, PyCharm, Sublime Text. 
• Motivo: Para editar e gerenciar o código da sua aplicação. 
8. Ferramentas de Teste de API (Opcional, mas Recomendado):
 • Exemplos: Postman, Insomnia, curl. 
• Motivo: Para testar os endpoints da API. 
Passos para Configurar o Ambiente:
 1.Instale o Python: Se você ainda não tem o Python instalado, baixe e 
instale a versão mais recente do site oficial do Python. 
2.Crie um Ambiente Virtual: 
• Navegue até o diretório do seu projeto no terminal. 
• Execute o comando python -m venv meu_env (ou virtualenv meu_env). 
• Ative o ambiente virtual: 
• Linux: source meu_env/bin/activate 
3.Instale as Dependências: 
• Execute o comando pip install -r requirements.txt. 
4.Configure o Banco de Dados MySQL: 
• Certifique-se de que o servidor MySQL esteja em execução. 
• Crie um banco de dados chamado estoque (ou o nome que você definiu 
no main.py). 
• Atualize as credenciais de acesso no main.py. 
5.Execute a Aplicação: 
• Execute o comando uvicorn main:app --reload. 
6.Acesse a Aplicação: 
• Abra um navegador web e acesse http://127.0.0.1:8000..
 
 
 Estrutura de diretorios e arquivos
 └─[$] <git:(main*)> tree                         
.
 ├── main.py
 ├── __pycache__
 │   └── main.cpython-311.pyc
 ├── requirements.txt
 ├── static
 │   ├── script.js
 │   └── style.css
 └── templates
    ├── agendamento_editar.html
    ├── agendamento_form.html
    ├── agendamentos_lista.html
    ├── cadastro.html
    ├── dashboard.html
    ├── editar_usuario.html
    ├── login.html
    ├── pagina_principal.html
    ├── produto_editar.html
    ├── produto_form.html
    ├── produtos_lista.html
    └── relatorios.html
 1. main.py:
 • Função: 
• Este é o arquivo principal da sua aplicação FastAPI. 
• Ele contém todas as rotas da sua API, lógica de negócios, 
configurações do banco de dados e definições de modelos. 
• Ele gerencia a criação de tabelas no banco de dados, define as rotas 
para login, cadastro de usuários, agendamentos, produtos e 
relatórios. 
• Ele serve tanto a interface web quanto a API de consulta de 
agendamentos. 
• Responsabilidades: 
• Definir as rotas da aplicação. 
• Gerenciar o acesso ao banco de dados. 
• Implementar a lógica de negócios da aplicação. 
• Servir os templates HTML. 
• Fornecer os endpoints da API. 
2. static/:
 • Função: 
• Este diretório contém os arquivos estáticos da sua aplicação, como 
CSS, JavaScript e imagens. 
• Os arquivos estáticos são servidos diretamente pelo servidor web. 
• Arquivos: 
• style.css: Arquivo CSS com os estilos da aplicação. 
• script.js: Arquivo JavaScript com a lógica do frontend. 
• Responsabilidades: 
• Definir a aparência e o comportamento das páginas web. 
3. templates/:
 • Função: 
• Este diretório contém os templates HTML da sua aplicação. 
• Os templates são usados para renderizar as páginas web da sua 
aplicação. 
• Eles usam a engine de templates Jinja2 para inserir dados dinâmicos 
nas páginas. 
• Arquivos: 
• pagina_principal.html: Página principal da aplicação. 
• login.html: Página de login. 
• cadastro.html: Página de cadastro de usuários. 
• dashboard.html: Página de dashboard com a lista de usuários. 
• editar_usuario.html: Página para editar um usuário. 
• agendamentos_lista.html: Página com a lista de agendamentos. 
• agendamento_form.html: Página para criar um novo agendamento. 
• agendamento_editar.html: Página para editar um agendamento. 
• produtos_lista.html: Página com a lista de produtos. 
• produto_form.html: Página para criar um novo produto. 
• produto_editar.html: Página para editar um produto. 
• relatorios.html: Página com os relatórios. 
• Responsabilidades: 
• Definir a estrutura e o layout das páginas web. 
• Exibir dados dinâmicos da aplicação. 
4. requirements.txt:
 • Função: 
• Este arquivo lista todas as dependências Python do seu projeto, 
juntamente com suas versões. 
• Ele é usado para recriar o ambiente virtual do projeto em outras 
máquinas. 
• Responsabilidades: 
• Listar as dependências do projeto.

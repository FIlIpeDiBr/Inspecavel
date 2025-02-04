# Instalação

O Inspecável foi desenvolvido com Django, um framework web baseado em python, por esta razão você precisará instalar ambos. Por boa prática, é recomendado o uso de um ambiente virtual de desenvolvimento e este será o método apresentado no tutorial.

> Para instalar o python você pode seguir as informações no [Guia de Instalação Python](https://www.python.org/downloads/ "Guia para instalação do Python") no site oficial.

## Baixando a Aplicação

Acesse o [repositório git](https://github.com/FIlIpeDiBr/Inspecavel "Repositório git da ferramenta Inspecável") e realize o download do código fonte da maneira de sua preferência, seja através do arquivo ZIP ou com o terminal git:

    git clone https://github.com/FIlIpeDiBr/Inspecavel.git

## Configurando o Ambiente Virtual

Com o Python instalado, selecione o diretório em que está o projeto e abra um prompt de comando no local do arquivo. Isso pode ser feito clicando com o botão direito sobre o ícone da pasta e selecionando "Abrir no Terminal" ou utilizando um prompt de comando e navegando até o diretório através do comando:

    cd \caminho\do\diretorio

No diretório do projeto, iremos criar um ambiente virtual. Para isso, execute o código:

    py -m venv Inspecavel

Isso irá criar uma pasta nomeada Inspecavel e configurar o ambiente virtual. Para ativar o ambiente, execute o código:

    Inspecavel\Scripts\activate.bat

O ambiente virtual está agora ativo, como indicado pelo "(Inspecavel)" próximo ao prompt de comando.

> **<ins>Importante</ins>:** O ambiente virtual deve ser ativado novamente <ins>sempre</ins> que você iniciar um novo prompt de comando ou reabrir o projeto, caso contrário não irá funcionar corretamente.

## Instalando as Dependências do Projeto

Para facilitar a instalação, o arquivo requirements.txt contém todas as dependências necessárias para que a ferramenta funcione adequadamente, basta apenas realizar a instalação delas através do comando:

    pip install -r requirements.txt

## Inicializando o Banco de Dados

Por padrão a aplicação utiliza a sqlite3, já que esta é simples de se configurar e, a menos que você precise de um grande número de requisições simultâneas (dezenas de usuários) ou armazenar muitos registros (GB), ela será o bastante.

O repositório traz as migrações e seeds do banco de dados prontas para serem implementadas através do comando:

    python manage.py migrate

>Para informações mais detalhadas sobre o banco de dados acesse a [Documentação Técnica](doc_tecnica.md#banco-de-dados "Seção do Banco de Dados na Documentação").

## Pronto!

Isso é tudo que precisa para que o Inspecável esteja totalmente configurado na sua máquina. Você pode agora testar a instalação hospedando o site de maneira local utilizando:

    python manage.py runserver

Para um guia de como utilizar a ferramenta, acompanhe o tutorial de [Primeiros Passos](guia_de_uso/index.md).
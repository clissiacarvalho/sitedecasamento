#importe das bibliotecas utilizafas
import sqlite3

#criando database nosso casamento
banco_nossocasamento = sqlite3.connect('Nosso_Casamento.db')

#Cursor de navegação do banco de dados"
cursor = banco_nossocasamento.cursor()

############################################################################################

#Criacao da tabela "Recado para os Noivos" se ela não existir, definindo a estrutura da tabela
cursor.execute("CREATE TABLE IF NOT EXISTS recadonoivos(\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                Nome VARCHAR(255) NOT NULL, \
                Email VARCHAR(100) NOT NULL, \
                Mensagem VARCHAR(500) NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO recadonoivos(Nome, Email, Mensagem)VALUES(?, ?, ?)"

#Inserindo dados na database
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("Ana Beatriz Almeida", "ana@gmail.com", "recadoA")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("André Santos", "andre.santos@gmail.com", "recadoB")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("Clissia Carvalho", "clissia.carvalho@gmail.com", "recadoC")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("Mari Cristina", "mari_cristina@gmail.com", "recadoD")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("Valéria Araújo", "val_araujo@gmail.com", "recadoE")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, Email, Mensagem) VALUES ("Jailson Bernandes", "jslsecret@gmail.com", "recadoF")')

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM recadonoivos"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

#Atualizar dados do banco de dados
banco_nossocasamento.commit();

#############################################################################################

#Criação da tabela "Confirmação de Presença"
cursor = banco_nossocasamento.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS conf_presenca(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Nome TEXT NOT NULL,\
               QuantConvidado NUMBER NOT NULL, \
               Presenca NUMBER NOT NULL, \
               Email TEXT NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email)VALUES(?, ?, ?, ?)"

#Inserindo dados na database
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("Ana Beatriz Almeida", 0, 0, "ana@gmail.com")')
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("André Santos", 2, 1, "andre.santos@gmail.com")')
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("Clissia Carvalho", 1, 1, "clissia.carvalho@gmail.com")')
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("Mari Cristina", 1, 1, "mari_cristina@gmail.com")')
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("Valéria Araújo", 2, 1, "val_araujo@gmail.com")')
banco_nossocasamento.execute('INSERT INTO conf_presenca(Nome, QuantConvidado, Presenca, Email) VALUES ("Jailson Bernandes", 0, 0, "jslsecret@gmail.com")')

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM conf_presenca"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

banco_nossocasamento.commit();

#############################################################################################

#Criação da tabela "Lista de Presentes"
cursor = banco_nossocasamento.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS lista_presentes(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Nome TEXT NOT NULL,\
               Email TEXT NOT NULL,\
               Item TEXT NOT NULL, \
               Preco FLOAT NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO lista_presentes(Nome, Email, Item, Preco)VALUES(?, ?, ?, ?)"

#Inserindo dados na database
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("Ana Beatriz Almeida", "ana@gmail.com", "Pipoqueira", 129.99)')
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("André Santos", "andre.santos@gmail.com", "Jogo de Taças", 129.99)')
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("Clissia Carvalho", "clissia.carvalho@gmail.com", "Chaleira", 129.99)')
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("Mari Cristina", "mari_cristina@gmail.com","Conjunto de Talheres", 129.99)')
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("Valéria Araújo", "val_araujo@gmail.com", "Conjunto de Panelas", 129.99)')
banco_nossocasamento.execute('INSERT INTO lista_presentes(Nome, Email, Item, Preco) VALUES ("Jailson Bernandes", "jslsecret@gmail.com", "Microondas", 129.99)')

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM lista_presentes"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

#Atualizar dados do banco de dados
banco_nossocasamento.commit();

#Relacionar tabelas

#Atualizar dados do banco de dados e fechar
banco_nossocasamento.commit();
banco_nossocasamento.close();
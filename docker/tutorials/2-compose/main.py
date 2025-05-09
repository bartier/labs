from flask import Flask, request, jsonify
import mysql.connector
import os
from mysql.connector import Error

app = Flask(__name__)

# Função de conexão com o banco de dados
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            database=os.getenv('MYSQL_DATABASE', 'tasks_db'),
            user=os.getenv('MYSQL_USER', 'user'),
            password=os.getenv('MYSQL_PASSWORD', 'password')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Inicializar banco de dados e tabelas
def init_db():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        # Criar tabela de tarefas se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                status VARCHAR(50) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        connection.commit()
        cursor.close()
        connection.close()

# Operações CRUD
@app.route('/tasks', methods=['GET'])
def get_tasks():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(tasks)
    return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        cursor.close()
        connection.close()
        if task:
            return jsonify(task)
        return jsonify({"error": "Tarefa não encontrada"}), 404
    return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Título é obrigatório"}), 400

    title = request.json['title']
    description = request.json.get('description', '')
    status = request.json.get('status', 'pending')

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)",
            (title, description, status)
        )
        connection.commit()
        task_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return jsonify({"id": task_id, "message": "Tarefa criada com sucesso"}), 201
    return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json:
        return jsonify({"error": "Nenhum dado fornecido"}), 400

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        # Verificar se a tarefa existe
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        if not task:
            cursor.close()
            connection.close()
            return jsonify({"error": "Tarefa não encontrada"}), 404

        # Atualizar tarefa
        title = request.json.get('title', task['title'])
        description = request.json.get('description', task['description'])
        status = request.json.get('status', task['status'])

        cursor.execute(
            "UPDATE tasks SET title = %s, description = %s, status = %s WHERE id = %s",
            (title, description, status, task_id)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Tarefa atualizada com sucesso"})
    return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        connection.commit()
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Tarefa não encontrada"}), 404
        cursor.close()
        connection.close()
        return jsonify({"message": "Tarefa excluída com sucesso"})
    return jsonify({"error": "Falha na conexão com o banco de dados"}), 500

# Inicializar o banco de dados quando a aplicação iniciar
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

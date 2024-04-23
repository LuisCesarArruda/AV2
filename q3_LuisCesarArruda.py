import mysql.connector

# Função para conectar ao banco de dados MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="Root",
        password="",
        database="AV2"
    )

# Função para inserir um registro em uma tabela
insert_record = lambda table, record: f"INSERT INTO {table} VALUES ({', '.join(map(str, record))})"

# Função para remover um registro de uma tabela
delete_record = lambda table, condition: f"DELETE FROM {table} WHERE {condition}"

# Função para consultar todos os registros de uma tabela
select_all_records = lambda table: f"SELECT * FROM {table}"

# Função para consultar registros de uma tabela com uma condição
select_records_with_condition = lambda table, condition: f"SELECT * FROM {table} WHERE {condition}"

# Função para executar uma consulta no banco de dados
def execute_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de inserção de um registro na tabela USERS
    insert_query = insert_record("USERS", (1, "John", "USA", 1))
    print("Inserindo registro na tabela USERS:", insert_query)
    execute_query(insert_query)

    # Exemplo de remoção de um registro da tabela GAMES
    delete_query = delete_record("GAMES", "id_game = 1")
    print("Removendo registro da tabela GAMES:", delete_query)
    execute_query(delete_query)

    # Exemplo de consulta de todos os registros da tabela COMPANY
    select_all_query = select_all_records("COMPANY")
    print("Consultando todos os registros da tabela COMPANY:", select_all_query)
    result = execute_query(select_all_query)
    for row in result:
        print(row)

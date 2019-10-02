from os import environ
import pymysql
import sys


def create_db_connection():
    db = pymysql.connect(

        environ.get('DB_HOST_DRINK'),
        environ.get('DB_USER_DRINK'),
        environ.get('DB_PASSWORD_DRINK'),
        environ.get('DB_NAME_DRINK'),
        autocommit=True
    )
    return db


def add_new_drink(drink_name, stock_level):
    command = f"INSERT INTO drink_management.Drink (name, stock) VALUES ('{drink_name}', {stock_level});"
    return run_db_set_command(command, "Error running command" + command)


def update_drink(drink_id, drink_name, stock_level):
    command = f"UPDATE drink_management.Drink SET name='{drink_name}',  stock={stock_level} WHERE drink_id={drink_id};"
    return run_db_set_command(command, "Error running command" + command)


def delete_drink(drink_id):
    command = f"DELETE FROM drink_management.Drink WHERE drink_id={drink_id};"
    return run_db_set_command(command, "Error running command" + command)


def get_all_data():
    command = f"SELECT * FROM drink_management.Drink;"
    result = run_db_get_command(command,
                                "Error reading data from server!\n" +
                                "function: get_all_data\n" +
                                command)
    return result


def get_all_data_by_id(drink_id):
    command = f"SELECT * FROM drink_management.Drink WHERE drink_id={drink_id};"
    result = run_db_get_command(command,
                                "Error reading data from server!\n" +
                                "function: get_all_data\n" +
                                command)
    return result


def is_in_db(table, column_to_check, looking_for_value):
    result = run_db_get_command(f"SELECT * FROM drink_management.{table} WHERE {column_to_check}='{looking_for_value}';",
                                "Error reading data from server!\n" +
                                "function: load_active_column_from_DB\n" +
                                "when trying to get max_id")
    if result:
        return True
    else:
        return False


def run_db_get_command(command, error):
    db_connection = create_db_connection()
    cursor = db_connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(command)
        results = cursor.fetchall()
        db_connection.close()
        return results
    except Exception:
        print(error)
        print(sys.exc_info())
        input("")
        db_connection.close()
        return False


def run_db_set_command(command, error):
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute(command)
        db_connection.close()
        return True
    except Exception:
        print(error)
        print(sys.exc_info())
        input("")
        db_connection.close()
        return False

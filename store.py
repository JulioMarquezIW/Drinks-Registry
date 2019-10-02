def get_all_data():
    command = f"SELECT * FROM drink_management.Drinks;"
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
    cursor = db_connection.cursor()
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

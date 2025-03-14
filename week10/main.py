import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect("test.db")) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print(f"Name of rows with id > 14:")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print("Error executring quer_1!")
            # Deleting row based on user input    
            try:
                del_row = int(input("Enter row id threshold for deletion: "))
                query_2 = "DELETE FROM demo WHERE id < ?"
                cursor.execute(query_2, (del_row,))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected!")
                db_conn.commit()
            except Exception as e:
                print("Could not execute query_2")
except sqlite3.Error as e:
    print(f"Database connection error: {e}")        
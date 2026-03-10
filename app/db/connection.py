import mysql.connector
import traceback
from dotenv import  load_dotenv
import os

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def execute_select(params=None):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Substitua a consulta abaixo pela sua consulta real, usando parâmetros se necessário
        query = """
            SELECT *
            FROM Processamento_Kit
            WHERE ((Status_Processamento IS NULL AND Created_At > NOW() - INTERVAL 10 MINUTE)
                OR Status_Processamento = 'FAIL')
                AND Created_At > '2026-01-01 00:00:00';
        """
        
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    except Exception:
        print(traceback.format_exc())
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()





# def execute_select():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()

#         query = """
        
#         """

#         cursor.execute(query)

#         return cursor.fetchall()
#     except:
#         print(traceback.format_exc())
#         return False
#     finally:
#         if cursor is not None:
#             cursor.close()
#         if connection is not None:
#             connection.close()



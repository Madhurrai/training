import pyodbc as db
from dbutils import result_as_dict


def main():
    driver='{ODBC Driver 18 for SQL Server}'
    server=r'localhost\SQLEXPRESS'
    database='ecolab_books_db'
    encrypt='no'
    trusted_connection='yes'

    connection_strings=f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        Trusted_Connection={trusted_connection};
        ENCRYPT={encrypt};
    '''
    with db.connect(connection_strings) as connection:
        print('Connection Success')
        cursor=connection.cursor()
        cursor.execute('Select * from book')
        rows = cursor.fetchall()
        result=result_as_dict(cursor)
        print(result)
    
        '''for row in rows:
            print(f'{row.title.ljust(50)}{row.author.ljust(50)}')
            for value in row:
                print(value,end='\t')'''
            



if __name__=='__main__':
    main()
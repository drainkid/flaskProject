import pandas as pd

def get_count(conn,reader_id,dateStart,dateEnd):
    print(dateStart)
    print(dateEnd)
    return pd.read_sql(f''' SELECT reader_name as name, count(reader_id)
    FROM book_reader
     join reader using (reader_id)
    WHERE reader_id = {reader_id} and book_reader.borrow_date>='{dateStart}' 
    and book_reader.return_date<='{dateEnd}' 
    ''',conn)
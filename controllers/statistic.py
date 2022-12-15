import pandas

from app import app
from flask import render_template, request, session
import sqlite3
from utils import get_db_connection
from models.model_statistic import get_count
from models.index_model import get_reader, get_book_reader, return_book, get_new_reader,borrow_book


def convert_date(date):
    dates=date.split('.')
    if(len(dates)>3):
        return dates[2]+'-'+dates[1]+'-'+dates[0]
    else:
        return date

@app.route('/statistic', methods=['get'])
def statistic():
    conn = get_db_connection()
    df_count = pandas.DataFrame

    if request.values.get('getc'):
        reader_id = int(request.values.get('reader'))
        session['reader_id'] = reader_id
        startDate = request.values.get('dateStart')
        endDate = request.values.get('dateEnd')
        startDate = convert_date(startDate)
        endDate = convert_date(endDate)
        df_count = get_count(conn,session['reader_id'],startDate,endDate)
        df_reader = get_reader(conn)
    else:
        session['reader_id'] = 1
        df_count = get_count(conn,session['reader_id'],dateStart=2021-12-12,dateEnd=2001-12-12)
        df_reader = get_reader(conn)

    return render_template('statistic.html',
                            df_count=df_count,
                            len=len,
                            reader_id=session['reader_id'],
                            combo_box=df_reader,
                           )



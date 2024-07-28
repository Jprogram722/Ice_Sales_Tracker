from database import connect
from schemas import DaysSchema


def insert_into_days_table(days_data: DaysSchema) -> dict[str, bool]:
    """
    This function will take the data passed to the api and insert it into the
    database
    """
    try:
        conn, cursor = connect()
        if conn is None:
            return {"msg": "Could Not Connect To Database", "success": False}
        else:
            cursor.execute(f"""
            INSERT INTO days (days_num_bails_sold, days_max_tempurature, days_num_stops, route_id_fk, days_date) VALUES
            ({days_data.num_bails_sold or "Null"}, 
            {days_data.max_tempurature or "Null"}, 
            {days_data.num_stops or "Null"}, 
            {days_data.route or "Null"}, STR_TO_DATE('{days_data.date}', '%Y-%m-%d'))
            """)
            conn.commit()
            conn.close()
            return {"msg": "Data Inserted Into DB", "success": True}
    except Exception as err:
        print(err)
        conn.close()
        return {"msg": "Could Not Connect To Database", "success": False, "date": days_data.date}

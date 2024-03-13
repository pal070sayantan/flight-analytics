import mysql.connector

hostname = "sql6.freesqldatabase.com"
database = "sql6690936"
port = "3306"
username = "sql6690936"
password = "b38jWTtTFR"
class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host=hostname, database=database, user=username, password=password, port=port
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection error')

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM sql6690936.flight
        UNION
        SELECT DISTINCT(Source) FROM sql6690936.flight
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM sql6690936.flight
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM sql6690936.flight
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM sql6690936.flight
							UNION ALL
							SELECT Destination FROM sql6690936.flight) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM sql6690936.flight
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
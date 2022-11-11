'''
    api.py
    Cathy Duan and Hannah Moran, 8 November 2022

    Tiny Flask API to support the met web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)
print("\n\n\n\n")

def get_connection():
    print("hi")
    return psycopg2.connect(database=config.database, user=config.user, password='')

@api.route('/mockup7/', strict_slashes = False) 
def get_artists():
    print('yo')
    query = '''SELECT artist_surname, artist_firstname, artist_bio, artist_birthyear, artist_deathyear
               FROM artists 
               ORDER BY artist_surname '''
    print(query)

    artist_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            artist = {'artist_surname':row[1],
                        'artist_firstname':row[2],
                        'artist_bio': row[3],
                        'artist_birthyear':row[4],
                        'artist_deathyear':row[5]}
            artist_list.append(artist)
        cursor.close()
        print("app slay moment")
        print(artist_list[0])
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(artist_list[0])

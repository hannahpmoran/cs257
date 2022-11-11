# Hannah Moran
# cs257

import sys
import psycopg2

def main():
    args = sys.argv

    # prints usage
    if args[1] == '-h' or args[1] == '--help':
        main_helper()

    if args[1] == '-a' or args[1] == '--athletes':
        noc_athletes(args[2])

    if args[1] == '-m' or args[1] == '--medals':
        noc_medals()

    if args[1] == '-y' or args[1] == '--years':
        year_medals()

# functionally a main method helper function. dont keep in final vers. 
def main_helper():
    with open('usage_olympics.txt', 'r') as file:
        text = file.read()
    print(text)

# returns a list of athlete names from a specified NOC
def noc_athletes(noc):
    # connect
    conn = psycopg2.connect(database = "olympics", user = "hannah", password = '')

    conn.autocommit = True

    # create cursor
    cursor = conn.cursor()

    # retrieve
    cursor.execute('''SELECT DISTINCT athletes.name
                    FROM player_attributes, noc_regions, athletes, linking_table
                    WHERE player_attributes.team = noc_regions.region
                    AND player_attributes.id = linking_table.player_attributes
                    AND athletes_id = linking_table.athletes_id
                    AND player_attributes.team = %s
                    ORDER BY athletes.name;''', (noc,))
    read_query(cursor)
    conn.commit()
    conn.close()

# returns a list of NOCs in descending order by gold medals won
def noc_medals():
    # connect
    conn = psycopg2.connect(database = "olympics", user = "hannah", password = '')

    conn.autocommit = True

    # create cursor
    cursor = conn.cursor()

    # retrieve
    cursor.execute('''SELECT player_attributes.team, COUNT(linking_table.medals) as C
                    FROM player_attributes, medals, linking_table
                    WHERE medals.medals = ' Gold'
                    AND medals.id = linking_table.medals
                    AND linking_table.player_attributes = player_attributes.id
                    GROUP BY player_attributes.team
                    ORDER BY C DESC;''')
    read_query(cursor)
    conn.commit()
    conn.close()

#  returns a list of the years and gold medals won by athletes in descending order
def year_medals():
    # connect
    conn = psycopg2.connect(database = "olympics", user = "hannah", password = '')

    conn.autocommit = True

    # create cursor
    cursor = conn.cursor()

    # retrieve
    cursor.execute('''SELECT player_attributes.year, athletes.name, COUNT(linking_table.medals) as C
                    FROM player_attributes, medals, linking_table, athletes
                    WHERE medals.medals = ' Gold'
                    AND medals.id = linking_table.medals
                    AND linking_table.player_attributes = player_attributes.id
                    AND athletes.id = linking_table.athletes_id
                    GROUP BY player_attributes.year, athletes.name
                    ORDER BY C DESC;''')
    read_query(cursor)
    conn.commit()
    conn.close()

def read_query(query):
    for row in query:
        print(row)

if __name__ == "__main__":
    main()
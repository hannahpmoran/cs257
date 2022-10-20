# Hannah Moran
# CS 257
# access the source data file 'athlete_events.csv' through Kaggle

import csv

def main():

    with open('noc_regions.csv') as csvfile:
            noc_regions_text = csv.reader(csvfile)

            nocs_dict = {}

            for row in noc_regions_text:
                n_data = row[0]
                if n_data not in nocs_dict:
                    nocs_dict[n_data] = str(len(nocs_dict))


    with open('athlete_events.csv') as csvfile:
        athlete_events_text = csv.reader(csvfile)
        next(athlete_events_text)

        # instantiate all dictionaries
        linking_table_dict = {}
        athletes_dict = {}
        player_attributes_dict = {}
        olympic_games_dict = {}
        olympic_events_dict = {}
        medals_dict = {}
        nocs_dict = {}

        # open medals seprately
        with open('medals.csv', 'a') as csvfile:
            medals = csv.writer(csvfile)
            medals.writerow(["Gold"])
            medals.writerow(["Silver"])
            medals.writerow(["Bronze"])
            medals.writerow(["NA"])

            medals_dict = {"Gold" : 0, "Silver" : 1, "Bronze" : 2, "NA" : 3}

        # for each row in athlete_events csv
        for row in athlete_events_text:   

            # check name and sex data; format data as a string to be compared
            a_data = row[1] + '|' + row[2]
            # if data is not already present in dictionary
            if a_data not in athletes_dict:
                # add into dictionary under new unique key, len(dict)
                athletes_dict[a_data] = str(len(athletes_dict))
            
            # check age, height, weight, team, and year; format data as a string to be compared
            p_data = row[3] + '|' + row[4] + '|' + row[5] + '|' + row[6] + '|' + row[9]
            if p_data not in player_attributes_dict:
                # add into dictionary under new unique key, len(dict)
                player_attributes_dict[p_data] = str(len(player_attributes_dict))
            
            # check season, year, city, and games; format data as a string to be compared
            g_data = row[10] + '|' + row[9] + '|' + row[11] + '|' + row[8]
            if g_data not in olympic_games_dict:
                # add into dictionary under new unique key, len(dict)
                olympic_games_dict[g_data] = str(len(olympic_games_dict))

            # check sports and event; format data as a string to be compared
            e_data = row[12] + '|' + row[13]
            if e_data not in olympic_events_dict:
                # add into dictionary under new unique key, len(dict)
                olympic_events_dict[e_data] = str(len(olympic_events_dict))

            # get medal
            medal = medals_dict[row[14]]

            # data is all data in row
            data = str(athletes_dict[a_data]) + '|' + str(player_attributes_dict[p_data]) + '|' + str(olympic_games_dict[g_data]) + '|' + str(olympic_events_dict[e_data]) + '|' + str(medal)
            if data not in linking_table_dict:
                linking_table_dict[data] = str(len(linking_table_dict))
                    
        # open new athletes csv
        with open('athletes.csv', 'a') as csvfile:
            athletes = csv.writer(csvfile)
            # each unique key in athletes will be read
            for key in athletes_dict.keys():
                # split string keys back into list elements for csv layout
                data_list = key.split('|')
                # use insert built-in to format list into writeable elements
                data_list.insert(0, athletes_dict[key])
                # finally transcribe formatted key information into csv row
                athletes.writerow(data_list)
        
        # repeat steps in "athletes.csv"
        with open('player_attributes.csv', 'a') as csvfile:
            player_attributes = csv.writer(csvfile)
            for key in player_attributes_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, player_attributes_dict[key])
                player_attributes.writerow(data_list)

        # repeat steps in "athletes.csv" 
        with open('olympic_games.csv', 'a') as csvfile:
            olympic_games = csv.writer(csvfile)
            for key in olympic_games_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, olympic_games_dict[key])
                olympic_games.writerow(data_list)
        
        # repeat steps in "athletes.csv"
        with open('olympic_events.csv', 'a') as csvfile:
            olympic_events = csv.writer(csvfile)
            for key in olympic_events_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, olympic_events_dict[key])
                olympic_events.writerow(data_list)
        
        with open('linking_table.csv', 'a') as csvfile:
            linking_table = csv.writer(csvfile)
            for key in linking_table_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, linking_table_dict[key])
                linking_table.writerow(data_list)

if __name__ == '__main__':
    main()
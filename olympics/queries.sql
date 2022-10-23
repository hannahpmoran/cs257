SELECT DISTINCT noc from noc_regions order by noc;

SELECT DISTINCT athletes.name
FROM athletes, player_attributes, linking_table
WHERE athletes.id = linking_table.athletes_id
AND player_attributes.id = linking_table.player_attributes
AND player_attributes.team = 'Jamaica'
ORDER BY athletes.name;

SELECT DISTINCT player_attributes.year, medals.medals, athletes.name
FROM athletes, player_attributes, medals, linking_table
WHERE athletes.id = linking_table.athletes_id
AND player_attributes.id = linking_table.player_attributes
AND athletes.name LIKE '%Gregory%Efthimios%'
GROUP BY medals.medals, player_attributes.year, athletes.name
ORDER BY player_attributes.year, medals.medals;

SELECT player_attributes.team, COUNT(linking_table.medals) as C
FROM player_attributes, medals, linking_table
WHERE medals.medals = ' Gold'
AND medals.id = linking_table.medals
AND linking_table.player_attributes = player_attributes.id
GROUP BY player_attributes.team
ORDER BY C DESC;

SELECT DISTINCT athletes.name
FROM player_attributes, noc_regions, athletes, linking_table
WHERE player_attributes.team = noc_regions.region
AND player_attributes.id = linking_table.player_attributes
AND athletes_id = linking_table.athletes_id
AND player_attributes.team = '(%(noc)s)'
ORDER BY athletes.name;


SELECT athletes.name, COUNT(linking_table.medals) as C
FROM player_attributes, medals, linking_table, athletes
WHERE medals.medals = ' Gold'
AND medals.id = linking_table.medals
AND linking_table.player_attributes = player_attributes.id
AND linking_table.athletes_id = athletes_id
GROUP BY athletes.name
ORDER BY C DESC;

SELECT player_attributes.year, athletes.name, COUNT(linking_table.medals) as C
FROM player_attributes, medals, linking_table, athletes
WHERE medals.medals = ' Gold'
AND medals.id = linking_table.medals
AND linking_table.player_attributes = player_attributes.id
AND athletes.id = linking_table.athletes_id
GROUP BY player_attributes.year, athletes.name
ORDER BY C DESC;


To run neo4j server using docker, use the following command
```
 docker run -p7687:7687 -p7474:7474 neo4j
```

In neo4j, run the following query to populate the data


```
// Create Teams
CREATE (team1:Team {name: 'Team A', country: 'India'}),
       (team2:Team {name: 'Team B', country: 'Australia'}),
       (team3:Team {name: 'Team C', country: 'England'});

// Create Players
CREATE (player1:Player {name: 'Player 1', role: 'Batsman', age: 30}),
       (player2:Player {name: 'Player 2', role: 'Bowler', age: 28}),
       (player3:Player {name: 'Player 3', role: 'All-rounder', age: 29}),
       (player4:Player {name: 'Player 4', role: 'Wicketkeeper', age: 32}),
       (player5:Player {name: 'Player 5', role: 'Batsman', age: 25});

// Assign Players to Teams
CREATE (player1)-[:PLAYED_FOR]->(team1),
       (player2)-[:PLAYED_FOR]->(team1),
       (player3)-[:PLAYED_FOR]->(team2),
       (player4)-[:PLAYED_FOR]->(team3),
       (player5)-[:PLAYED_FOR]->(team3);

// Create Matches
CREATE (match1:Match {date: date('2024-01-10'), location: 'Mumbai', match_type: 'ODI'}),
       (match2:Match {date: date('2024-02-15'), location: 'Sydney', match_type: 'Test'}),
       (match3:Match {date: date('2024-03-20'), location: 'London', match_type: 'T20'});

// Players participated in Matches
CREATE (player1)-[:PARTICIPATED_IN]->(match1),
       (player2)-[:PARTICIPATED_IN]->(match1),
       (player3)-[:PARTICIPATED_IN]->(match2),
       (player4)-[:PARTICIPATED_IN]->(match3),
       (player5)-[:PARTICIPATED_IN]->(match3);

// Team won Matches
CREATE (team1)-[:WON_MATCH]->(match1),
       (team2)-[:WON_MATCH]->(match2),
       (team3)-[:WON_MATCH]->(match3);
```


Now install all dependencies using:

```
pip install -r requirements.txt
```

Now you can run the file:

```
python src/hello.py
```

Navigate to  ```http://127.0.0.1:5000/graphq``` and use the UI to query neo4j using graphQL

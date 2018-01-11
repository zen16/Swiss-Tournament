-- Table definitions for the tournament project.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament

DROP TABLE IF EXISTS Players CASCADE;
DROP TABLE IF EXISTS Matches CASCADE;

CREATE TABLE Players (
	name TEXT NOT NULL,
	id SERIAL PRIMARY KEY
	);

CREATE TABLE Matches (
	winner_id integer NOT NULL REFERENCES Players(id),
	loser_id integer NOT NULL REFERENCES Players(id),
	id SERIAL PRIMARY KEY
	);

CREATE VIEW Standings AS
  SELECT 
    id, 
    name, 
    (SELECT COUNT(winner_id) FROM Matches WHERE p.id = winner_id) AS wins,
    (SELECT COUNT(*) FROM Matches WHERE p.id IN (winner_id, loser_id)) AS matches
  FROM Players as p
  ORDER BY wins DESC;

#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament


import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def do_request(request, data=(), do_fetch=False, do_commit=False):
    """Send SQL-query to DB.

    Also can perform a commit and fetch data from cursor.

    Args:
      request: SQL-query string
      data: arguments for SQL-query
      do_fetch: flag for returning fetched data
      do_commit: flag for commit after executing the request

    Returns:
      Fetched data from cursor, if do_fetch=True.
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(request, data)
            if do_commit:
                conn.commit()
            if do_fetch:
                return cur.fetchall()
            return


def delete_matches():
    """Remove all the match records from the database."""
    
    query = '''DELETE FROM Matches;'''
    do_request(query, do_commit=True)
    return


def delete_players():
    """Remove all the player records from the database."""

    query = '''DELETE FROM Players CASCADE;'''
    do_request(query, do_commit=True)
    return


def count_players():
    """Returns the number of players currently registered."""

    query = '''SELECT COUNT(*) FROM Players;'''
    return int(do_request(query, do_fetch=True)[0][0])


def register_player(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = '''INSERT INTO Players VALUES(%s);'''
    do_request(query, do_commit=True, data=(name,))
    return


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
     
    query = '''SELECT * FROM Standings;'''
    return do_request(query, do_fetch=True)


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    query = '''INSERT INTO Matches VALUES(%s, %s);'''
    do_request(query, do_commit=True, data=(winner, loser))
    return
 
 
def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = player_standings()
    pairs = []
    first_opponent = None
    for player_stat in standings:
        if not first_opponent:
            first_opponent = tuple(player_stat[0:2])
            continue
        else:
            second_opponent = tuple(player_stat[0:2])
            pairs.append(first_opponent + second_opponent)
            first_opponent = None

    return pairs

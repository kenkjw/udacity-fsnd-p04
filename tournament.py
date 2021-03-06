#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    query = "DELETE FROM matches"

    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    query = "DELETE FROM players"

    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()

    
def countPlayers():
    """Returns the number of players currently registered."""
    query = "SELECT count(*) FROM players"

    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    count = cursor.fetchone()
    cursor.close()
    db.close()
    return count[0]



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players (name) VALUES (%s)"

    db = connect()
    cursor = db.cursor()
    cursor.execute(query,(name,))
    db.commit()
    cursor.close()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a 
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = """ 
        SELECT p.id, p.name, count(m1.winner) as wins, 
               count(m1.winner)+count(m2.loser) as matches
        FROM players as p
        LEFT JOIN matches as m1 on p.id=m1.winner
        LEFT JOIN matches as m2 on p.id=m2.loser
        GROUP BY p.id
        ORDER BY wins DESC
    """   

    db = connect()
    cursor = db.cursor()    
    cursor.execute(query)
    standings = cursor.fetchall()
    cursor.close()
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    query = "INSERT INTO matches (winner,loser) VALUES (%s,%s)"
    db = connect()
    cursor = db.cursor()
    cursor.execute(query,(winner,loser))
    db.commit()
    cursor.close()
    db.close()
 
 
def swissPairings():
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
    s = playerStandings()
    return [(s[i][0],s[i][1],s[i+1][0],s[i+1][1]) for i in xrange(0,len(s),2)]

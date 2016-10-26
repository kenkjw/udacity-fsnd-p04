# Udacity Full Stack Nanodegree Project: Tournament Results

This project utilizes a PostgreSQl database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

For this project, the students were given a pre-setup Vagrant VM as their environment for running the code.  
Here are links to [Vagrant](http://vagrantup.com/), [VirtualBox](https://www.virtualbox.org/), and the [VM repository](http://github.com/udacity/fullstack-nanodegree-vm)) for setting up the dev environment.

The project uses [Python 2.7](https://www.python.org/download/releases/2.7/) and [PostgreSQL v9.3.14](https://www.postgresql.org/download/). In addition, the python module `psycopg2` is required. These are all already bundled with the Vagrant VM should you choose to use it.

Project files:
* tournament.sql - SQL database and table definitions
* tournament.py - Python implementation of the tournament API
* tournament_test.py - Instructor provided test suite

To setup the database from the command line, run the following commands:  

```
createdb tournament
psql -f tournament.sql tournament
```

To run the test suite:  

```
python tournament_test.py
```
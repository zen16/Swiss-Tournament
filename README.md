# Swiss-System Tournament
https://en.wikipedia.org/wiki/Swiss-system_tournament


This is a Learning Project of Udacity Intro to Relational Databases (https://classroom.udacity.com/courses/ud197)

### Understand the purpose of each file

tournament.sql  - this file is used to set up your database schema (the table representation of your data structure).
tournament.py - this file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program). Remember that when you define a function, it does not execute, it simply means the function is defined to run a specific set of instructions when called.
tournament_test.py - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py

### Using the Vagrant Virtual Machine

The Vagrant VM has PostgreSQL installed and configured, as well as the psql command line interface (CLI), so that you don't have to install or configure them on your local machine.
To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command vagrant up (powers on the virtual machine) followed by vagrant ssh (logs into the virtual machine).  
Remember, once you have executed the vagrant ssh command, you will want to cd /vagrant to change directory to the synced folders in order to work on your project, once your cd /vagrant, if you type ls on the command line, you'll see your tournament folder.
The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed, as well as the psql command line interface (CLI), so you'll need to have your VM on and be logged into it to run your database configuration file (tournament.sql), and test your Python file with tournament_test.py.

### Using the tournament.sql file

The tournament.sql file should be used for setting up your schema and database prior to a client making use of the database for reporting and managing tournament players and matches. This file will only be ran once by a client setting up a new tournament database, however we will probably run this file many times as we work on this project.

## Example of a 16 Player Swiss Tournament:

First round pairing is by random draw. For example, with 16 players they would be matched into 8 random pairs for the first round. For now, assume all games have a winner, and there are no draws.

##### After the first round
there will be a group of 8 players with a score of 1 (win), and a group of 8 players with a score of 0 (loss). For the 2nd round, players in each scoring group will be paired against each other – 1’s versus 1’s and 0’s versus 0’s.

##### After round 2
there will be three scoring groups:
4 players who have won both games and have 2 points
8 players who have won a game and lost a game and have 1 point
4 players who have lost both games and have no points.

##### Again, for round 3
players are paired with players in their scoring group. After the third round, the typical scoring groups will be:
2 players who have won 3 games (3 points)
6 players with 2 wins (2 points)
6 players with 1 win (1 point)
2 players with no wins (0 points)

##### For the fourth (and in this case final) round
the process repeats, and players are matched with others in their scoring group. Note that there are only 2 players who have won all of their games so far – they will be matched against each other for the "championship" game. After the final round, we’ll have something that looks like this:
1 player with 4 points – the winner!
4 players with 3 points – tied for second place
6 players with 2 points
4 players with 1 point
1 player with 0 points

The Swiss system produces a clear winner in just a few rounds, no-one is eliminated and almost everyone wins at least one game, but there are many ties to deal with.

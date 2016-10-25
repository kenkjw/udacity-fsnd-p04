-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop table if exists players cascade;
drop table if exists matches;

CREATE TABLE players ( id SERIAL primary key,
                      name varchar(64) not null);

CREATE TABLE matches ( id SERIAL,
                      winner int references players(id),
                      loser int references players(id));




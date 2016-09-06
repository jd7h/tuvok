# tuvok
TV-series episode selector based on IMDB-ratings. 

## Etymology
Named after [Tuvok](https://en.wikipedia.org/wiki/Tuvok), the security officer from Star Trek: Voyager. After all, it is only logical to watch only the highest-rated episodes of classic series.

## Goal
I originally made this script for determining which subset of Star Trek episodes to watch.

## Usage and output
The script takes two inputs: an IMDB-id and a minimum rating. I will work on neat argument parsing in the future.

```
>>> tuvok.main("tt0303461",8.0)
Season 1
----------
8.6      1 The Train Job
8.7      2 Bushwhacked
9.2      3 Our Mrs. Reynolds
9.0      4 Jaynestown
9.5      5 Out of Gas
8.6      6 Shindig
8.3      7 Safe
9.2      8 Ariel
9.1      9 War Stories
9.5      10 Objects in Space
9.1      11 Serenity
8.5      12 Heart of Gold
9.0      13 Trash
8.6      14 The Message

Firefly (2002–2003) has 14 episodes with rating >= 8.0.
```

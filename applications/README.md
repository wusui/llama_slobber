# LLAMA SLOBBER APPLICATIONS

The applications in this directory are used to generate the json file and
csv file information in the subdirectories here.

## Applications

### save_personal_data.py

Save personal information (College, Location, Gender) for all current
Learned League players.

***

### save_match_hist.py

Using personal/people.json, get the results of all matches.  Save in
match_data.  Each match_data entry contains 100 individual match histories
for 100 players

***

### find_wlt_best.py

Scan through the files in match_data.  Look for patterns of won-loss-tie
numbers that repeat.  Save the ones with the smallest cycle and return a
dictionary indexed by player, where each entry is a season number and the
cycle length.  Only the shortest ones are returned.

***

## Directories

### personal

Files in this directory include:
  * <Rundle>.json -- personal information by rundle
  * everybody.json -- all personal information
  * locations.csv -- csv file of people and locations
  * schools.csv -- csv file of people and schools
  * people.json -- alphabetically sorted list of people

***

### match_data

Files in this directory are of the form X__Y.json where X is the name of the
first person in the file, and Y is the name of the last person in the file.
The names are in alphabetical order.  Each of these files is 100 entries long.

***

# SCREEN SCRAPING API

The following is a description of the methods in llama_slobber used for scraping data from the Learned League site.
Except for get_session() (the first method documented), all of these methods allow the user to pass a session keyword
argument (session=session_id).  If this argument is not passed, the method will extract the information from logindata.ini.
It will still work but will require input from an external file read for each call.  So if the user is intending to do many
api calls, then this parameter should be used for efficiency purposes.

The modules also contain HTMLParser sub-classes that are used by the code to scrape information from web pages.
These classes are not documented as part of the API.

***

### get_session()

Returns -- session id

Routine used to obtain a session id.  This session id can be passed as a keyword argument to later calls.

***

### get_page_data(url, parser)

Arguments:
  * url -- URL of web page to be parsed.
  * parser -- HTMLParser class used for parsing
  
Returns -- data to be passed back by the API call.

This method is used by the other methods in the package to parse data.  It is not normally used by the user
but is available if one wants to extract data using their own HTMLParser class.

***

### get_season()

Returns -- the current season number, or the last completed season if between seasons  (int)

This method reads the main Learned League page to extract the current season number.

***

### get_leagues(season)

Arguments:
  * season -- season number (int)

Returns -- list of league names

***

### get_rundles(season, league)

Arguments:
  * season -- season number (int)
  * league -- league name (string)

Returns -- list of rundles in this league

***

### get_onedays()

Returns -- list of one-day contests.  Each entry in this list is a list that consists of:
  * the date that this contest took place (example: 'Jul 18, 2018')
  * the abbreviated name of this contest (example: '60sspycraze')
  * the full name of this contest (example: 'The 60s Spy Craze')
  
***

### get_qhist(player)

Arguments:
  * player -- name of the player

Returns -- the question history for the player

The return value is a dictionary whose keys correspond to each question category found on the Question History tab.
Each entry consists of a dictionary with two keys ('correct' and 'wrong').  These values of these entries are lists
of questions depending on whether this person got the question right or wrong.

The indivual questions are indicated by a dash separated string of numbers whose values in order are:
  * season number
  * day number
  * question number

78-13-5 for example would be the fifth question on day 13 of season 78.

***

### get_matchday(season, day, rundle)

Arguments:
  * season -- season number
  * day -- match day number
  * rundle -- rundle name
  
Returns -- a two item list.  The first item is extracted data from the
page for the specified rundle on the specified match day.
The second item is metadata.

The first item is a dictionary of data extracted from the web page.  Each entry in the returned dictionary
is indexed by the name of a player in that rundle.

The corresponding value of each entry is another dictionary containing the following elements:
  * 'opp' -- the player's opponent for that match
  * 'answers' -- a 6 item list corresponding to this player's answers for the six questions on that day.  Values can be '0' (for incorrect), '1' (for correct), or 'F' (for forfeit).
  * 'ratings' -- a 6 item list of integer values corresponding to how that player was defended for each question.
  
***

### get_personal_data(person)

Arguments:
  * person -- llama id (usuiw, for example)

Returns a dictionary containing personal information for this user.
Current fields are Gender, Location, and School.

***

### get_rundle_members(season, rundle)

Arguments:
  * season -- season number
  * rundle -- rundle name ('B_Pacific' for example)

Returns a list of players in this rundle.

***

### get_rundle_personal(season, rundle)

Arguments:
  * season -- season number
  * rundle -- rundle name ('B_Pacific' for example)

This combines the previous two calls.  What this returns is a dictionary
indexed by player names.  The saved values are values returned by
get_personal_data for each individual

***

### get_rundle_comp(season, rundle, fsize, session_id=get_session(),func_parm=calc_hun)

Arguments:
  * season -- LL season number
  * rundle -- rundle name "B_Pacific" for example
  * fsize -- size of the field to be displayed
  * func_parm -- name of the routine to be executed for all pairs in this rundle.  Keyword parameter, defaults to calc_hun.

This function returns a dictionary whose keys are an alpabetically sorted
list of the names of the players in the rundle.  Each value is a list of tuples
consisting of a opponent and the result of the func_parm call when passed the
combination of the user name in the key and the user name in the tuple.  This
list is sorted in descending numeric order based on the second number in the
tuple.  If no func_parm is specfied, calc_hun is used.

***

### get_matchresult(season, day, rundle, session=get_session())

Arguments:
  * season -- season number
  * day -- match day number in range 1 to 25
  * rundle -- name of rundle (R_Pacific_Div_2, for example)

Returns a list of match results.  Each result consist of a dictionary with
two entries.  The 'players' entry is a list of the two players in a match.
The score entry is a list of strings corresponding to their scores (in
LL x(y) notation).

***

### get_user_data(player,  session=get_session())

Arguments:
   player -- player name

Returns career information for a player.  The results are returned
as a list of two dictionaries.  Each dictionary is indexed by a season
number.

The first dict contains lists of matches.  Each match consists of two lists
each two numbers long.  The first list is the matchpoint score and correct
answer count for the plaayer.  The second list is the matchpoin score and
correct answer count for the opponent.

The second dict contains a list of won-loss records for the player.  Each
match is a three item list of numbers representing matches won, lost, and
tied up to that point.

***

### get_matchresult(season, day, rundle, session=get_session())

Arguments:
  * season -- season number
  * day -- match day number in range 1 to 25
  * rundle -- rundle name (B_Pacific, for example)

Return a list of matches.  Each match is represented by a dictionary entry
whose keys are 'names' and 'scores'.  The values of those entries are two
item lists of player names, and their correspoding score (stored as characters)

***

### get_csv_oneday_players(quiz, session=get_session())

Arguments:
  * quiz -- one-day quiz name

Returns a list of players who played this oneday.

***

### get_csv_ondeday_data(quiz, session=get_session())

Arguments:
  * quiz -- one-day quiz name

Returns the contents of the csv file corresponding to this one-day quiz name.

***

### read_csv_data(url, session=get_session())

Arguments:
  * url -- url of a csv file to be read

Returns a  list of lines.  Each line is a list of fields.

***

### parse_oneday_get_date(oneday, session=get_session())

Arguments:
  * oneday -- quiz name

Returns a date value (the day that this quiz took place).

***

### ll_oneday_players(oneday, session=get_session())

Arguments:
  * oneday -- quiz name

Returns a list of players in this oneday.

***

### handle_conn_err(func)

Arguments:
  * func -- function being wrapped.

handle_conn_err is used as decorator by other scraping functions to
avoid having spurious requests.ConnectionErrors exceptions terminate
lengthy scraping session.

***

### act_on_all_rundles(season, action, payload):

Arguments:
  * season -- season number
  * action -- function that will operate on all rundles
  * payload -- either parameters passed to action, or an object into which
               results are saved.

All rundles names are found for the season specified (A_Coastal, B_Pacific,
R_Laguna_Div_2 are examples).  For each of these rundles, the function
specified by action is called.  The season, rundle, and payload are passed.

Depending on the behavior of the action function, payload is either a
set of parameters passed to the action function, or a mutable objecct
that will be modified as data is inserted by the action function.

***

### append_action(_, rundle, payload)

Arguments:
  * rundle -- rundle name
  * payload -- list into which extracted rundle names will be saved

This routine is passed to act_on_all_rundles to generate a list of
rundle names

***

# EXAMPLES

The first example here demonstrates the get_season, get_leagues, get_rundles, and get_onedays calls.  The second example
demonstrates the get_qhist and get_matchday calls and also demonstrates how to set and pass a session value.

```python
(slobber)$ python
Python 3.6.2 (default, Jul 23 2018, 10:46:18)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from llama_slobber import get_season
>>> from llama_slobber import get_leagues
>>> from llama_slobber import get_rundles
>>> from llama_slobber import get_onedays
>>> get_season()
78
>>> get_leagues(66)
['Alpine', 'Central', 'Coastal', 'Corridor', 'Frontier', 'Highland', 'Horizon', 'Maritime', 'Memorial', 'Meridian', 'Metro', 'Midland', 'Pacific', 'Seaboard', 'Sequoia', 'Skyline', 'Sugarloaf']
>>> get_rundles(78, 'Pacific')
['A_Pacific', 'B_Pacific', 'C_Pacific_Div_1', 'C_Pacific_Div_2', 'D_Pacific_Div_1', 'D_Pacific_Div_2', 'E_Pacific_Div_1', 'E_Pacific_Div_2', 'R_Pacific_Div_1', 'R_Pacific_Div_2']
>>> get_onedays()[0:2]
[['Oct 13, 2018', 'nationalism', 'Nationalism'], ['Oct 13, 2018', 'justimagesmathematics', 'Just Images Mathematics']]
```

```python
(slobber)$ python
Python 3.6.2 (default, Jul 23 2018, 10:46:18)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from llama_slobber import get_session
>>> from llama_slobber import get_qhist
>>> from llama_slobber import get_matchday
>>> session_id = get_session()
>>> q = get_qhist('usuiw', session=session_id)
>>> q['MATH']['correct'][0:10]
['78-24-1', '78-9-5', '77-13-5', '77-7-4', '77-4-6', '76-25-6', '76-19-2', '76-1 1-2', '76-7-1', '75-25-1']
>>> m = get_matchday(78, 25, 'B_Pacific', session=session_id)
>>> print(m[1])
{'season': 78, 'day': 25, 'rundle': 'B', 'league': 'Pacific', 'division': 0}
>>> m[0]['UsuiW']['ratings']
[2, 1, 1, 3, 0, 2]
```


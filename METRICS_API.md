# LLAMA SLOBBER METRICS

The following is a description of the methods in llama_slobber used for data
analysis.  If a session_id is passed as an optional keyword argument, then
that session_id is the same as the session_ids documented in SCRAPING_API.md.

***

### calc_hun(player1, player2, session_id=session_id)

Arguments:
  * player1 -- first player
  * player2 -- second player
  * session_id -- session id (optional)

Returns -- floating point number between 0 and 1 (Hun calculated)

Hamill/Usui numbers (HUN) are a metric to determine how similar a player
is to another player.  This value is the number of questions on which they
got the same result (both got right or both missed) divided by the total
number of questions that they answered in common.  This has a maximum
value of one and the higher the number is, the similar to two players are.

***

### comp_hun(player1, player2)

Arguments:
  * player1 -- first player question history dictionary
  * player2 -- second player question history dictionary

Returns -- floating point number between 0 and 1 (Hun calculated)

Called by calc_hun, this method can be called directly if the question
history information has already been obtained.

***

### calc_wonder(season, rundle, session_id=session_id)

Arguments:
  * season -- season number
  * rundle -- rundle name
  * session_id -- session id (optional)

Returns -- Sorted list of tuples consisting of players and wonder values.

WONDER ("Warren's Overtly Narcissistic Defensive Efficiency Rating") is a 
statistic that measures how much defense affected the standings points
of a player.  It compares match point scores with total questions scores
for a match.  If player A and player B tie on total questions but player A
beats player B on matchpoints, then player A's WONDER score goes up by 1 and
player B's WONDER score goes down by 1.  Similarly, a loss in total questions
with a tie in matchpoints would also change WONDER values by 1, and a loss in
total questions with a win in matchpoints would change WONDER values by 2.

Since this value only changes by a low integer, the tracking of this value
is only being done for each season. 

***

### score_wonder(match_info)

Arguments:
    match_info -- score in [[a, b], [c, d]] format

Return wonder score for the individual match.

***

### get_wlt_patterns(player)

Arguments:
  * player -- player name

Returns -- pattern information

The return value is a list of seasons with a repeating cycles of scores.
Each entry in the list consists of a season number, and the length of the
cycle where the repeating scores appear.

***

### find_wlt_patterns(player, pinfo)

Arguments:
  * player -- player name
  * pinfo -- player record information

Returns -- pattern information

The return value is a list of seasons with a repeating cycles of scores.
Each entry in the list consists of a season number, and the length of the
cycle where the repeating scores appear.

***

### find_stored_stat(directory, this_func, oresult)

Arguments:
  * directory -- location of json files to be scanned.
  * this_func -- function to be run against the entries found
  * oresult -- dictionary saving the results of this_func calls

Run this_func using as input all the json files in the directory specified
by the directory parameter. Results are accumulated in oresult.

***

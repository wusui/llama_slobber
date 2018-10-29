# LLAMA SLOBBER METRICS

The following is a description of the methods in llama_slobber used for
data analysis and data formatting.  If a session_id is passed as an
optional keyword argument, then that session_id is the same as the
session_ids documented in SCRAPIND_API.md.

***

### format_float(number, decimal_places)

Arguments:
  * number -- floating point number to be formatted.
  * decimal_places -- number of decimal places to be displayed
  
Returns -- a floating point value limited to the number of decimal places.
           Values are rounded

This method can be used to format floating point numbers for display.

##### USAGE

```python
from llama_slobber import format_float
.
.
.
print(format_float(.497, 2))
```

This should print out .48

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

##### USAGE

```python
from llama_slobber import calc_hun
.
.
.
hun = calc_hun('usuiw', 'veredj')
```

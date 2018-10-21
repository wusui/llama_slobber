# SCREEN SCRAPING API

The following is a description of the methods in llama_slobber used for scraping data from the Learned League site.
Except for get_session() (the first method documented), all of these methods allow the user to pass a session keyword
argument (session=session_id).  If this argument is not passed, the method will extract the information from logindata.ini.
It will still work but will require input from an external file read for each call.  So if the user is intending to do many
api calls, then this parameter should be used for efficiency purposes.

The modules also contain HTMLParser sub-classes that are used by the code to scrape information from web pages.
These classes are not documented as part of the API.

***

### ll_local_io.get_session()

Returns -- session id

Routine used to obtain a session id.  This session id can be passed as a keyword argument to later calls.

##### USAGE

```python
from llama_slobber.ll_local_io import get_session
.
.
.
session_id = get_session()
```

***

### ll_local_io.get_page_data(url, parser)

Arguments
  * url -- URL of web page to be parsed.
  * parser -- HTMLParser class used for parsing
  
Returns -- data to be passed back by the API call.

This method is used by the other methods in the package to parse data.  It is not normally used by the user
but is available if one wants to extract data using their own HTMLParser class.

***

### ll_season.get_season()

Returns -- the current season number, or the last completed season if between seasons  (int)

This method reads the main Learned League page to extract the current season number.

##### USAGE

```python
from llama_slobber.ll_season import get_season
.
.
.
season_number = get_season()
```

***

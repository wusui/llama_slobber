# LLAMA SLOBBER

Llama_slobber is a package of python3 tools useful for Learned League data analysis.

It consists of screen scraping routines which can be used to extract data from
Learned League web pages, calculation routines for various Llama Slobber
statistics, and some formatting routines to help generate web pages and
csv files.

## Name Origin

[Learned League](http://www.learnedleague.com) is a website hosting a series of on-line trivia tournaments
(see this [Washington Post article](https://www.washingtonpost.com/lifestyle/style/the-coolest-weirdest-internet-community-youll-never-be-able-to-join/2014/08/20/3c3f565e-26eb-11e4-958c-268a320a60ce_story.html?noredirect=on&utm_term=.16ba008490a5) for more information).
Due to the fact that Learned League starts with the letters LL, members of this league tend to refer to themsleves as llamas.

During some on-line discussion on this site, someone off-handedly refered to some members of the group as
Learned League Sabrmetricians which definitely is the wrong term.  Sabrmetrics refers to the analysis of baseball data
performed by the [Society of American Baseball Research](https://sabr.org).  We were clearly different.
So I have started the Society of Learnedleague Obscure and Byzantine Reseach (abbreviated SLOBR), and developed this
package to aid others in doing analysis of Learned League data.

## Installation

Llama_slobber has been packaged on the [Python Package Index website](https://pypi.org) and can be downloaded using the following
command: `python -m pip install llama_slobber`.  It also requires the requests
packages, so if this is not installed, you should also run:
`python -m pip install requests`.

## logindata.ini file

In order to use the tools in llama_slobber, one must be able to login to the Learned League website.  So before any of these
tools can work, the user must create a file named logindata.ini which would contain the following:

```
[DEFAULT]
username = <your Learned League user name>
password = <your Learned League user password>
```

This logindata.ini file should be placed in the directory from which the user's python code will be run.

## USAGE

All of the methods documented in the files listed in the *Further Documentaion*
section of this document can be used by importing the method and calling the
method with the appropriate variables.  For example, the following
code will caculate hun values for the B_Pacific rundle during season 78,
and print the hun values for 'usuiw' as an html page

```python
from llama_slobber import get_rundle_comp
from llama_slobber import gen_html_table
.
.
.
foo = get_rundle_comp(78, 'B_Pacific', 6)
print(gen_html_table('usuiw', foo['usuiw']))
```

## Other files in this directory

Most of the other files in this directory are in the application subdirectory,
which contains files that are used to produce the Llama Slobber website.
(http://warrensusui.com/llama_slobber/main_page.html)

## Futher Documentation

  * [Screen Scraping API](https://github.com/wusui/llama_slobber/blob/master/SCRAPING_API.md)
  * [Metrics API](https://github.com/wusui/llama_slobber/blob/master/METRICS_API.md)
  * [I/O API](https://github.com/wusui/llama_slobber/blob/master/IO_API.md)
 
## Author

  * Warren Usui (warrenusui@gmail.com)

## License

This project is licensed under the MIT License

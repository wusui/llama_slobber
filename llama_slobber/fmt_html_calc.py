#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Given the results of a get_rundle_comp call, generate a web page to display
those values.
"""


def html_wrap(ptext, owrapper):
    """
    Wrap text with html tags.

    Input:
        ptext -- text to be wrapped
        owrapper -- tag to wrap ptext with

    If owrapper ends with a newline, then the newline will appear after the
    bracket character in the last tag.

    Returns the wrapped string value.
    """
    wrapper = owrapper.strip()
    hdr = '<%s>' % wrapper
    trlr = '</%s>' % wrapper
    if owrapper.endswith('\n'):
        trlr += '\n'
    return hdr + ptext + trlr


def add_attrib(attrib, ptext):
    """
    Insert an attribute into some html text

    Input:
        attrib -- text of the attribute to be added.
        ptext -- snippet of html code in which to insert the attribute.

    Returns the text with the attribute added.
    """
    bloc = ptext.find('>')
    if bloc <= 0:
        return ptext
    fpart = ptext[0:bloc]
    spart = ptext[bloc:]
    return fpart + ' ' + attrib + spart


def add_breaks(instring, above, below):
    """
    Add line breaks before and after some text

    Input:
        instring -- text inside the breaks.
        above -- number of blank lines above the text
        below -- number of blank lines below the text

    Returns string with breaks added.
    """
    outstr = ''
    for _ in range(0, above):
        outstr += '<br>'
    outstr += instring
    for _ in range(0, below):
        outstr += '<br>'
    return outstr + '\n'


def gen_html_table(header, data):
    """
    Generate an html table for a user.

    Input:
        header -- user whose data will be formatted into a table
        data -- tuples of information used to make rows in the table

    Returns a snippet of html code representing this table
    """
    hsize = len(data[0])
    disp = html_wrap(header, 'th')
    disp = add_attrib('colspan="%d"' % hsize, disp)
    disp = html_wrap(disp, 'tr\n')
    for ptuple in data:
        tline = ''
        for field in ptuple:
            tline += html_wrap(field, 'td')
        tline = html_wrap(tline, 'tr\n')
        disp += tline
    return html_wrap(disp, 'table\n')


def gen_html_page(info, title, header):
    """
    Generate an html page for get_rundle_comp data

    Input:
        info -- the get_rundle_comp data to be displayed
        title -- text for the page's title
        header -- text for the large centered text at the top of the page

    Returns:
        Web page contents as a string
    """
    otext = html_wrap(title, 'title\n')
    css_info = """h1 { text-align: center }
              table { float: left; border: 1px solid black; margin: 12px; }
              td { border: 1px solid black; text-align: center }"""
    css_info = html_wrap(css_info, 'style\n')
    css_info = html_wrap(css_info, 'head\n')
    otext += css_info
    text = add_breaks(html_wrap(header, 'h1'), 1, 3)
    for peep in info:
        text += gen_html_table(peep, info[peep])
    text = html_wrap(text, 'body')
    otext += text
    return "<!DOCTYPE html>\n" + html_wrap(otext, 'html')

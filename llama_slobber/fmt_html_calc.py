#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Given the results of a get_rundle_comp call, generate a web page to display
those values.
"""


def html_wrap(ptext, owrapper, attribute=''):
    """
    Wrap text with html tags.

    Input:
        ptext -- text to be wrapped
        owrapper -- tag to wrap ptext with
        attribute -- if set, attribute to add to ptext

    If owrapper ends with a newline, then the newline will appear after the
    bracket character in the last tag.

    Returns the wrapped string value.
    """
    wrapper = owrapper.strip()
    hdr = '<%s>' % wrapper
    if attribute:
        hdr = add_attrib(attribute, hdr)
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


def gen_html_table(def_head, data, attribute='', tabhdrs=False):
    """
    Generate an html table for a user.

    Input:
        def_head -- dict key used as header for entire table if no other
                    headers are specified.
        data -- tuples of information used to make rows in the table
        attribute -- if set, attribute to add to table.
        tabhdrs -- if set, table of headers to be used.  If this entry
                   is a list of a list of headers, then both def_head
                   and this set of headers are used.

    Returns a snippet of html code representing this table
    """
    both = False
    if tabhdrs:
        if len(tabhdrs) == 1:
            both = True
            tabhdrs = tabhdrs[0]
    hsize = len(data[0])
    disp = ''
    if both or not tabhdrs:
        disp = html_wrap(def_head, 'th')
        disp = add_attrib('colspan="%d"' % hsize, disp)
        disp = html_wrap(disp, 'tr\n')
    if tabhdrs:
        for field in tabhdrs:
            disp += html_wrap(field, 'th')
        disp = html_wrap(disp, 'tr\n')
    for ptuple in data:
        tline = ''
        for field in ptuple:
            tline += html_wrap(field, 'td')
        tline = html_wrap(tline, 'tr\n')
        disp += tline
    return html_wrap(disp, 'table\n', attribute=attribute)


def gen_html_page(info, title, header, centered=False, tabhdrs=False):
    """
    Generate an html page for get_rundle_comp data

    Input:
        info -- the get_rundle_comp data to be displayed
        title -- text for the page's title
        header -- text for the large centered text at the top of the page
        centered -- if true, table will be centered rather than float left.

    Returns:
        Web page contents as a string
    """
    otext = html_wrap(title, 'title\n')
    if centered:
        float_pt = ''
    else:
        float_pt = ' float: left;'
    css_info = """h1 { text-align: center } p { text-align: center }
              table {%s border: 1px solid black; margin: 12px; }
              td { border: 1px solid black; text-align: center }
              th { border: 1px solid black; text-align: center }""" % float_pt
    if centered:
        css_info += """table.center { margin-left:auto; margin-right:auto;}"""
    css_info = html_wrap(css_info, 'style\n')
    css_info = html_wrap(css_info, 'head\n')
    otext += css_info
    text = add_breaks(html_wrap(header, 'h1'), 1, 2)
    text += '<p></p><br>'
    for peep in info:
        if centered:
            text += gen_html_table(peep, info[peep],
                                   attribute="class='center'",
                                   tabhdrs=tabhdrs)
        else:
            text += gen_html_table(peep, info[peep], tabhdrs=tabhdrs)
    text = html_wrap(text, 'body')
    otext += text
    return "<!DOCTYPE html>\n" + html_wrap(otext, 'html')


def inject_text(htmltext, intext):
    """
    Insert text from a file into an html string.

    Arguments:
        htmltext -- string where text will be added.
        intext -- input file

    Returns: text with intext added between <p></p> characters
    """
    parts = htmltext.split('<p></p>')
    with open(intext, 'r') as infile:
        adddata = infile.read()
    return "%s<p>%s</p>%s" % (parts[0], adddata, parts[1])

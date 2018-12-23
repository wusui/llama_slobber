# LLAMA SLOBBER FORMATTING

Extra methods used to either format data, interface to json files, or perform
specialized I/O.

***

### format_float(number, decimal_places)

Arguments:
  * number -- floating point number to be formatted.
  * decimal_places -- number of decimal places to be displayed
  
Returns -- a string representation of the number.

This method can be used to format floating point numbers for display.
If an integer is passed for number, then the fractional display will be
padded with zeroes.  There will be a minimum of one digit to the right
of the decimal point.  Values are rounded.

***

### gen_html_table(header, data, centered=False)

Arguments:
  * header -- user whose data will be formatted into a table
  * data -- tuples of information used to make rows in the table
  * centered -- keyword argument.  If True, tale is centered on page.
                (defaults to float left)

Generates a portion of html text that is table composed from the data
passed in the data parameter.  In most cases, header is a key from the
result of a get_rundle_comp call, and data is the corresponding value.

***

### gen_html_page(info, title, header, attribute='')

Arguments:
  * info -- the get_rundle_comp data to be displayed
  * title -- text for the title at the top of the html tab
  * header -- text for the large centered text at the top of the page
  * attribute -- keyword parameter, if not empty, attribute to be added
                 to '<table>' html statements.

Generates the text for an html file based on the information in info.  The
html file generated will consist of a set of tables where each table will be
extracted from an entry in info.

***

### out_csv_file(out_csv, in_json, field)

Arguments:
  * out_csv -- csv file to be written
  * in_json -- json file containing the data to be written
  * field -- field in in_json

Output a csv file whose entries consist of the keys and the corresponding 
passed in field for the json file passed in.

***

### lookup_user(directory, in_text)

Arguments:
 * directory -- directory where every file name has the form "x__y.json"
                x and y are alphabetically ordered entries, and every
                    entry in that file is within the range of x and y.
 * in_text -- text to scan for.

Find the appropriate file name in directory that contains an entry in in_text.
The scan assumes that the name is in the correct file.  If it can not be found
because the name is not within any of the boundaries of the file names, then
the file name returned is a valid file name but does not contain the entry.

***

### inject_text(htmltext, intext)

Arguments:
  * htmltext -- string where text will be added.
  * intext -- input file

Read intext file. Return htmltext with intext contents added in what was a
prevously blank parargraph.

***

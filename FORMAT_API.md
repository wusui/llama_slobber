# LLAMA SLOBBER FORMATTING

Extra methods used to format data

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

### gen_html_table(header, data)

Arguments:
  * header -- user whose data will be formatted into a table
  * data -- tuples of information used to make rows in the table

Generates a portion of html text that is table composed from the data
passed in the data parameter.  In most cases, header is a key from the
result of a get_rundle_comp call, and data is the corresponding value.

***

### gen_html_page(info, title, header)

Arguments:
  * info -- the get_rundle_comp data to be displayed
  * title -- text for the title at the top of the html tab
  * header -- text for the large centered text at the top of the page

Generates the text for an html file based on the information in info.  The
html file generated will consist of a set of tables where each table consists
of the data for a person in the rundle.


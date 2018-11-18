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

##### USAGE

```python
from llama_slobber import format_float
.
.
.
# This line will print 0.50
print(format_float(.497, 2))
```

This should print out .48


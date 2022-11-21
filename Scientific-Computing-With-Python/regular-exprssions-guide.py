"""
Regular expressions in python: 'import re'
    - re.search(), re.findall()
    - https://docs.python.org/3/howto/regex.html
    - quick reference guide:
        - ^ matches the beginning of a line
        - [^ ] means not a blank, notice the blank inside []
        - $ matches the end of the line
        - . matches any character
        - \s matches whitespace
        - \S matches any non-whitespace character
        - '*' without '' repeats a character zero or more times # greedy returns longest possible match
        - '*?' without '' repeats a character zero or more times (non-greedy) # non-greedy returns shortest possible match
        - '+' without '' repeats a character one or more times # greedy returns longest possible match
        - '+?' without '' repeats a character one or more times (non-greedy) # non-greedy returns shortest possible match
        - [aeiou] matches a single character in the listed set 'aeiou'
        - [^XYZ] matches a single character not in the listed set 'XYZ'
        - [a-z0-9] the set of characters can include a range 'a-z''0-9'
        - '(' without '' indicates where string extraction is to start
        - ')' without '' indicates where string extraction is to stop
        - '\' without '' prefex for when you want to search for something that is in above list: \$ is an example
"""
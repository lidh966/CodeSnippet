#### Using startswith() and endswith() method to match text at the start and end of a string ####

filename = 'spam.txt'
filename.endswith('.txt')    # >>> True

url = 'http://www.python.org'
url.startswith('ftp:')    # False
url.startswith('http:')    # >>> True

# Multiple choices
# The patterns must be included in a tuple!!!
choices = ('http:', 'ftp:')    # Put the choices in a tuple is required
url = 'http://www.python.org'
url.startswith(choices)
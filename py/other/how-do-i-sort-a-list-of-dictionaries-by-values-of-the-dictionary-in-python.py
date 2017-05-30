# http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python

example = [
    {'name':'Homer', 'age':39},
    {'name':'Bart', 'age':10},
]

sorted = [
    {'name':'Bart', 'age':10},
    {'name':'Homer', 'age':39},
]

example = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]


#################

newlist = sorted(example, key=lambda k: k['name'])
print newlist
# TypeError: 'list' object is not callable

from operator import itemgetter
newlist = sorted(example, key=itemgetter('name'))
print newlist
# TypeError: 'list' object is not callable

# For completeness, add reverse=True to sort descending
newlist = sorted(example, key=itemgetter('name'), reverse=True)

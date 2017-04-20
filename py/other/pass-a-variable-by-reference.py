# class PassByReference:
#     def __init__(self):
#         self.variable = 'Original'
#         self.change(self.variable)
#         print(self.variable)
# 
#     def change(self, var):
#         var = 'Changed'
#         print('var --> ', var)
# 
# a = PassByReference()

# OUT:
# ('var --> ', 'Changed')
# Original


# Try to modify the list that was passed to a method
def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('change to', the_list)

outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)

# Python3 Out:
# before, outer_list = ['one', 'two', 'three']
# got ['one', 'two', 'three']
# change to ['one', 'two', 'three', 'four']
# after, outer_list = ['one', 'two', 'three', 'four']


# String - an immutable type
# It's immutable, so there's nothing we can do to change the contents of the string

# Try to change the reference
def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the see'
    print('set to', the_string)

outer_string = 'It was many and many a year ago'

print('before, outer_string = ', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string = ', outer_string)

# Python 3 Out:
# before, outer_string =  It was many and many a year ago
# got It was many and many a year ago
# set to In a kingdom by the see
# after, outer_string =  It was many and many a year ago


def return_a_whole_new_string(the_string):
    new_string = something_to_do_with_the_old_string(the_string)
    return new_string

my_string = return_a_whole_new_string(my_string)

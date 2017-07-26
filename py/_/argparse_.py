import argparse
parser = argparse.ArgumentParser(description='Descr...')
parser.add_argument('-f', '--foo', required=True)
parser.add_argument('-b', '--bar', required=True)
args = vars(parser.parse_args())

if args['foo'] == 'hello':
    print 'you say hello'

if args['bar'] == 'world':
    print 'you say world'

# ~/play python argparse_.py -f hello -b world
# you say hello
# you say world

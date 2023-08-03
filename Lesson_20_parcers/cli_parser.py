from argparse import ArgumentParser

parser = ArgumentParser(description='Parser for numbers arguments in this file')
#
# parser.add_argument('--number_1', help='Integer range 1-100', default=5)
# parser.add_argument('--number_2', help='Integer range 1-10', default=5)
#
# args = parser.parse_args()
#
# print(f'{args.number_1} + {args.number_2} = {args.number_1 + args.number_2}')

class Chrome:
    def __init__(self):
        print('CHROME')

class FireFox:
    def __init__(self):
        print('FireFox')


parser.add_argument('--browser', help='browser name', default='chrome')
browser = parser.parse_args().browser

if browser.lower() == 'chrome':
    Chrome()
elif browser.lower() == 'firefox':
    FireFox()
else:
    Chrome()

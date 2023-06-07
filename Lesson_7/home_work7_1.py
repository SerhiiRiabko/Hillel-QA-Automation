import sys


def custom_print(*args, sep=' ', end='\n'):
    output = sep.join(str(arg) for arg in args) + end
    sys.stdout.write(output)


custom_print('Test')

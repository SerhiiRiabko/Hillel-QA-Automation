class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year


class Bus:
    def __init__(self, model, year):
        self.model = model
        self.year = year


def transport_factory(transport_type, *args, **kwargs):
    if transport_type.lower() == 'car':
        return Car(*args, **kwargs)

    elif transport_type.lower() == 'bus':
        return Bus(*args, **kwargs)

    else:
        print('No this class in system')


if __name__ == '__main__':
    my_transport = transport_factory('car', 'tesla', 2017)
    my_transport_2 = transport_factory('bus', 'Laz', 1967)


# example

class Chrome:
    def __init__(self):
        print('I am Chrome')


class Safari:
    def __init__(self):
        print('I am Safari on Mac')


class Firefox:
    def __init__(self):
        print('I am FireFox')


def browser_factory(browser, *args, **kwargs):
    if browser.lower() == 'chrome':
        return Chrome()

    elif browser.lower() == 'safari':
        return Safari()

    elif browser.lower() == 'firefox':
        return Firefox()

    else:
        print('Some other browser')
        # or add some default - return Chrome()
        return Chrome()


if __name__ == '__main__':
    browser_factory('Chrome')
    browser_factory('Firefox')
    browser_factory('Safari')
    browser_factory('Edge')
    c = 0

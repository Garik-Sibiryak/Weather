"""
    Modul that creates the dictionary with the declined names
    of Russian cities for correct spelling in the weather forecast.
"""


def file_read(city):
    """
        This function accepts the parameter "city". It reads .txt
        file line by line, extracts values by index, passes
        them to the variables and creates a dictionary. If
        the dictionary contains the key identical to the value
        from the accepted parameter, the function returns the value
        of this key.
    :param city: accepts the name of a city
    :return: cities_dict[city]
    """

    keys = []
    values = []
    cities_dict = {}

    with open('Russian_cities.txt', encoding='utf-8') as cdb:
        for i in cdb:
            t = i.split(',')
            keys = t[0]
            values = t[-1]
            cities_dict = {keys: values}
            if city in cities_dict:
                yield cities_dict[city]


c = 'Омск'
p = file_read(c)

if __name__ == "__main__":
    print(next(p))

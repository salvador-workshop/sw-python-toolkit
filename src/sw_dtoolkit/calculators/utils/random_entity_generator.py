import random
from random import randrange
from datetime import datetime, timedelta

class RandomEntityGenerator:
    def __init__(self):
        self.data = []

        # self.bandNames = open("../data/band-names.txt", "r", encoding='utf-8')
        # self.albumNames = open("../data/album-names.txt", "r", encoding='utf-8')
        # self.cityNames = open("../data/city-names.txt", "r", encoding='utf-8')
        # self.countryNames = open("../data/country-names.txt", "r", encoding='utf-8')
        # self.genreNames = open("../data/genre-list.txt", "r", encoding='utf-8')
        # self.businessNames = open("../data/business-names.txt", "r", encoding='utf-8')
        # self.businessIndustryList = open("../data/business-industry-list.txt", "r", encoding='utf-8')
        # self.countryCodes = open("../data/country-codes.txt", "r", encoding='utf-8')
        # self.streetNames = open("../data/street-names.txt", "r", encoding='utf-8')
        # self.personNames = open("../data/person-names.txt", "r", encoding='utf-8')

        # TODO -- reorganize "gd-name-gen" code into generalized funcs
        # usable by several calculators
        #     + random_line_from_file(file_path)
        #     + random_person()
        #     + random_address()
        #     + random_datetime(start_date, end_date)
        #     + random_business_name()
        #     + random_business_industries(num_industries)
        #     + random_music_act()
        #     + random_music_genres(num_genres)
        #     + random_music_album(num_tracks)

    def random_line_from_file(self, afile, default=None):
        line = default
        for i, aline in enumerate(afile, start=1):
            if randrange(i) == 0:  # random int [0..i)
                line = aline
        return line.rstrip()

    def random_num_string(self):
        r_num = random.randint(1, 9999)
        return f'{r_num:04}'

    def random_person(self):
        pName = random_line(personNames).rstrip()
        pPhone = f'{random_num_string()}-{random_num_string()}{random_num_string()}'
        return f'{pName}\n{pPhone}'

    def random_address(self):
        addr_num = random.randint(1, 3999)
        addr_street = random_line(streetNames).rstrip()
        addr_city = random_line(cityNames).rstrip()
        addr_country = random_line(countryNames).rstrip()
        addr_phone = f'{random_num_string()}-{random_num_string()}{random_num_string()}'

        random_address = f'{addrNum} {addrStreet}\n{addrCity}, {addrCountry}\n{addrPhone}'
        return random_address

    def random_datetime(self, start_date, end_date):
        """
        This function will return a random datetime between two datetime 
        objects.
        """
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start_date + timedelta(seconds=random_second)

    def random_business_name(self):
        return None

    def random_business_industries(self, num_industries):
        for x in range(num_industries):
            business_industry_list.seek(0)
            bus_industries += f'- {random_line(business_industry_list).rstrip()}\n'
        loopStr += f'{bus_industries}\n'
        return loopStr;

    def random_music_act(self):
        return None

    def random_music_genres(self, num_genres):
        return None

    def random_music_album(self, num_tracks):
        return None

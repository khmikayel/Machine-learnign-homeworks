from bs4 import BeautifulSoup
import re


class Parser:

    def parse_object(self, content):

        return [self.get_property(content, i) for i in range(0, 8)]

    def get_property(self, content, property_ind):

        all_raw_properties = re.findall('<th[^^]*?</th>|<td[^^]*?</td>', content)
        raw_property = all_raw_properties[property_ind]
        soup = BeautifulSoup(raw_property, features="html.parser")

        return soup.text.replace('\n', '')
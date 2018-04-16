import CV

class XpathGEN(object):
    def __init__(self, soup, tag, maxp_layer=3):
        self.soup = soup
        self.tag = tag
        self.p_layers = maxp_layer
        self.allow_attr = ['id', 'class', 'style']
        self.xpath = []

    def generate_string(self, tag_attrs, attr):
        attr_value = tag_attrs[attr]
        if type(attr_value) is list:
            attr_value = ' '.join(attr_value)
        return '@%s="%s"' % (attr, attr_value)

    def parse_tag(self, tag):
        if tag is None:
            return 'Can not match the conditions!'
        tag_name = tag.name
        tag_attrs = tag.attrs

        for attr in self.allow_attr:
            if attr in tag_attrs:
                _string = self.generate_string(tag_attrs, attr)
                return '%s[%s]' % (tag_name, _string)
        return tag_name

    def get_tags_parents(self, plevel):
        tag = self.tag
        self.xpath.append(self.parse_tag(tag))
        while plevel >= 1:
            self.xpath.append(self.parse_tag(tag.parent))
            tag = tag.parent
            plevel -= 1

    def get_xpath(self):
        if self.tag is None:
            return {'xpath': ['Did not match the conditions!']}
        plevel = 1
        while plevel <= self.p_layers:
            self.get_tags_parents(plevel)
            self.xpath.reverse()
            re_xpath = '//'+'/'.join(self.xpath)
            if self.check_xpath(re_xpath):
                break
            else:
                plevel += 1
        return re_xpath
        
    def check_xpath(self, re_xpath):
        driver = CV.BROWSER
        elements = driver.find_elements_by_xpath(re_xpath)
        if len(elements) == 1:
            return True
        else:
            return False

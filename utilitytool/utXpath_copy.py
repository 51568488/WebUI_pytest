class XpathGEN1(object):
    def __init__(self, soup, tags, parent_layers=2):
        self.soup = soup
        self.tags = tags
        self.p_layers = parent_layers
        self.allow_attr = ['id', 'class', 'style']
        self.xpaths = []

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

    def get_tags_parents(self, tags):
        while self.p_layers > 0:
            tag_parents_xpath = []
            _tags = []
            for tag in tags:
                tag_parents_xpath.append(self.parse_tag(tag.parent))
                _tags.append(tag.parent)
            self.xpaths.append(tag_parents_xpath)

            self.p_layers -= 1
            self.get_tags_parents(_tags)

    def get_xpaths(self):
        first_tags = self.tags
        if first_tags is None:
            return {'xpath': ['Did not match the conditions!']}
        self.get_tags_parents(first_tags)

        re_xpaths = []
        for x in map(lambda x: list(x), zip(*self.xpaths)):
            x.reverse()
            re_xpaths.append('//'+'/'.join(x))
        return list(set(re_xpaths))
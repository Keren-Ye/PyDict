#coding: utf-8

class trieTree():
    def __init__(self, source, key_index = 0, codec = 'utf-8'):
        self.codec = codec
        self.key_index = key_index

        self.root = dict()

        try:
            self.load(source)
        except Exception, e:
            raise Exception, e

    def load(self, source):
        try:
            file = open(source, 'r')
            for line in file:
                line = line.strip().decode(self.codec)

                items = line.split('\t')
                if len(items) > self.key_index:
                    self.insert(items[self.key_index], items)

            file.close()
        except Exception, e:
            raise Exception, e

    def insert(self, key, value):
        root = self.root

        for ch in key:
            if not ch in root:
                root[ch] = dict()

            root = root[ch]

        if not 'DATA' in root:
            root['DATA'] = list()
        root['DATA'].append(value)

    def search(self, key):
        key = key.decode(self.codec)
        root = self.root

        for ch in key:
            if not ch in root:
                return []

            root = root[ch]

        if not 'DATA' in root:
            return []

        return root['DATA']

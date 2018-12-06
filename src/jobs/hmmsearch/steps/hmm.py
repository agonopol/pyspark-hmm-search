class MatrixBuilder(object):
    def __init__(self, alphabet):
        super(MatrixBuilder, self).__init__()
        self.alphabet = list(filter(lambda x: x != "", alphabet.split(" ")))
        self.matrix, self.begin, self.node, self.compo = {}, None, None, None

    def append(self, line):
        parts = list(filter(lambda x: x != '', line.replace("*", "0").split(" ")))
        if parts[0].isdigit():
            self.node = parts[0].strip()
            self.matrix[self.node] = {}
            self.matrix[self.node]["match"] = list(map(float, parts[1:len(self.alphabet) + 1]))
            self.matrix[self.node]['map'] = parts[len(self.alphabet) + 1]
            self.matrix[self.node]['cons'] = parts[len(self.alphabet) + 2]
            self.matrix[self.node]['rf'] = parts[len(self.alphabet) + 3]
            self.matrix[self.node]['mm'] = parts[len(self.alphabet) + 4]
            self.matrix[self.node]['cs'] = parts[len(self.alphabet) + 4]
        elif self.node:
            if 'insertion' in self.matrix[self.node]:
                self.matrix[self.node]['transition'] = list(map(float, parts[1:]))
            else:
                self.matrix[self.node]['insertion'] = list(map(float, parts[1:]))
        elif parts[0] == "COMPO":
            self.compo = list(map(float, parts[1:]))
        elif self.compo and self.begin:
            self.begin.append(list(map(float, parts[1:])))
        elif self.compo and not self.begin:
            self.begin = list(map(float, parts[1:]))

    def build(self):
        return {"alphabet": self.alphabet, "matrix": self.matrix, 'compo': self.compo, 'begin': self.begin}


def parse(stream):
    hmm, matrix = {}, None
    for line in map(lambda x: x.strip(), stream.readlines()):
        if line == "//":
            hmm["HMM"] = matrix.build()
            yield hmm
            hmm = {}
            matrix = None
        elif matrix:
            matrix.append(line)
        else:
            parts = line.split(" ")
            if parts[0] == "HMM":
                matrix = MatrixBuilder(" ".join(parts[1:]).strip())
            else:
                hmm[parts[0]] = " ".join(parts[1:]).strip()

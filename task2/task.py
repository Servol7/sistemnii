import csv

class r:
    def __init__(self, r1, r2, r3, r4, r5):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.r5 = r5

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = {}
        self.r = r(0, 0, 0, 0, 0)

    def append(self, value):
        node = self.__class__(value, parent=self)
        self.children[value] = node
        return node

    def dfs(self, func):
        func(self)
        for child in self.children.values():
            child.dfs(func)

    def find(self, value):
        if self.value == value:
            return self
        for child in self.children.values():
            res = child.find(value)
            if res:
                return res

    def set_relations(self):
        for child in self.children.values():
            self.r.r1 += 1
            child.r.r2 += 1
            child.r.r5 = len(self.children) - 1
            for grandchild in child.children.values():
                grandchild.dfs(self._set_inderect)
            child.set_relations()

    def _set_inderect(self, node):
        self.r.r3 += 1
        node.r.r4 += 1

def task(tree):
    rows = [row.split(",") for row in tree.splitlines()]
    root = Node(rows[0][0])
    for row in rows:
        root.find(row[0]).append(row[1])
    root.set_relations()
    nodes = []
    root.dfs(nodes.append)
    res = ""
    for node in sorted(nodes, key=lambda node: node.value):
        res += f"{node.r.r1},{node.r.r2},{node.r.r3},{node.r.r4},{node.r.r5}\n"
    print(res)


file_=input()
with open(file_, 'r') as file_r:
    csv_r = csv.reader(file_r, delimiter=",")
    L = list(csv_r)
data = ""
for i in L:
    data += ",".join(i)
    data += "\n" 

task(data)

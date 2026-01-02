'''
Data Structures/Types
format: ntuple
(name,type,file)
'''

class Scan:
    def __init__(self, fpath: str):
        self.fpath = fpath
        self.files = []
        self.data_structures = []

    def visualize(self):
        pass

class Scanner:
    def __init__(self):
        pass

    def scan(self, fpath: str) -> Scan:
        data_structures: dict = {}
        scan = Scan(fpath)

        # TODO:
        #   - scan for: struct, typedef, define
        #   - tuple them with source file name
        #   - add them to scan

        return scan

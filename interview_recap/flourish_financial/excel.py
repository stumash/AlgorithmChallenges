# Today we’re going to build a basic spreadsheet application like Google sheets or Excel but much simpler. Our spreadsheet, let’s call it OpenSheet, will only support cells which hold either integers or formulas that sum two cells.

# You are tasked with writing a program that handles this functionality for OpenSheet. You can make any decisions you want regarding how this program is organized, but there must be some sort of setter/getter methods that can be called by the application for any given cell. All inputs will be strings.

# For setting you can expect two inputs: the cell location and the cell value.

# Example of how your setter could look
# set_cell("C1", "45")
# set_cell("B1", "10")
# set_cell("A1", "=C1+B1")

# For getting you will be provided one input that is the cell location.

# Example of how your getter could look
# set_cell("C1", "45")
# set_cell("B1", "10")
# set_cell("A1", "=C1+B1")
# get_cell("A1") # should return 55 in this case

# Now let’s assume that the way our users use OpenSheet results in considerably higher amounts of value reading than value setting, which means our application needs to be optimized for reading in order to give our users the best experience possible. Given this constraint, how can we optimize this implementation to improve performance?

from typing import Dict
from collections import defaultdict

class ExcelSheet:
    def __init__(self):
        # simple key-value pair. for a given cell, get the user-provided value, raw
        self.sheet: Dict[str, str] = defaultdict(lambda: '0')

        # for a list of cells, get the cached value of that cell
        self.memo: Dict[str, int] = {}

        # for a given cell name, get list of cells that depend on it directly
        self.graph_dependants = defaultdict(set)

    def get_cell(self, cell_name: str) -> int:
        if cell_name not in self.memo:
            s = self.sheet[cell_name]
            if len(s) > 0 and s[0] == '=':
                [cell1, cell2] = s[1:].split('+')
                self.memo[cell_name] = self.get_cell(cell1) + self.get_cell(cell2)
            else:
                self.memo[cell_name] = int(s)
        return self.memo[cell_name]

    def set_cell(self, cell_name: str, value: str):
        old_value = self.sheet[cell_name]
        self.sheet[cell_name] = value
        self.invalidate_memo(cell_name)
        if len(old_value) > 0 and old_value[0] == '=':
            [cell1, cell2] = old_value[1:].split('+')
            if cell1 in self.graph_dependants:
                self.graph_dependants[cell1].remove(cell_name)
                if len(self.graph_dependants[cell1]) == 0:
                    del self.graph_dependants[cell1]
            if cell2 in self.graph_dependants:
                self.graph_dependants[cell2].remove(cell_name)
                if len(self.graph_dependants[cell2]) == 0:
                    del self.graph_dependants[cell2]
        if len(value) > 0 and value[0] == '=':
            [cell1, cell2] = value[1:].split('+')
            self.graph_dependants[cell1].add(cell_name)
            self.graph_dependants[cell2].add(cell_name)
        self.re_get_dependants(cell_name)

    def invalidate_memo(self, cell_name: str):
        if cell_name in self.memo:
            del self.memo[cell_name]
        if cell_name not in self.graph_dependants:
            return
        for dependant in self.graph_dependants[cell_name]:
            self.invalidate_memo(dependant)

    def re_get_dependants(self, cell_name):
        self.get_cell(cell_name)
        if cell_name in self.graph_dependants:
            for dependant in self.graph_dependants[cell_name]:
                self.re_get_dependants(dependant)

    def __repr__(self) -> str:
        return '\n'.join([
            'ExcelSheet',
            f'  sheet: {dict(self.sheet)}',
            f'  memo: {self.memo}',
            f'  deps: {dict(self.graph_dependants)}',
        ])


sheet = ExcelSheet()

sheet.set_cell("C1", "45")
print(sheet)

sheet.set_cell("B1", "10")
print(sheet)

sheet.set_cell("A1", "=C1+B1")
print(sheet)

sheet.set_cell("D1", "=A1+B1")
print(sheet)

sheet.set_cell("A1", "5")
print(sheet)

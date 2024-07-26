from project.table.table import Table


class OutsideTable(Table):
    @property
    def _min_num(self):
        return 51

    @property
    def _max_num(self):
        return 100

    @property
    def _type(self):
        return "Outside"



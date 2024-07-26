from project.table.table import Table


class InsideTable(Table):
    @property
    def _min_num(self):
        return 1

    @property
    def _max_num(self):
        return 50

    @property
    def _type(self):
        return "Inside"

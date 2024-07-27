class Major:
    def __init__(self, id, name, id_dean):
        self.id = id
        self.name = name
        self.id_dean = id_dean

    def __str__(self):
        return f"{self.id} - {self.name} - {self.id_dean}"

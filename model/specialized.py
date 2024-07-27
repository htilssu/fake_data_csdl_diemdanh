class Specialized:
    def __init__(self, id, name, major_id):
        self.id = id
        self.name = name
        self.major_id = major_id

    def __str__(self):
        return f"Specialize: {self.name} - {self.major_id}"

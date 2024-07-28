class Room:
    def __init__(self, name, campus_id):
        self.name = name
        self.campus_id = campus_id

    def __str__(self):
        return f"Room(name={self.name}, campus_id={self.campus_id})"

    def __repr__(self):
        return f"Room(name={self.name!r}, campus_id={self.campus_id!r})"

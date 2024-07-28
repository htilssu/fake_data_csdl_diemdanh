class Subject:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

        # Validate credit
        if not (0 <= self.credit <= 7):
            raise ValueError("Credit must be between 0 and 7")

    def __str__(self):
        return f"Subject(id={self.id}, name={self.name}, credit={self.credit})"

    def __repr__(self):
        return f"Subject(id={self.id!r}, name={self.name!r}, credit={self.credit!r})"

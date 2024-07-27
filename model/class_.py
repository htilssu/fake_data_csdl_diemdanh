class Class:
    def __init__(self, name, spec_id, fal_advisor_id):
        self.name = name
        self.spec_id = spec_id
        self.fal_advisor_id = fal_advisor_id

    def __str__(self):
        return f"Class: {self.name} - {self.spec_id} - {self.fal_advisor_id}"
class ClassSection:
    def __init__(self, id, id_subject, id_room, id_lecturer, start, end, day_of_week):
        self.id = id
        self.id_subject = id_subject
        self.id_room = id_room
        self.id_lecturer = id_lecturer
        self.start = start
        self.end = end
        self.day_of_week = day_of_week

        if not (2 <= self.day_of_week <= 7):
            raise ValueError("DayOfWeek must be between 2 and 7")

    def __str__(self):
        return (f"ClassSection(id={self.id}, id_subject={self.id_subject}, "
                f"id_room={self.id_room}, id_lecturer={self.id_lecturer}, start={self.start}, "
                f"end={self.end}, day_of_week={self.day_of_week})")

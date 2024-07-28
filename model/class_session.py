import uuid
from datetime import datetime


class ClassSession:
    def __init__(self, id_class_section: str, time: datetime, id_room: str, id_lecturer: str,
                 id: str = None):
        self.id = id or str(uuid.uuid4())
        self.id_class_section = id_class_section
        self.time = time
        self.id_room = id_room
        self.id_lecturer = id_lecturer

    def __repr__(self):
        return (f"ClassSession(id={self.id}, id_class_section={self.id_class_section}, "
                f"time={self.time}, id_room={self.id_room}, id_lecturer={self.id_lecturer})")

    def save_to_db(self, connection):
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO ClassSession (Id, Id_ClassSection, Time, Id_Room, Id_Lecturer)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.id, self.id_class_section, self.time, self.id_room, self.id_lecturer))
            connection.commit()
        except:
            print("Lỗi khi thêm class_session")

    @classmethod
    def get_by_class_section(cls, conn, classss):
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM ClassSession WHERE Id_ClassSection = ?
        ''', classss)
        rows = cursor.fetchall()
        cursor.close()
        return [cls(row.Id_ClassSection, row.Time, row.Id_Room, row.Id_Lecturer, row.Id) for row in
                rows]

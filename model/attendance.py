import uuid


class Attendance:
    def __init__(self, id, id_class_session, id_student, time, status, remark=None,
                 id_lecturer=None):
        self.id = id or str(uuid.uuid4())
        self.id_class_session = id_class_session
        self.id_student = id_student
        self.time = time
        self.status = status
        self.remark = remark
        self.id_lecturer = id_lecturer

    def __repr__(self):
        return (f"Attendance(Id={self.id}, Id_ClassSession={self.id_class_session}, "
                f"Id_Student={self.id_student}, Time={self.time}, Status={self.status}, "
                f"Remark={self.remark}, Id_Lecturer={self.id_lecturer})")

    def save_to_db(self, conn):
        try:
            cursor = conn.cursor()
            # Câu lệnh SQL để chèn dữ liệu
            sql = '''
            INSERT INTO dbo.Attendance (Id, Id_ClassSession, Id_Student, Time, Status, Remark, 
            Id_Lecturer)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(sql, (
                self.id, self.id_class_session, self.id_student, self.time, self.status,
                self.remark,
                self.id_lecturer))
            cursor.commit()
            cursor.close()
        except Exception as e:
            print("An error occurred:", e)

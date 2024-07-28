class Study:
    def __init__(self, id_student, id_class_section):
        self.id_student = id_student
        self.id_class_section = id_class_section

    def __str__(self):
        return f'{self.id_student}, {self.id_class_section}'

    def save_to_db(self, conn):
        try:
            # Kết nối tới SQL Server
            cursor = conn.cursor()

            # Câu lệnh SQL để chèn dữ liệu
            sql = '''
            INSERT INTO dbo.Study (Id_Student, Id_ClassSection)
            VALUES (?, ?)
            '''

            # Thực hiện câu lệnh SQL với các giá trị của đối tượng
            cursor.execute(sql, (self.id_student, self.id_class_section))
            conn.commit()
            cursor.close()
        except Exception as e:
            print("An error occurred:", e)

    @staticmethod
    def get_students_by_class_section(conn, id_class_section):
        try:
            # Kết nối tới SQL Server

            cursor = conn.cursor()

            # Câu lệnh SQL để lấy danh sách ID sinh viên
            sql = '''
            SELECT Id_Student
            FROM dbo.Study
            WHERE Id_ClassSection = ?
            '''

            # Thực hiện câu lệnh SQL với id_class_section
            cursor.execute(sql, id_class_section)
            rows = cursor.fetchall()

            # Trả về danh sách ID sinh viên
            student_ids = [row[0] for row in rows]
            cursor.close()
            return student_ids
        except Exception as e:
            print("An error occurred:", e)
            return []

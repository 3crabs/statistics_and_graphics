import xlwt
import os
from dataclasses import dataclass


def create_xls_grade():
    items = []
    for i in range(0, 10):
        items.append(GradeItems(name="Тест Name", type="Тест Type", grade="25.00", user_modified="Тест Иван Иванов", max_grade="100"))
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("ntcn")
    row = 0
    sheet.write(row, 0, "Результаты")
    row += 1
    sheet.write(row, 0, "Студент")
    sheet.write(row, 1, "Иван Иванов")
    row += 1
    sheet.write(row, 0, "Курс")
    sheet.write(row, 1, "Курс Тест")
    row += 1
    sheet.write(row, 0, "№")
    sheet.write(row, 1, "Элемент")
    sheet.write(row, 2, "Тип")
    sheet.write(row, 3, "Оценка")
    sheet.write(row, 4, "Максимальная оценка")
    sheet.write(row, 5, "Оценил")
    for i, val in enumerate(items):
        row += 1
        sheet.write(row, 0, i + 1)
        sheet.write(row, 1, val.name)
        sheet.write(row, 2, val.get_type())
        sheet.write(row, 3, val.get_grade())
        sheet.write(row, 4, val.max_grade)
        sheet.write(row, 5, val.get_user_modified())

    path = os.path.curdir + "\\xml\\spreadsheet-" + str(11) + "-" + str(30113) + ".xlsx"
    book.save(path)
    return path


@dataclass
class GradeItems:
    name: str
    type: str
    grade: str
    user_modified: str
    max_grade: str

    def get_type(self):
        if self.type == 'quiz':
            return "Тест"
        elif self.type == 'assign':
            return "Задание"
        elif self.type == 'lesson':
            return "Лекция"
        else:
            return "-"

    def get_grade(self):
        if self.grade:
            return str(self.grade)
        return str(self.grade_min)

    def get_user_modified(self):
        if self.user_modified:
            return str(self.user_modified)
        return 'Система'

if __name__ == '__main__':
    create_xls_grade()
import xlwt
import os
from dataclasses import dataclass


def create_xls_grade():
    items = []
    for i in range(0, 10):
        items.append(GradeItems(name="Тест Name", type="Тест Type", grade="25.00", user_modified="Тест Иван Иванов",
                                max_grade="100"))
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


def create_xls_grade():
    items = []
    for i in range(0, 10):
        items.append(GradeItems(name="Тест Name", type="Тест Type", grade="25.00", user_modified="Тест Иван Иванов",
                                max_grade="100"))
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


def create_xls_info_course():
    items = []
    for i in range(0, 10):
        items.append(InfoCourse(name="Тест Name", last_access="May 16, 2020 2:11am", final_grade="25.00", max_grade="100"))
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Инфо")
    row = 0
    sheet.write(row, 0, "Информация о курсе")
    row += 1
    sheet.write(row, 0, "Преподаватель")
    sheet.write(row, 1, "Иван Иванов")
    row += 1
    sheet.write(row, 0, "Курс")
    sheet.write(row, 1, "Курс Тест")
    row += 1
    sheet.write(row, 0, "№")
    sheet.write(row, 1, "ФИО студента")
    sheet.write(row, 2, "Последний доступ")
    sheet.write(row, 3, "Итоговая оценка")
    sheet.write(row, 4, "Максимальная оценка")
    for i, val in enumerate(items):
        row += 1
        sheet.write(row, 0, i + 1)
        sheet.write(row, 1, val.name)
        sheet.write(row, 2, val.last_access)
        sheet.write(row, 3, val.final_grade)
        sheet.write(row, 4, val.max_grade)

    path = os.path.curdir + "\\xml\\spreadsheet-" + str(11) + "-" + str(30113) + ".xlsx"
    book.save(path)
    return path


@dataclass
class InfoCourse:
    name: str
    last_access: str
    final_grade: str
    max_grade: str


if __name__ == '__main__':
    create_xls_info_course()

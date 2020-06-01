import os

import xlwt


def create_xls_grade(student_name: str, course_name: str, items: [], end_grade: str):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Результаты")
    row = 0
    sheet.write(row, 0, "Результаты")
    row += 1
    sheet.write(row, 0, "Студент")
    sheet.write(row, 1, student_name)
    row += 1
    sheet.write(row, 0, "Курс")
    sheet.write(row, 1, course_name)
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
        sheet.write(row, 4, val.grade_max)
        sheet.write(row, 5, val.get_user_modified())
    row += 1
    sheet.write(row, 0, "Итоговая")
    sheet.write(row, 1, end_grade)

    path = "index/xml/results.xlsx"
    book.save(path)
    return path

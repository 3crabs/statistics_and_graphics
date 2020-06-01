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

    path = "index/xml/user_results.xlsx"
    book.save(path)
    return path


def create_xls_info_course(teacher_name: str, course_name: str, items: []):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Инфо")
    row = 0
    sheet.write(row, 0, "Информация о курсе")
    row += 1
    sheet.write(row, 0, "Преподаватель")
    sheet.write(row, 1, teacher_name)
    row += 1
    sheet.write(row, 0, "Курс")
    sheet.write(row, 1, course_name)
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
        sheet.write(row, 2, val.get_last_access())
        sheet.write(row, 3, val.get_end_grade())
        sheet.write(row, 4, val.get_end_grade_max())

    path = "index/xml/course_info.xlsx"
    book.save(path)
    return path


def create_xls_group(group_name, header, users):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Группа")
    row = 0
    sheet.write(row, 0, "Итоговая успеваемость группы")
    sheet.write(row, 1, group_name)
    row += 1
    sheet.write(row, 0, "№")
    sheet.write(row, 1, "ФИО/Курс")
    for i in range(len(header.courses)):
        sheet.write(row, i + 2, header.courses[i].name)
    for i, val in enumerate(users):
        row += 1
        sheet.write(row, 0, i + 1)
        sheet.write(row, 1, val.name)
        for i in range(len(val.courses)):
            sheet.write(row, i + 2, val.courses[i].get_final_grade())

    path = "index/xml/group.xlsx"
    book.save(path)
    return path

from random import *

students = []

def get_status(student):
	if student['status']==True:
		print('Текущее состояние: учится')
	else:
		print('Текущее состояние: отчислен')


def munu():
	print('1. Показать всех студентов')
	print('2. Зачислить нового студента')
	print('3. Отчислить студента')
	print('4. Показать всех отчисленных')
	print('0. Выход')


def print_student(student):
	print('Фамилия Имя:',student['surname'],student['name'])
	print('Группа:',student['group'])
	print('Степень:', student['stepen'])
	print('Дата:', student['date'])
	get_status(student)


def all():
	index = 1
	if(len(students)!=0):
		for student in students:
			print("========",index,"===========")
			print_student(student)
			index+=1
	else:
		print("Нету студентов")


def add_student():
	surname = input('Введите фамилию:')
	name = input('Введите имя:')
	group = input('Введите группу:')
	date = int(input('Введите дату поступления:'))
	stepen = input("Введите степень (бакалавр/магистр итд): ")
	student = {'surname':surname, 'name':name, 'group':group, 'date':date,'stepen':stepen, 'status':True}
	students.append(student)

def check_index_in_students(index):
	if index>=0 and index<len(students):
		return True
	else:
		return False


def delete_student():
	index = int(input("Введите номер студента:")) - 1
	if check_index_in_students(index):
		set_expelled_student(index)
		print("Данный студент был отчислен:")
		print_student(students[index])


def set_expelled_student(index):
	students[index]['status'] = False


def print_all_expelled_students():
	for student in students:
		if student['status']==False:
			print_student(student)
			return
	print('Нет отчисленных')


answer = -1
while answer!=0:
	munu()
	answer = int(input('Ваш выбор:'))
	if answer==1:
		all()
	elif answer==2:
		add_student()
	elif answer==3:
		delete_student()
	elif answer==4:
		print_all_expelled_students()

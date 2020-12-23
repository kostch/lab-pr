from random import *

students = []

def getStatus(student):
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

def PrintStudent(student):
	print('Фамилия Имя:',student['surname'],student['name'])
	print('Группа:',student['group'])
	print('Степень:', student['stepen'])
	print('Дата:', student['date'])
	getStatus(student)



def All():
	index = 1
	if(len(students)!=0):
		for student in students:
			print("========",index,"===========")
			PrintStudent(student)
			index+=1
	else:
		print("Нету студентов")

def AddStudent():
	surname = input('Введите фамилию:')
	name = input('Введите имя:')
	group = input('Введите группу:')
	date = int(input('Введите дату поступления:'))
	stepen = input("Введите степень (бакалавр/магистр итд): ")
	student = {'surname':surname, 'name':name, 'group':group, 'date':date,'stepen':stepen, 'status':True}
	students.append(student)

def DeleteStudent():
	index = int(input("Введите номер студента:"))-1
	if index>=0 and index<len(students):
		setExpelledStudent(index)
		print("Данный студент был отчислен:")
		PrintStudent(students[index])

def setExpelledStudent(index):
	students[index]['status'] = False

def PrintAllExpellesStudents():
	for student in students:
		if student['status']==False:
			PrintStudent(student)
			return
	print('Нет отчисленных')


answer = -1
while answer!=0:
	munu()
	answer = int(input('Ваш выбор:'))
	if answer==1:
		All()
	elif answer==2:
		AddStudent()
	elif answer==3:
		DeleteStudent()
	elif answer==4:
		PrintAllExpellesStudents()








	

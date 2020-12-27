from random import *


students = []


class Core:

	def all(self):
		index = 1
		if(len(students)!=0):
			for student in students:
				print("========",index,"===========")
				student.test()
				index+=1
		else:
			print("Нету студентов")

	def munu(self):
		print('1. Показать всех студентов')
		print('2. Зачислить нового студента')
		print('3. Отчислить студента')
		print('4. Показать всех отчисленных')
		print('0. Выход')


	def add_student(self):
		surname = input('Введите фамилию:')
		name = input('Введите имя:')
		group = input('Введите группу:')
		date = int(input('Введите дату поступления:'))
		stepen = input("Введите степень (бакалавр/магистр итд): ")
		st = student(surname, name, group,date,stepen)
		st.add_student()

	def delete_student(self):
		index = int(input("Введите номер студента:")) - 1
		if self.check_index_in_students(index):
			students[index].set_expelled_student()

			
	check_index_in_students = lambda self, index: True if index>=0 and index<len(students) else False# ламбда функция


	def print_all_expelled_students(self):
		[student.print_all_expelled_students() for student in students]#списковое включение
		# по сути списковое вкл, должно возаращать список, он его вернет оно будет = [].
		# и как бы он тут нам не нужен, ну раз по заданию нужно, я по этому и показала на таком примере
			





class student:
	def __init__(self, surname, name, group, date,stepen ):
		self.surname = surname
		self.name = name
		self.group = group
		self.stepen = stepen
		self.status = True
		self.date = date

	def add_student(self):
		students.append(self)

	

	def __str__(self):# эта штука, которая в задании требуется
		fio = 'Фамилия Имя: '+self.surname+' '+self.name+'\n'
		gr = 'Группа: '+self.group+'\n'
		step = 'Степень: '+self.stepen+'\n'
		d = 'Дата: '+ str(self.date)+'\n'
		st = self.get_status()+'\n'
		return fio+gr+step+d+st

	def test(self):#а здесь создается функция тест которая ее сипользует
		print(self)

	def set_expelled_student(self):
		self.status = False
		print("Данный студент был отчислен:")
		self.test()

	def print_all_expelled_students(self):
			if self.status==False:
				print(self)
				return
			print('Нет отчисленных')

	get_status = lambda self: 'Текущее состояние: учится' if self.status==True 	else 'Текущее состояние: отчислен'# ламбда





answer = -1
cor = Core()
while answer!=0:
	cor.munu()
	answer = int(input('Ваш выбор:'))
	if answer==1:
		cor.all()
	elif answer==2:
		cor.add_student()
	elif answer==3:
		cor.delete_student()
	elif answer==4:
		cor.print_all_expelled_students()



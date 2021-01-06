import unittest
from unittest.mock import*
import io
from Classes import*

class TestCore(unittest.TestCase):
	def setUp(self):
		self.cor = Core()

	def test_check_index_in_students_empy(self):
		self.assertEqual(self.cor.check_index_in_students(0), False)


	@patch('sys.stdout', new_callable=io.StringIO)
	def test_all_empty(self,mock_stdout):
		students.clear()
		self.cor.all()
		self.assertEqual("Нету студентов\n", mock_stdout.getvalue())


class TestStudent(unittest.TestCase):
	
	def test_get_status_true(self):
		st = student("Иванов2", "Иван2","РИС2-16", 2017,"БАКАЛАВР")
		st.status = True
		self.assertEqual('Текущее состояние: учится', st.get_status())


	def test_get_status_false(self):
		st = student("Иванов2", "Иван2","РИС2-16", 2017,"БАКАЛАВР")
		st.status = False
		self.assertEqual('Текущее состояние: отчислен', st.get_status())

	def test_add_student(self):
		self.st = student("Иванов", "Иван","РИС-16", 2016,"БАКАЛАВР")
		students.clear()
		self.st.add_student()
		index = len(students)-1
		self.assertEqual(True, self.st.name == students[index].name
						 and self.st.surname == students[index].surname
						  and self.st.group == students[index].group 
						  and self.st.status == students[index].status
						   and self.st.date == students[index].date )









if __name__ == "__main__":
	unittest.main()


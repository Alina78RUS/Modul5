'''Создайте класс Model, в котором будет метод save. Метод save 
должен создавать словарь со всеми значениями атрибутов классов 
и записывать его в json файл.
 Пример: {'title':'заголовок', 'author': 'Имя автора'}
 
'''
import json

class Model:

	def __init__(self):
		self.dictionary = {}
	
	def save (self, key, value):
		self.key = key
		self.value = value
		self.dictionary[self.key] = self.value 
		with open ('Modul5,Part2','w') as f:
			json.dump(self.dictionary, f)
		return self.dictionary
		
	def get (self):
		return self.dictionary

s = Model()
s.save('Aleksandr Sergeevich Pushkin','Ruslan and Ludmila')
s.save('Lev Nikolaevich Tolstoi','Anna Karenina')
s.save('Aleksandr Triphonovich Tvardovskii', 'Vasilii Terkin')
print (s.get())


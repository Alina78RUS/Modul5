'''Создайте класс Model, в котором будет метод save. Метод save 
должен создавать словарь со всеми значениями атрибутов классов 
и записывать его в json файл.
 Пример: {'title':'заголовок', 'author': 'Имя автора'}
 
'''
import json

class Model:
	title = 'Stalker'
	author = 'Brothers Strugatskie'

	def save(self):
		dictionary = {}
		book = list(filter(lambda x: not x.startswith('_'), dir(Model)))
		book.remove('save')
		for i in book:
			dictionary[i] = eval('self.' + i)
		with open('Modul5,Part2.json', 'w') as f:
			json.dump(dictionary, f)
		return dictionary

s = Model()
s.title = '2033'
s.author = 'Gluhovskii'
print (s.save())
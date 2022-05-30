text='''Создайте класс StringVar для работы со строковым типом данных,
содержащий методы set() и get(). Метод set() служит для изменения 
содержимого строки, get() для получения содержимого строки.
Создайте обьект типа StringVar и протестируйте его методы'''


class StringVar:
	def __init__(self):
		self.s = ''
	def set (self, txt): # Метод изменения содержимого строки
		self.s = txt
		return self.s
	def get (self):     # Метод получения содержимого строки
		return self.s
	
s = StringVar()
s.set(text)            
print(s.get())

s.set('I love Python')
print (s.get())




import random

class Voin:
	
	def __init__(self, name, health=100, armor=100, endurance=100):   # Инициализация параметров нашего воина

		self.name=name
		self.health=health
		self.armor=armor
		self.endurance=endurance

	def attack (self, health, endurance):                             # Метод в случае если оба воина атакуют
		if self.endurance <= 0:
			self.health -= random.randint(0,10)
			print ('Запас выносливости истощен, урон понижен')
			return self.health, self.endurance
		self.health -= random.randint(0,30)
		self.endurance -= random.randint(0,10)		
		return self.health, self.endurance

	def defense (self, health, armor):                               # Метод защиты                      
		
		if self.armor <= 0:
			self.health -= random.randint(10,30)
			print ('Прочность брони закончилась, урон повышен')	
			return self.health, self.armor		                    
		self.health -= random.randint(0,20)
		self.armor -= random.randint(0,10)		
		return self.health,  self.armor

s1=Voin('Воин1')                                                    # Инициализация воинов
s2=Voin('Воин2',100,100,100)

while True:                                                         # Цикл в котором начался бой
	round = random.randint(1,4)

	if round == 1 :
		print ('Воин2 атакует, Воин1 защищается ')                        
		s1.defense(s1.health, s1.armor)
		print ('Здоровье ', s1.name, s1.health, '\n')
		if s1.health <= 10:
			print ('Воин2 победил !!!')
			win = input('Казнить Воина1? (y or n)')
			if win == 'y':
				print ('Воин2 казнил Воина1' )
				break
			else:
				print ('Воин2 помиловал Воина1')
				break		
		continue	

	if round == 2:
		print ('Воин1 атакует, Воин2 защищается ')	
		s2.defense(s2.health, s2.armor)
		print ('Здоровье ', s2.name, s2.health, '\n')
		if s2.health <= 10:
			print ('Воин1 победил !!!')
			win = input('Казнить Воина2? (y or n)')
			if win == 'y':
				print ('Воин1 казнил Воина2')
				break
			else:
				print ('Воин1 помиловал Воина2')
				break
		continue

	if round == 3:
		print ('Оба Воина атакуют')
		s1.attack(s1.health, s1.endurance)
		print ('Здоровье ', s1.name, s1.health, )		
		s2.attack(s2.health, s2.endurance)
		print ('Здоровье ', s2.name, s2.health, '\n')
		if s1.health <= 10:
			print ('Воин2 победил !!!')
			win = input('Казнить Воина1? (y or n)')
			if win == 'y':
				print ('Воин2 казнил Воина1')
				break
			else:
				print ('Воин2 помиловал Воина1')
				break
		if s2.health <= 10:
			print ('Воин1 победил !!!')
			win = input('Казнить Воина2? (y or n)')
			if win == 'y':
				print ('Воин1 казнил Воина2')
				break
			else:
				print ('Воин1 помиловал Воина2')
				break
		continue		

	if round == 4:		
		print ('Оба Воина защищаются''\n')

		continue
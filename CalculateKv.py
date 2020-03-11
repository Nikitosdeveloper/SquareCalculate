from kivy.app import App #импортируем главный класс он и будет нашим приложением

from kivy.uix.gridlayout import GridLayout #импортируем класс в котором будут распологаться виджеты кнопок
from kivy.uix.boxlayout import BoxLayout #импортируем класс в котором будут распологаться виджеты экрана и панели
from kivy.uix.textinput import TextInput #импортируем класс - текстовая панель
from kivy.uix.button import Button #импортируем класс кнопка
from kivy.uix.modalview import ModalView #импортируем класс при использовании которого будет вылезать окно с решение
from kivy.uix.slider import Slider

from kivy.config import Config #импортируем класс который позволит изменять размеры экрана

Config.set('graphics','width',1081)#{
Config.set('graphics','height',2341)#изменяем размер экрана
#Config.set('graphics','resizable',0)#}

global b
b = ['1','2','3','4','5','6','7','8','9','0','-','+']
global level
level = 0
global one_zero
one_zero = True
global one_plus
one_plus = True
global two_zero
two_zero = True
global two_plus
two_plus = True
global three_zero
three_zero = True
global three_plus
three_plus= True
global level2_nomber
level2_nomber = True
global last_symbol

class MyApp(App):
	def on_value(self,instance,value):
		#функция которая меняет размер шрифта
		self.ti2.cursor = self.cursorm
		text_massive = self.ti2.text.split('\n')
		for i in range(len(text_massive)):
			text_massive[i] = len(text_massive[i])
		self.sl.max = int(max(text_massive))
		self.cursorm[1] = int(text_massive.index(max(text_massive)))
		self.cursorm[0] = int(round(self.sl.value))
		self.ti2.cursor = self.cursorm

	def clear(self,instance):
		#функция которая очищает текстовую панель
		self.sl.value = 10
		self.ti1.text = '0'
		self.ti2.text = str('a = '+ ' ' + ' ' + 'b = '+ ' ' + '\n' + 'c = ' + ' ' +  'D = ')
		self.formula = ""
		global level
		level = 0
		global one_zero
		one_zero = True
		global one_plus
		one_plus = True
		global two_zero
		two_zero = True
		global two_plus
		two_plus = True
		global three_zero
		three_zero = True
		global three_plus
		three_plus = True
		global level2_nomber
		level2_nomber = True
		self.modal.dismiss()
	def calcualte(self):
		#функция которая решает квадратные у-я
		global klop
		import math
		s = self.formula
		a = ''
		b = ''
		c = ''
		sa, sbc = s.split('x²')
		if sa == '':
			a = 1
		elif sa == '-':
			a = -1
		else:
			a = sa
		if 'x' in sbc:
			sb, sc = sbc.split('x')
			if sb == '' or sb=='+':
				b = 1
			elif sb == '-':
				b = -1
			else:
				b = sb
			if '+' in sc or '-' in sc:
				c, l = sc.split('=')
				del l
			else:
				c = 0
		else:
			b = 0
			sc = sbc
			if '+' in sc or '-' in sc:
				c, l = sc.split('=')
				del l
			else:
				c = 0
		a = int(a)
		b = int(b)
		c = int(c)
		if a == 0:
			h = 'Ты где такой пример нашел?\na не может быть равно 0'
		else:
			disk = (b ** 2) - (4 * a * c)
			len1 = len('-' + str(b) + ' - √' + str(disk)) // 2
			len1 += len('-' + str(b) + ' - √' + str(disk)) % 2
			len1a = len('2*' + str(a)) // 2
			len1a += len('2*' + str(a)) % 2
			len2 = len(str(b)) // 2
			len2 += len(str(b)) % 2
			len1 = max(len1, len1a)
			len2 = max(len2, len1a)

			if disk > 0:
				x1 = -b - math.sqrt (disk)
				x1 /= (2*a)
				x1 = float('{:.5f}'.format(x1))
				x2 = -b + math.sqrt (disk)
				x2 /= (2 * a)
				x2 = float('{:.5f}'.format(x2))
			elif disk == 0:
				x=-b/(2*a)
				x = float('{:.5f}'.format(x))
			h = str('    a = '+ str(a) + ' b = '+ str(b) + ' c = '+ str(c) +  '\n    ' + 'D = b² - 4ac' + ' = ' + str(b) + '² ' + '- 4*' + str(a) + '*' + str(c) + ' = ' + str(disk))
			if disk < 0:
				h += '    \n    ' + 'Ответ: нет корней'
			elif disk == 0:
				h += '    \n     	      b        '+ str(b) + '\n    x = - —— - ' + '—'*len2 + ' = ' + str(x) + '\n   	      2a     2*' + str(a)
				h += '\n    Ответ: x = '+ str(x)
			else:
				h += '    \n    ' + '         -b - √D'+ '	-' + str(b) + ' - √' + str(disk) + ';\n    x1 = ———— = ' + '—'*len1 + ' = ' + str(x1) + '    \n            2a' + '       	2*' + str(a) + '    '
				h += '    \n    \n    ' + '         -b + √D'+ '	-' + str(b) + ' + √' + str(disk) + ';\n    x2 = ———— = ' + '—'*len1 + ' = ' + str(x2) + '\n                2a' + '       	2*' + str(a) + '    '
				h += '    \n    Ответ: x = ('+ str(x1) + ' ; ' + str(x2) + ')'
			h = h.replace("--","+")
		return h

	def build(self):
		#функция которая запускает нашу программу 
		self.formula = ""
		self.modal = ModalView(size = (400, 400), auto_dismiss = False)
		self.cursorm = [0,0]
		gl = GridLayout(cols=3,spacing = 3,size_hint = (1, 0.3))
		bl = BoxLayout(orientation = 'vertical')#, padding = 25
		bl2 = BoxLayout(orientation = 'vertical') 
		self.ti1 = TextInput(text = '0', font_size = 100, size_hint = (1, 0.7), halign = 'left', allow_copy = False, readonly = False, multiline = True )
		self.ti2 = TextInput(text = '	a = '+ ' ' + ' ' + 'b = '+ ' ' + '\n    ' + 'c = ' + ' ' +  'D = ' +'     \n' + '    \n', font_size = 50, size_hint = (1,0.8) , halign = 'left', allow_copy = False, cursor = self.cursorm, multiline = False, readonly = False)
		self.sl = Slider(orientation = 'horizontal', min = 0, max = 255, value = 0, size_hint = (1,0.1))
		self.sl.bind(value = self.on_value)
		bl2.add_widget(self.ti2)	
		bl2.add_widget(self.sl)
		bl2.add_widget(Button(text =  'очистить',font_size = 60,size_hint = (1,0.1), on_press = self.clear,  color = [0,0,0,1], background_color = [96,96,96,1]))
		bl.add_widget(self.ti1)
		#bl.add_widget(self.ti2)
		self.modal.add_widget(bl2)
		b1 = Button(text = '+', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '<==', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '-', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '7', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '8', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '9', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '4', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '5', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '6', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '1', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '2', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '3', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = 'x²', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '0', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = 'x', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1])
		gl.add_widget(b1)
		b1 = Button(text = '=', font_size = 60,on_press = self.add_number, color = [0,0,0,1], background_color = [96,96,96,1], size_hint = (1,0.1))
		bl.add_widget(b1)
		bl.add_widget(gl)
		return bl
	def add_number(self,instance):
		#функция которая позволяет вводить данные на текстовую паннель
		global level
		global one_zero
		global one_plus
		global two_zero
		global two_plus
		global three_zero
		global three_plus
		global level2_nomber
		global last_symbol
		if level == 0:
			if instance.text in b:
				if instance.text == '-' and one_zero:
					self.formula += instance.text
					last_symbol = instance.text
					one_zero = False
					one_plus = False
				elif instance.text != '-' and instance.text != '+':
					self.formula += instance.text
					last_symbol = instance.text
					one_zero = False
					one_plus = False
			elif instance.text == "x²":
				self.formula +=instance.text
				last_symbol = instance.text
				one_zero = False
				one_plus = False
				level += 1
		elif level == 1:
			if instance.text in b:
				if instance.text == '-' and two_zero:
					self.formula += instance.text
					last_symbol = instance.text
					two_zero = False
					two_plus = False
				elif instance.text == '+' and two_plus:
					self.formula += instance.text
					last_symbol = instance.text
					two_zero = False
					two_plus = False
				elif instance.text != '-' and instance.text != '+':
					if (not two_plus) or (not two_zero):
						self.formula += instance.text
						last_symbol = instance.text
						two_zero = False
						two_plus = False
						level = 4
					else:
						self.formula += '+' + instance.text
						last_symbol = instance.text
						two_zero = False
						two_plus = False
						level = 4
			elif instance.text == 'x':
				if (not two_plus) or (not two_zero):
					self.formula += instance.text
					last_symbol = instance.text
					level = 2
				else:
					self.formula += '+' + instance.text
					last_symbol = instance.text
					level = 2
			elif two_zero and two_plus and instance.text == '=':
				level = 3
				self.formula += '=0'
				self.ti2.text = self.calcualte()
				self.modal.open()
		elif level == 4:
			if instance.text in b and instance.text != '-' and instance.text != '+':
				self.formula += instance.text
				last_symbol = instance.text
			elif instance.text == 'x':
				self.formula += instance.text
				last_symbol = instance.text
				level = 2
			elif instance.text == '=':
				level = 3
				self.formula += '=0'
				self.ti2.text = self.calcualte()
				self.modal.open()
		elif level == 2:
			if instance.text in b:
				if instance.text == '-' and three_zero:
					self.formula += instance.text
					last_symbol = instance.text
					three_zero = False
					three_plus = False
				elif instance.text == '+' and three_plus:
					self.formula += instance.text
					last_symbol = instance.text
					three_zero = False
					three_plus = False
				elif instance.text != '-' and instance.text != '+':
					if (not three_plus) or (not three_zero):
						self.formula += instance.text
						last_symbol = instance.text
						three_zero = False
						three_plus = False
						level2_nomber = False
					else:
						self.formula += '+' + instance.text
						last_symbol = instance.text
						three_zero = False
						three_plus = False
						level2_nomber = False
			elif instance.text == '=':
				if three_plus and three_zero:
					level = 3
					self.formula += '=0'
					self.ti2.text = self.calcualte()
					self.modal.open()
				elif not level2_nomber:
					level = 3
					self.formula += '=0'
					self.ti2.text = self.calcualte()
					self.modal.open()
		if self.formula == '':
			self.ti1.text = '0'
		else:	
			self.ti1.text = str(self.formula.replace('x^2','x²'))
		print(last_symbol)
#запуск программы
if __name__ == "__main__":
	MyApp().run()

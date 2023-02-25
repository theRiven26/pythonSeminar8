

def appendPhonebook(file):
	firstname = input("Введите имя абонента: ").lower()
	surname = input("Введите фамилию абонента: ").lower()
	phone = int(input("Введите номер: "))
	with open(file,'a') as data:
		data.write(f"Caller: {firstname} {surname}.  Phone: {phone}")
		data.write('\n')

def serching(element, file):
	with open(file) as data:
		for line in data:
			if element in line:
				print(line, end='')
				return True
	return False
		print("Абонент не найден")


def searchCaller(file):
	word = input("Введите строку поиска: ").lower()
	find = False
	with open(file) as data:
		for line in data:
			if word in line:
				print(line, end='')
				find = True
	if not find:
		print()
		print("Абонент не найден")

def openBook(file):
	with open(file) as data:
		for line in data:
				print(line, end='')

def passBook(file):
	with open(file, 'wb'):
		pass

def exit():
	quit()

def menu():
	print()
	print("1 - добавить абонента")
	print("2 - найти абонента")
	print("3 - открыть справочник")
	print("4 - редактировать данные абонента")
	print("5 - удалить данные абонента")
	print("6 - выход")



def main():
	file = '_phonebook.txt'
	while True:
		menu()
		result = int(input(": "))
		if result == 1:
			appendPhonebook(file)
		elif result == 2:
			searchCaller(file)
		elif result == 3:
			openBook(file)
		elif result == 4:
			passBook(file)
		elif result == 5:
			passBook(file)
		elif result == 6:
			exit()


main()




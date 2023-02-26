

def appendPhonebook(file):
	name = input("Введите ФИО абонента: ").lower()
	phone = int(input("Введите номер: "))
	listName = name.split()
	while len(listName) <= 3:
		listName.append("")
	idCaller = getIdCaller(file)
	with open(file, 'a') as data:
		data.write(f"{idCaller};{listName[0]};{listName[1]};{listName[2]};{phone}")
		data.write('\n')

def getIdCaller(file):
	return sum(1 for line in open(file))

def searching(element, file):
	listResult = []
	with open(file) as data:
		for line in data:
			if element in line:
				listResult.append(line.split(";"))
	return listResult

def searchCaller(file):
	word = input("Введите строку поиска: ").lower()
	searchResult = searching(word, file)
	if len(searchResult) > 0:
		for i in searchResult:
			print(fomatListForUser(i))
	else:
		print()
		print("Абонент не найден")

def openBook(file):
	with open(file) as data:
		for line in data:
			listLine = line.split(";")
			print(fomatListForUser(listLine))

def fomatListForUser(list):
	return f"Caller: {list[1]} {list[2]} {list[3]} Phone:{list[4]}".replace("\n", "")

def deleteElement(file):
	word = input("Введите строку поиска: ").lower()
	searchResult = searching(word, file)
	with open(file) as data:
		oldData = data.read()
	for i in searchResult:
		print(fomatListForUser(i))
	if len(searchResult) > 1:
		print("Найдено больше одного абонента. Введите нужный номер")
		editLine = searchResult[int(input()) - 1]
	else:
		editLine = searchResult[0]
	newData = oldData.replace(";".join(editLine), "")
	with open(file, 'w') as f:
		f.write(newData)

def editBook(file):
	word = input("Введите строку поиска: ").lower()
	searchResult = searching(word, file)
	with open(file) as data:
		oldData = data.read()
	for i in searchResult:
		print(fomatListForUser(i))
	if len(searchResult) > 1:
		print("Найдено больше одного абонента. Введите нужный номер")
		editLine = searchResult[int(input())-1]
	else:
		editLine = searchResult[0]
	print("Выберите пункты для редактирования")
	print("1 - Фамилия")
	print("2 - Имя")
	print("3 - Отчество")
	print("4 - Телефон")
	_idParam = int(input())
	newEditline = editLine.copy()
	newEditline[_idParam] = input()
	newData = oldData.replace(";".join(editLine), ";".join(newEditline))
	with open(file, 'w') as f:
		f.write(newData)
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
	print("6 - очистить справочник")
	print("7 - выход")



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
			editBook(file)
		elif result == 5:
			deleteElement(file)
		elif result == 6:
			passBook(file)
		elif result == 7:
			exit()


main()




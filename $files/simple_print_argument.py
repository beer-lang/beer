def BeerLang(Syntax):
	State = 0
	Token = ""
	String = ""
	for Char in Syntax:
		Token += Char
		if Token == " ":
			if State == 0:
				Token = ""

		elif Token == "\n":
			Token = ""

		elif Token == "t =>":
			Token = ""

		elif Token == "\"":
			if State == 0:
				State = 1
				Token = ""

			elif State == 1:
				State = 0

		elif State == 1:
			String += Token
			Token = ""

	print(String)

Content = open("scr/main.beer", "r").readlines()
for Line in Content:
	BeerLang(Line)


def BeerLang(Syntax):
	State = 0
	Token = ""
	String = ""
	for Char in Syntax:
		Token += Char
		if Token == " ":
			if State == 0:
				Token = ""

		elif Token == "\n":
			Token = ""

		elif Token == "n =>>" + "":
			Token = ""

		elif Token == "\"":
			if State == 0:
				State = 1
				Token = ""

			elif State == 1:
				State = 0

		elif State == 1:
			String += Token
			Token = ""

	print(String)

Content = open("scr/main.beer", "r").readlines()
for Line in Content:
	BeerLang(Line)
print("Github Status : 🍻|Drinking beer with python")

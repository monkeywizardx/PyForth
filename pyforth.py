import forth
executing = true
PyForth = forth.Forth()
def parse(string):
	return string.lower().split()

while executing:
	code = parse(input("forth>"))
	if "bye" in code:
		executing = false

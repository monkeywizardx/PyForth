from sys import argv
import forth
executing = True

def run(string):
	forth.forth_eval(forth.parse(string))
def main_loop():
  while executing:
    try: run(input("pyforth>"))
    except IndexError:
      print("Stack Error!")
      stack.append(-127)

if __name__ == "__main__":
  if len(argv) == 1:
    main_loop()
  else:
    file = open(argv[1], 'r')
    run(file.read())
    main_loop()

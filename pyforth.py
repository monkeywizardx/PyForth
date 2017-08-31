import forth
executing = true
PyForth = forth.Forth({
        'DUP': 'VARIABLE holder holder ! holder @ holder @',
        'SWAP': 'VARIABLE top VARIABLE bottom top ! bottom ! top @ bottom @'
})

while executing:
	REPL_input = input("pyforth>")
        if REPL_input.upper() == 'BYE':
                executing = false
        else:
                PyForth.evaluate(PyForth.parse(REPL_input))

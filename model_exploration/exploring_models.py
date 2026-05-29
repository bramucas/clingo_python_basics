import sys
import clingo

with open(sys.argv[1], "r") as f:
    ASP_program = f.read()

ctl = clingo.Control(
    arguments=['-n', '0'],
)

ctl.add("base", [], ASP_program)
ctl.ground([("base", [])])

with ctl.solve(yield_=True) as solution_iterator:
        nanswer=1
        for model in solution_iterator:
            print(f'Answer {nanswer}')
            for atom in model.symbols(atoms=True):  
                # atoms=True for ignoring #show statements, otherwise symbols will retrieve only shown atoms.
                if atom.name == 'bulb' and len(atom.arguments) == 1:  # We check if atom is bulb/1.
                    print(f'Bulb is {atom.arguments[0]}')  # Arguments can be retrieved from atom.arguments
            nanswer+=1

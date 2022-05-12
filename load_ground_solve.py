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
            print(model)
            nanswer+=1

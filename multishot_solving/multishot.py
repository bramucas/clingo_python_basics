import clingo
from clingo.symbol import Number

ctl = clingo.Control()

# Add multiple program parts
ctl.add("a", [], "q.")
ctl.add("b", ["t"], "q(t).")

# Ground and solve first part
ctl.ground([("a", [])])
print("First solve:")
print(ctl.solve(on_model=print))

# Ground additional parts with parameters
ctl.ground([("b", [Number(1)]), ("b", [Number(2)])])
print("Second solve:")
print(ctl.solve(on_model=print))

# Ground another part
ctl.ground([("b", [Number(3)])])
print("Third solve:")
print(ctl.solve(on_model=print))

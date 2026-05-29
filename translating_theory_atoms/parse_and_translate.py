from clingo import Function, Number

from clingo.ast import parse_string
import clingo.ast as cast

from clingo.ast import (
    Location,
    Position,
    Literal,
    Rule,
    SymbolicAtom,
    SymbolicTerm,
)

THEORY_ATOM_NAME = "dl"

loc = Location(
    Position("", 0, 0),
    Position("", 0, 0),
)


def translate_rule(sentence):
    print("processing:", sentence)

    new_body = []
    
    if sentence.ast_type == cast.ASTType.Rule:
        for literal in sentence.body:
            if literal.ast_type == cast.ASTType.Literal:
                if literal.atom.ast_type == cast.ASTType.TheoryAtom:
                    if literal.atom.term.name == THEORY_ATOM_NAME:
                        # do whatever you want here
                        # example
                        sym_term = SymbolicTerm(loc, Function("@whatever", [Number(1), Number(2), Number(3)]))
                        sym_atom = SymbolicAtom(sym_term)
                        new_lit = Literal(
                            literal.location,
                            False,      # Change to True if you want default negation
                            sym_atom
                        )
                        print("new lit:", new_lit)
                        new_body.append(new_lit)

            else:
                # Regular literal, add it to new body
                new_body.append(literal)

        new_rule = Rule(sentence.location, sentence.head, new_body)
        print("new rule:", new_rule)


with open("example.lp", "r") as f:
    program = f.read()

parse_string(
    program,
    lambda ast: translate_rule(ast)
)
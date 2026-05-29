# Multi-shot Solving

This folder contains examples of multi-shot solving, where you can ground and solve multiple times in a single control object.

## Files

- `multishot.py` - Example showing incremental grounding and solving

## Usage

```sh
python multishot.py
```

## Concepts

- **Multi-shot solving**: Ground and solve multiple times with the same Control object
- **Program parts**: Add different parts of a program with parameters
- **Incremental grounding**: Add new parts incrementally and re-solve
- **Number symbols**: Use clingo.symbol.Number to pass numeric parameters to grounding

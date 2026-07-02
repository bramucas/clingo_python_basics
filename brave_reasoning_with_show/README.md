Brave reasoning `--enum-mode=brave` obtains the union of all answer sets.
Given a set of show statements this seems to affect the early stopping.

I don't really know about if this also affects the search in any other way.

### Example

```
clingo 0 --enum-mode=brave choices.lp
```

```
clingo 0 --enum-mode=brave choices.lp show.lp
```

| Metric | con show | sin show |
|---|---|---|
| Models | 2 | 2047 |
| Brave | yes | yes |
| Consequences | 3 | 2054 |
| Calls | 1 | 1 |
| Time | 0.003s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s) | 3.049s (Solving: 3.05s 1st Model: 0.00s Unsat: 0.00s) |
| CPU Time | 0.003s | 0.705s |
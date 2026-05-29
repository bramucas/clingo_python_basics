# Projection

This folder contains examples of using the `#project` directive for answer set projection.

## Files

- `kk_encoding.lp` - ASP encoding with choice rules
- `kk_show.lp` - Show directive for output
- `kk_project.lp` - Project directive for projection

## Usage

```sh
clingo 0 kk_encoding.lp kk_show.lp kk_project.lp --project=auto
```

Without projection:
```sh
clingo 0 kk_encoding.lp kk_show.lp --project=auto
```

## Concepts

- **#project directive**: Specifies which atoms to project on
- **--project=auto**: Automatically includes #project directives from files
- **Projection**: Reduces answer sets to only the projected atoms


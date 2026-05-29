
You can execute with 
```sh
clingo 0 [files] --project=auto
```

in this way, if you keep a separate file like `kk_project.lp` with the project directive, it will be automatically included only if the file is included.

this will project
```sh
clingo 0 kk_encoding.lp kk_show.lp kk_project.lp --project=auto
```

this no
```sh
clingo 0 kk_encoding.lp kk_show.lp --project=auto
```
because there is no `#project` directive in any of the files.


% --- muchos modelos ---
{a(1..2000)}.

% --- átomo de interés (depende de algunos) ---
b :- a(1), a(2).
c :- a(3), a(4).
d :- a(5).

% --- ruido independiente (no afecta nada) ---
{r(1..50)}.

% --- regla para mezclar un poco la estructura ---
ok :- b.
ok :- c.
ok :- d.

% --- restricción ligera para evitar modelo vacío trivial ---
:- not ok.

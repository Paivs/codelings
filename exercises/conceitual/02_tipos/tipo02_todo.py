# TITLE: Tipos - Convertendo Valores
# TYPE: todo
# DESCRIPTION: Complete as conversoes de tipo nos espacos indicados.
# ID: 005

# TODO: Converta a string "42" para inteiro e armazene em 'numero_inteiro'

# TODO: Converta o inteiro 7 para float e armazene em 'numero_float'

# TODO: Converta o numero 0 para booleano e armazene em 'valor_falso'

# TODO: Converta o numero 99 para string e armazene em 'numero_texto'

numero_inteiro = int("42")
numero_float = float(7)
valor_falso = bool(0)
numero_texto = str(99)


# --- Validacao (nao modifique abaixo) ---
assert numero_inteiro == 42, f"Esperado 42, obtido {numero_inteiro}"
assert isinstance(numero_inteiro, int), f"Esperado int, obtido {type(numero_inteiro).__name__}"
assert numero_float == 7.0, f"Esperado 7.0, obtido {numero_float}"
assert isinstance(numero_float, float), f"Esperado float, obtido {type(numero_float).__name__}"
assert valor_falso is False, f"Esperado False, obtido {valor_falso}"
assert numero_texto == "99", f"Esperado '99', obtido '{numero_texto}'"
assert isinstance(numero_texto, str), f"Esperado str, obtido {type(numero_texto).__name__}"
print(f"int    : {numero_inteiro!r}  ({type(numero_inteiro).__name__})")
print(f"float  : {numero_float!r}  ({type(numero_float).__name__})")
print(f"bool   : {valor_falso!r}  ({type(valor_falso).__name__})")
print(f"str    : {numero_texto!r}  ({type(numero_texto).__name__})")
print("Exercicio concluido!")

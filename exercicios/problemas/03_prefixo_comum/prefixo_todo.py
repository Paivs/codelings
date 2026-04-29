# TITULO: Prefixo Comum - Implementar
# TIPO: todo
# ID: 023

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de autocomplete precisa encontrar o maior trecho
# inicial comum entre todas as palavras de uma lista.
#
# Exemplos:
#   longest_common_prefix(["flower", "flow", "flight"])       -> "fl"
#   longest_common_prefix(["dog", "racecar", "car"])          -> ""
#   longest_common_prefix(["interview", "inter", "internal"]) -> "inter"
#
# Regras de negocio:
#   - Lista vazia retorna ""
#   - Lista com uma palavra retorna a propria palavra
#   - Se nao houver prefixo comum, retorna ""
# =================================================================

def longest_common_prefix(strs):
    # TAREFA: Itere pelos caracteres da primeira string. Para cada
    # posicao i, verifique se todas as outras strings tem o mesmo
    # caractere nessa posicao. Pare ao encontrar uma divergencia ou
    # quando alguma string for mais curta que i.
    pass

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert longest_common_prefix(["flower", "flow", "flight"])       == "fl",    "caso 1 incorreto"
assert longest_common_prefix(["dog", "racecar", "car"])           == "",     "caso 2 incorreto"
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter", "caso 3 incorreto"
assert longest_common_prefix(["a"])                               == "a",    "caso 4 incorreto"
assert longest_common_prefix([])                                  == "",     "caso 5 incorreto"
assert longest_common_prefix(["abc", "abc", "abc"])               == "abc",  "caso 6 incorreto"
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print("Exercicio concluido!")

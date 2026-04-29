# TITULO: Prefixo Comum - Bug no Corte da String
# TIPO: fix
# ID: 022

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de autocomplete encontra o maior prefixo comum entre
# palavras, mas ha um bug: ao encurtar o prefixo, ele remove do
# lado errado da string.
#
# Corrija a direcao do corte.
# =================================================================

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while prefix and not s.startswith(prefix):
            prefix = prefix[1:]   # <- revise esta linha
    return prefix

# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert longest_common_prefix(["flower", "flow", "flight"])       == "fl",    "caso 1 incorreto"
assert longest_common_prefix(["dog", "racecar", "car"])           == "",     "caso 2 incorreto"
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter", "caso 3 incorreto"
assert longest_common_prefix(["a"])                               == "a",    "caso 4 incorreto"
assert longest_common_prefix([])                                  == "",     "caso 5 incorreto"
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print('["interview","inter","internal"] ->', longest_common_prefix(["interview","inter","internal"]))
print("Exercicio concluido!")

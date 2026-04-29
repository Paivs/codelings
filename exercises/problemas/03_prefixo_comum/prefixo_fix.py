# TITLE: Prefixo Comum - Bug no Corte da String
# TYPE: fix
# DESCRIPTION: A funcao encurta o prefixo pelo lado errado da string.
# ID: 022

def longest_common_prefix(strs):
    """Retorna o maior prefixo comum entre todas as strings da lista."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while prefix and not s.startswith(prefix):
            prefix = prefix[1:]   # BUG: remove do inicio, deveria remover do final
    return prefix


assert longest_common_prefix(["flower", "flow", "flight"])       == "fl"
assert longest_common_prefix(["dog", "racecar", "car"])           == ""
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter"
assert longest_common_prefix(["a"])                               == "a"
assert longest_common_prefix([])                                  == ""
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print('["interview","inter","internal"] ->', longest_common_prefix(["interview","inter","internal"]))
print("Exercicio concluido!")

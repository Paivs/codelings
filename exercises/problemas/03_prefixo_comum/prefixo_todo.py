# TITLE: Prefixo Comum - Implementar
# TYPE: todo
# DESCRIPTION: Encontre o maior prefixo comum entre todas as strings da lista.
# ID: 023

def longest_common_prefix(strs):
    """
    Retorna o maior prefixo comum a todas as strings de 'strs'.
    Se nao houver prefixo comum ou a lista for vazia, retorne "".

    longest_common_prefix(["flower", "flow", "flight"])      -> "fl"
    longest_common_prefix(["dog", "racecar", "car"])          -> ""
    longest_common_prefix(["interview", "inter", "internal"]) -> "inter"
    """
    # TODO: Implemente a funcao.
    # Dica: Para cada posicao i da primeira string, verifique se todas as
    # outras strings possuem o mesmo caractere nessa posicao.
    pass


# --- Validacao (nao modifique abaixo) ---
assert longest_common_prefix(["flower", "flow", "flight"])       == "fl"
assert longest_common_prefix(["dog", "racecar", "car"])           == ""
assert longest_common_prefix(["interview", "inter", "internal"]) == "inter"
assert longest_common_prefix(["a"])                               == "a"
assert longest_common_prefix([])                                  == ""
assert longest_common_prefix(["abc", "abc", "abc"])               == "abc"
print('["flower","flow","flight"]      ->', longest_common_prefix(["flower","flow","flight"]))
print('["dog","racecar","car"]          ->', longest_common_prefix(["dog","racecar","car"]))
print('["interview","inter","internal"] ->', longest_common_prefix(["interview","inter","internal"]))
print("Exercicio concluido!")

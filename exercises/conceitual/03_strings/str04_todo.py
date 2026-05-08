# TITULO: Strings - Gerador de Slug
# TIPO: todo
# ID: 042

# =================================================================
# ENUNCIADO
# =================================================================
# Um sistema de blog precisa gerar slugs (URLs amigaveis) a partir
# de titulos de artigos. O processo envolve tres transformacoes
# aplicadas em sequencia.
#
# Titulo de entrada: "  Aprenda Python em 2024!  "
#
# Resultados esperados:
#   limpo    -> "Aprenda Python em 2024!"  (sem espacos nas bordas)
#   minusculo -> "aprenda python em 2024!" (tudo em minusculas)
#   slug     -> "aprenda-python-em-2024!"  (espacos substituidos por "-")
# =================================================================

titulo = "  Aprenda Python em 2024!  "

# TAREFA: Transforme 'titulo' em 'slug' passo a passo.


# =================================================================
# TESTES (nao modifique abaixo)
# =================================================================
assert limpo    == "Aprenda Python em 2024!",  f"limpo incorreto: {limpo!r}"
assert minusculo == "aprenda python em 2024!", f"minusculo incorreto: {minusculo!r}"
assert slug     == "aprenda-python-em-2024!",  f"slug incorreto: {slug!r}"
print(f"limpo    = {limpo!r}")
print(f"minusculo = {minusculo!r}")
print(f"slug     = {slug!r}")
print("Exercicio concluido!")

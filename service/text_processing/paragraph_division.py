import re

def dividir_em_paragrafos(texto: str) -> list[str]:
    """
    Divide o texto em parágrafos, considerando linhas em branco como delimitadores.

    Args:
        texto: O texto completo.

    Returns:
        Uma lista de strings, onde cada string é um parágrafo.
    """
    # Substitui múltiplos espaços/quebras de linha por um padrão consistente
    texto_normalizado = re.sub(r'\n\s*\n', '\n\n', texto.strip())
    # Divide pelos parágrafos (duas quebras de linha) e remove parágrafos vazios
    paragrafos = [p.strip() for p in texto_normalizado.split('\n\n') if p.strip()]
    return paragrafos

paragrafos = dividir_em_paragrafos(texto_carregado)

# Exibir os primeiros parágrafos para verificação
# print("Parágrafos extraídos:")
# for i, p in enumerate(paragrafos):
#     print(f"--- Parágrafo {i+1} ---")
#     print(p)
#     print("-" * 20)
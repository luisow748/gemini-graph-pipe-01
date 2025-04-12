from service.text_processing.paragraph_division import dividir_em_paragrafos


def ler_texto(fonte_texto: str, eh_arquivo: bool = False) -> str:
    """
    Lê texto de um arquivo ou de uma string.

    Args:
        fonte_texto: O caminho do arquivo ou a string de texto.
        eh_arquivo: True se fonte_texto for um caminho de arquivo, False caso contrário.

    Returns:
        O conteúdo do texto como uma string.
    """
    if eh_arquivo:
        try:
            with open(fonte_texto, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em {fonte_texto}")
            return ""
    else:
        return fonte_texto

# Exemplo de texto (string)



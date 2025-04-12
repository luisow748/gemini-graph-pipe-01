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
texto_exemplo = """
O desenvolvimento de software moderno exige conhecimento em diversas linguagens de programação, como Python, Java e JavaScript. As equipes ágeis colaboram para entregar valor continuamente aos usuários, utilizando práticas como Integração Contínua e Entrega Contínua (CI/CD). A qualidade do código é fundamental, sendo garantida por testes unitários, de integração e end-to-end.

A ciência de dados, por outro lado, foca na extração de conhecimento a partir de dados. Cientistas de dados utilizam técnicas estatísticas e de machine learning para construir modelos preditivos e descritivos. Ferramentas como Pandas, NumPy e Scikit-learn são essenciais no dia a dia desses profissionais. A visualização de dados com Matplotlib ou Seaborn ajuda a comunicar os achados de forma eficaz.

Ambas as áreas, desenvolvimento de software e ciência de dados, estão em constante evolução. Novas tecnologias e abordagens surgem frequentemente, demandando aprendizado contínuo. A inteligência artificial e o machine learning estão cada vez mais presentes no desenvolvimento de software, automatizando tarefas e criando funcionalidades mais inteligentes.

Profissionais que combinam habilidades de engenharia de software com conhecimentos em ciência de dados são altamente valorizados no mercado. Eles são capazes de construir pipelines de dados robustos, implementar modelos de machine learning em produção e desenvolver aplicações data-driven completas. A colaboração entre engenheiros e cientistas de dados é crucial para o sucesso de projetos complexos.
"""

texto_carregado = ler_texto(texto_exemplo)
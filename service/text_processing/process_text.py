from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

from service.text_processing.paragraph_division import dividir_em_paragrafos
from service.text_processing.read_text import ler_texto

embedding_model_name = 'all-MiniLM-L6-v2'
embedding_model = SentenceTransformer(embedding_model_name)

topic_model = BERTopic(embedding_model=embedding_model,
                       language="multilingual", 
                       calculate_probabilities=True, 
                       verbose=True)

texto_exemplo = """
O desenvolvimento de software moderno exige conhecimento em diversas linguagens de programação, como Python, Java e JavaScript. As equipes ágeis colaboram para entregar valor continuamente aos usuários, utilizando práticas como Integração Contínua e Entrega Contínua (CI/CD). A qualidade do código é fundamental, sendo garantida por testes unitários, de integração e end-to-end.

A ciência de dados, por outro lado, foca na extração de conhecimento a partir de dados. Cientistas de dados utilizam técnicas estatísticas e de machine learning para construir modelos preditivos e descritivos. Ferramentas como Pandas, NumPy e Scikit-learn são essenciais no dia a dia desses profissionais. A visualização de dados com Matplotlib ou Seaborn ajuda a comunicar os achados de forma eficaz.

Ambas as áreas, desenvolvimento de software e ciência de dados, estão em constante evolução. Novas tecnologias e abordagens surgem frequentemente, demandando aprendizado contínuo. A inteligência artificial e o machine learning estão cada vez mais presentes no desenvolvimento de software, automatizando tarefas e criando funcionalidades mais inteligentes.

Profissionais que combinam habilidades de engenharia de software com conhecimentos em ciência de dados são altamente valorizados no mercado. Eles são capazes de construir pipelines de dados robustos, implementar modelos de machine learning em produção e desenvolver aplicações data-driven completas. A colaboração entre engenheiros e cientistas de dados é crucial para o sucesso de projetos complexos.
"""

texto_carregado = ler_texto(texto_exemplo)

paragrafos = dividir_em_paragrafos(texto_carregado)
topics, probs = topic_model.fit_transform(paragrafos)


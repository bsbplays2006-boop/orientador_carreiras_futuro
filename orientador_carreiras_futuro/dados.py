# dados.py
from modelos import Carreira

# Exemplo de conjunto de carreiras com pesos (quanto cada competência importa)
CARREIRAS_PADRAO = [
    Carreira(
        nome="Cientista de Dados",
        descricao="Analisa dados, cria modelos preditivos e extrai insights.",
        competencias_necessarias={
            "Estatística": 9, "Python": 9, "Machine Learning": 9,
            "Lógica": 7, "Comunicação": 6, "Criatividade": 5
        },
        trilha=[
            ("Fundamentos de Probabilidade e Estatística", "Curso online - Estatística básica"),
            ("Programação em Python para Dados", "Livro ou curso Python"),
            ("Machine Learning: teoria e prática", "curso prático com projetos")
        ]
    ),
    Carreira(
        nome="Engenheiro de Software",
        descricao="Projeta, implementa e mantém sistemas de software.",
        competencias_necessarias={
            "Lógica": 9, "Estruturas de Dados": 8, "Python": 7,
            "Arquitetura de Software": 7, "Colaboração": 8
        },
        trilha=[
            ("Algoritmos e Estruturas de Dados", "Curso universitário ou MOOC"),
            ("Práticas de engenharia (Git, testes)", "Hands-on com repositório"),
            ("Projetos: construir aplicações completas", "Portfólio no GitHub")
        ]
    ),
    Carreira(
        nome="Especialista em Experiência do Usuário (UX)",
        descricao="Pesquisa e projeta interações e experiências para usuários.",
        competencias_necessarias={
            "Pesquisa de Usuário": 8, "Design Thinking": 8, "Comunicação": 9,
            "Criatividade": 8, "Empatia": 9
        },
        trilha=[
            ("Fundamentos de UX e Design Thinking", "curso introdutório"),
            ("Pesquisa com usuários e prototipagem", "projetos práticos"),
            ("Portfólio de estudos de caso", "construir estudos de caso")
        ]
    ),
    Carreira(
        nome="Analista de Cibersegurança",
        descricao="Protege sistemas, detecta vulnerabilidades e responde a incidentes.",
        competencias_necessarias={
            "Redes": 8, "Sistemas Operacionais": 7, "Segurança": 9,
            "Lógica": 6, "Análise": 7
        },
        trilha=[
            ("Fundamentos de redes e sistemas", "lab prático de redes"),
            ("Noções de segurança e pentesting", "cursos e labs"),
            ("Certificações (ex: CompTIA, OSCP)", "estudo direcionado")
        ]
    )
]

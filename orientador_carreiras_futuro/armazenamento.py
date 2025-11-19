# armazenamento.py
import json
from modelos import Perfil, Competencia
from typing import List
import os

ARQUIVO = "perfis.json"

def salvar_perfis(perfis: List[Perfil], arquivo: str = ARQUIVO):
    data = []
    for p in perfis:
        data.append({
            "nome": p.nome,
            "idade": p.idade,
            "email": p.email,
            "criado_em": p.criado_em,
            "competencias": [{"nome": c.nome, "tipo": c.tipo, "nivel": c.nivel} for c in p.competencias]
        })
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def carregar_perfis(arquivo: str = ARQUIVO):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    perfis = []
    for p in data:
        perfil = Perfil(nome=p["nome"], idade=p["idade"], email=p["email"])
        perfil.criado_em = p.get("criado_em", perfil.criado_em)
        for c in p.get("competencias", []):
            perfil.adicionar_competencia(c["nome"], c["tipo"], c["nivel"])
        perfis.append(perfil)
    return perfis

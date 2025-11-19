# modelos.py
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import datetime

@dataclass
class Competencia:
    nome: str
    tipo: str  # 'tecnica' ou 'comportamental'
    nivel: int  # 0 a 10

    def __post_init__(self):
        if self.nivel < 0: self.nivel = 0
        if self.nivel > 10: self.nivel = 10

@dataclass
class Perfil:
    nome: str
    idade: int
    email: str
    competencias: List[Competencia] = field(default_factory=list)
    criado_em: str = field(default_factory=lambda: datetime.datetime.now().isoformat())

    def adicionar_competencia(self, nome: str, tipo: str, nivel: int):
        # atualiza caso já exista
        for c in self.competencias:
            if c.nome.lower() == nome.lower():
                c.tipo = tipo
                c.nivel = max(0, min(10, nivel))
                return
        self.competencias.append(Competencia(nome=nome, tipo=tipo, nivel=max(0, min(10, nivel))))

    def obter_valores_competencias(self) -> Dict[str, int]:
        return {c.nome: c.nivel for c in self.competencias}

    def media_tecnicas(self) -> float:
        techs = [c.nivel for c in self.competencias if c.tipo == 'tecnica']
        return sum(techs)/len(techs) if techs else 0.0

    def media_comportamentais(self) -> float:
        comps = [c.nivel for c in self.competencias if c.tipo == 'comportamental']
        return sum(comps)/len(comps) if comps else 0.0

@dataclass
class Carreira:
    nome: str
    descricao: str
    competencias_necessarias: Dict[str, int]  # nome -> peso (0-10)
    trilha: List[Tuple[str, str]] = field(default_factory=list)
    # trilha: lista de (etapa, recurso_sugerido)

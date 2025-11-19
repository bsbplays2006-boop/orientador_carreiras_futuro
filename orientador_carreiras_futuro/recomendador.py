# recomendador.py
from modelos import Perfil, Carreira
from typing import List, Dict, Tuple
import math

class Recomendador:
    def __init__(self, carreiras: List[Carreira]):
        self.carreiras = carreiras

    def _pontuar_para_carreira(self, perfil: Perfil, carreira: Carreira) -> Dict:
        # Calcula correspondência entre perfil e carreira, retornando uma dict com pontuação e gaps
        competencias_perfil = perfil.obter_valores_competencias()
        peso_total = sum(carreira.competencias_necessarias.values()) or 1
        soma = 0.0
        gaps = {}
        for nome_comp, peso in carreira.competencias_necessarias.items():
            nivel_usuario = competencias_perfil.get(nome_comp, 0)
            # contribuição: quanto do peso é coberto pelo nível (normaliza nível/10)
            contrib = (nivel_usuario / 10.0) * peso
            soma += contrib
            # gap: quanto falta para atingir peso máximo
            nivel_ideal = (peso/10.0)*10  # simplificado: nivel ideal proporcional ao peso
            falta = max(0, peso - (nivel_usuario * (peso/10.0)))
            if falta > 0:
                gaps[nome_comp] = round(falta, 2)
        # score percentual
        score = (soma / peso_total) * 100
        # melhorar interpretabilidade: transformar extremos
        score = round(min(100.0, max(0.0, score)), 2)
        return {"carreira": carreira, "score": score, "gaps": gaps}

    def gerar_recomendacoes(self, perfil: Perfil, top_n: int = 3) -> List[Dict]:
        avaliacoes = [self._pontuar_para_carreira(perfil, c) for c in self.carreiras]
        avaliacoes.sort(key=lambda x: x['score'], reverse=True)
        # Para cada carreira no top, sugerir prioridade nas principais lacunas
        resultados = []
        for a in avaliacoes[:top_n]:
            carreira = a['carreira']
            gaps_ordenados = sorted(a['gaps'].items(), key=lambda kv: kv[1], reverse=True)
            sugestoes_trilha = []
            # mapear gaps para itens da trilha (heurística simplificada)
            for gap_nome, falt in gaps_ordenados[:3]:
                # procurar etapas da trilha que contenham palavras-chave similares
                for etapa, recurso in carreira.trilha:
                    if gap_nome.lower().split()[0] in etapa.lower() or gap_nome.lower().split()[0] in recurso.lower():
                        sugestoes_trilha.append((gap_nome, etapa, recurso))
                # se não encontrou, sugere primeira etapa da trilha
                if not sugestoes_trilha:
                    sugestoes_trilha = [(gap_nome, *carreira.trilha[0])]
            resultados.append({
                "nome": carreira.nome,
                "descricao": carreira.descricao,
                "score": a['score'],
                "gaps_principais": gaps_ordenados[:5],
                "sugestoes_trilha": sugestoes_trilha[:5]
            })
        return resultados

    def explicar_recomendacao(self, recomendacao: Dict) -> str:
        texto = f"{recomendacao['nome']} — {recomendacao['score']}% de compatibilidade\n"
        texto += f"{recomendacao['descricao']}\n"
        if recomendacao['gaps_principais']:
            texto += "Principais lacunas:\n"
            for nome, falta in recomendacao['gaps_principais']:
                texto += f" - {nome}: falta aproximada {falta}\n"
        if recomendacao['sugestoes_trilha']:
            texto += "Sugestões de trilha / próximos passos:\n"
            for item in recomendacao['sugestoes_trilha']:
                # item pode ter formato (gap_nome, etapa, recurso)
                gap, etapa, recurso = item
                texto += f" * Para melhorar '{gap}': {etapa} — {recurso}\n"
        return texto

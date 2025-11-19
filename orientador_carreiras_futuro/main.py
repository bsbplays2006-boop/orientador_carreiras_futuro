# main.py
from modelos import Perfil
from dados import CARREIRAS_PADRAO
from recomendador import Recomendador
from armazenamento import salvar_perfis, carregar_perfis
import sys

def mostrar_menu():
    print("\n=== ORIENTADOR DE CARREIRAS (CLI) ===")
    print("1) Cadastrar novo perfil")
    print("2) Listar perfis")
    print("3) Editar perfil (adicionar/atualizar competência)")
    print("4) Analisar perfil e obter recomendações")
    print("5) Salvar perfis")
    print("6) Carregar perfis")
    print("0) Sair")

def cadastrar_perfil(perfis):
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("E-mail: ").strip()
    try:
        idade = int(idade)
    except:
        idade = 0
    perfil = Perfil(nome=nome, idade=idade, email=email)
    perfis.append(perfil)
    print(f"Perfil '{nome}' criado.")

def listar_perfis(perfis):
    if not perfis:
        print("Nenhum perfil cadastrado.")
        return
    for i, p in enumerate(perfis, start=1):
        print(f"[{i}] {p.nome} — {p.email} — {len(p.competencias)} competências — criado em {p.criado_em}")

def selecionar_perfil(perfis):
    listar_perfis(perfis)
    if not perfis:
        return None
    escolha = input("Escolha o número do perfil: ").strip()
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(perfis):
            return perfis[idx]
    except:
        pass
    print("Seleção inválida.")
    return None

def editar_perfil(perfil):
    if not perfil:
        print("Perfil não selecionado.")
        return
    while True:
        nome_comp = input("Nome da competência (ou ENTER para voltar): ").strip()
        if nome_comp == "":
            break
        tipo = input("Tipo ('tecnica' ou 'comportamental'): ").strip().lower()
        if tipo not in ("tecnica", "comportamental"):
            print("Tipo inválido, usando 'tecnica'.")
            tipo = "tecnica"
        nivel = input("Nível (0-10): ").strip()
        try:
            nivel = int(nivel)
        except:
            nivel = 0
        perfil.adicionar_competencia(nome_comp, tipo, nivel)
        print(f"Competência '{nome_comp}' adicionada/atualizada com nível {nivel}.")

def analisar_perfil(perfis, recomendador):
    perfil = selecionar_perfil(perfis)
    if not perfil:
        return
    print(f"\nAnalisando perfil: {perfil.nome}")
    print(f"Média competências técnicas: {perfil.media_tecnicas():.2f}")
    print(f"Média competências comportamentais: {perfil.media_comportamentais():.2f}")
    recs = recomendador.gerar_recomendacoes(perfil, top_n=3)
    for r in recs:
        print("\n---")
        print(recomendador.explicar_recomendacao(r))

def main():
    perfis = []
    # tenta carregar automaticamente ao iniciar (silencioso)
    try:
        perfis = carregar_perfis()
        if perfis:
            print(f"{len(perfis)} perfis carregados automaticamente.")
    except Exception as e:
        print("Aviso: não foi possível carregar perfis automáticos.", e)

    recomendador = Recomendador(CARREIRAS_PADRAO)
    while True:
        mostrar_menu()
        op = input("Opção: ").strip()
        if op == "1":
            cadastrar_perfil(perfis)
        elif op == "2":
            listar_perfis(perfis)
        elif op == "3":
            p = selecionar_perfil(perfis)
            editar_perfil(p)
        elif op == "4":
            analisar_perfil(perfis, recomendador)
        elif op == "5":
            salvar_perfis(perfis)
            print("Perfis salvos em 'perfis.json'.")
        elif op == "6":
            perfis = carregar_perfis()
            print(f"{len(perfis)} perfis carregados.")
        elif op == "0":
            print("Encerrando. Até logo!")
            sys.exit(0)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

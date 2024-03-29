"""
Este script é uma ferramenta de análise de espaço de armazenamento que calcula e exibe o tamanho de cada diretório dentro de um diretório especificado, neste caso, a pasta "OneDrive" no diretório home do usuário. Ele ignora arquivos e diretórios ocultos (aqueles cujos nomes começam com ".") na sua contagem. O tamanho é apresentado em gigabytes (GB) com precisão de duas casas decimais. O script permite especificar a profundidade da análise, o que significa que ele pode ser configurado para examinar subdiretórios até um nível de profundidade definido pelo usuário. Por padrão, a profundidade é definida como 1, significando que apenas o primeiro nível de diretórios dentro do caminho especificado será analisado. A saída é formatada para refletir a estrutura hierárquica dos diretórios, com subdiretórios sendo indentados para indicar sua profundidade. Antes de iniciar a análise, o script limpa o console para garantir que a saída seja fácil de ler.
"""

import pathlib
import os
import time

os.system("clear")

print("PRIMEIRA EXECUÇÃO - SCRIPT PROFESSOR")

def retornaTamanhoDiretorios(caminho, profundidade = 1, tamanhoLinha = 1):
    for diretorio in caminho.glob("*"):
        if diretorio.is_dir() and not diretorio.name.startswith("."):
            tamanhoDir = 0
            for arquivo in diretorio.glob("**/*"):
                if arquivo.is_file():
                    tamanhoDir += os.path.getsize(arquivo)
            print("--" * tamanhoLinha, diretorio.name, round(tamanhoDir / 1024 / 1024 / 1024, 2), "GB")
        if profundidade > 1:
            retornaTamanhoDiretorios(diretorio, profundidade - 1, tamanhoLinha + 1)

tempoInicio = time.time()

caminho = pathlib.Path.home() / "OneDrive"
print(f"Caminho: {caminho}")
retornaTamanhoDiretorios(caminho)

tempoFim = time.time()

print(f"Tempo de execução: {(tempoFim - tempoInicio):.2f} segundos.")

print("\nSEGUNDA EXECUÇÃO - SCRIPT CHATGPT COM TAMANHO TOTAL DE DIRETÓRIOS")

def retornaTamanhoDiretorios_(caminho_, profundidade_ = 1, tamanhoLinha_ = 1, tamanhoTotal_ = [0]):
    for diretorio_ in caminho_.glob("*"):
        if diretorio_.is_dir() and not diretorio_.name.startswith("."):
            tamanhoDir_ = 0
            for arquivo_ in diretorio_.glob("**/*"):
                if arquivo_.is_file():
                    tamanhoArquivo_ = os.path.getsize(arquivo_)
                    tamanhoDir_ += tamanhoArquivo_
                    tamanhoTotal_[0] += tamanhoArquivo_
            print("--" * tamanhoLinha_, diretorio_.name, round(tamanhoDir_ / 1024 / 1024 / 1024, 2), "GB")
        if profundidade_ > 1:
            retornaTamanhoDiretorios_(diretorio_, profundidade_ - 1, tamanhoLinha_ + 1, tamanhoTotal_)
    return tamanhoTotal_[0]

tempoInicio_ = time.time()

caminho_ = pathlib.Path.home() / "OneDrive"
print(f"Caminho: {caminho_}")
tamanhoTotal_ = retornaTamanhoDiretorios_(caminho_)

tempoFim_ = time.time()

print(f"Tempo de execução: {(tempoFim_ - tempoInicio_):.2f} segundos.")
print(f"Tamanho total dos diretórios: {round(tamanhoTotal_ / 1024 / 1024 / 1024, 2)} GB")

print("\nTERCEIRA EXECUÇÃO - SCRIPT CHATGPT COM PEDIDO DE MELHORIA DO SCRIPT")

def retorna_tamanho_diretorios(caminho, profundidade=1, tamanho_linha=1, tamanho_total=[0]):
    for entrada in caminho.iterdir():
        if entrada.is_dir() and not entrada.name.startswith("."):
            tamanho_dir = 0
            for root, _, files in os.walk(entrada, topdown=True):
                for nome_arquivo in files:
                    try:
                        caminho_arquivo = os.path.join(root, nome_arquivo)
                        tamanho_arquivo = os.path.getsize(caminho_arquivo)
                        tamanho_dir += tamanho_arquivo
                        tamanho_total[0] += tamanho_arquivo
                    except FileNotFoundError:
                        # Ignora arquivos que possam ter sido removidos durante a varredura
                        pass
            print("--" * tamanho_linha, entrada.name, round(tamanho_dir / 1024 ** 3, 2), "GB")
        if profundidade > 1:
            retorna_tamanho_diretorios(entrada, profundidade - 1, tamanho_linha + 1, tamanho_total)
    return tamanho_total[0]

tempo_inicio = time.time()

caminho = pathlib.Path.home() / "OneDrive"
print(f"Caminho: {caminho}")
tamanho_total = retorna_tamanho_diretorios(caminho)

tempo_fim = time.time()

print(f"Tempo de execução: {(tempo_fim - tempo_inicio):.2f} segundos.")
print(f"Tamanho total dos diretórios: {round(tamanho_total / 1024 ** 3, 2)} GB")

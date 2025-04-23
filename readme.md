<div align="center">
    <h1>Case Técnico-Estágio ScientifiCloud</h1>
    <p>
       Ferramenta de linha de comando (CLI) para análise das dimensões dos territórios brasileiros. Permite consultar a área de um território específico ou comparar dois territórios, gerando gráficos que auxiliam na tomada de decisões estratégicas para expansão empresarial.
    </p>
</div>

</br>

## Tecnologias usadas/Requisitos de sistema
No desenvolvimento do projeto foi utilizado:
- <a href="https://www.python.org/downloads/">Python3</a> 
- <a href="https://docs.python.org/pt-br/3/installing/index.html">Python3-PIP</a>
- <a href="https://docs.python.org/3/library/venv.html">Python3-VENV</a> 

### Principais bibliotecas

- <a href="https://docs.python.org/3/library/argparse.html">Argparse</a>
- <a href="https://docs.python.org/3/library/sqlite3.html">Python3 sqlite3</a>
- <a href="https://docs.python.org/3/howto/logging.html"> Logging</a>

## Download
Faça o download da CLI para o seu sistema operacional na seção de <a href="https://github.com/LuisHenriqueDaSilv/TesteTecnicoScientifiCloud/releases/tag/first">releases</a>.

## Como usar

``` bash
# No Linux, torne o arquivo executável (se necessário)
chmod +x territory

# Execute
./territory [comando] [argumentos]
``` 

### Comandos Disponíveis

#### dimension
Retorna a dimensão (em km²) de um território brasileiro informado por ID ou nome, e gera um gráfico ilustrativo em formato de imagem.

<strong>Uso:</strong>
```bash
./territory dimension {id} {caminho_para_o_grafico}
#Você pode usar --id ou --name para identificar o território.
```

#### compare
Compara as dimensões (em km²) de dois territórios brasileiros, retornando a diferença entre eles e gerando um gráfico ilustrativo em formato de imagem.

<strong>Uso:</strong>

```bash
./territory compare {id1} {id2} {caminho_para_o_grafico}
```
</br>

## Build do projeto

Com todos os requisitos do sistema devidamente instalados, siga o passo a passo abaixo para gerar a build da CLI em sua máquina:

1) Clone o repositório em sua máquina:

```bash
    git clone https://github.com/LuisHenriqueDaSilv/TesteTecnicoScientifiCloud.git # Clona o repositório
    cd TesteTecnicoScientifiCloud # Entra no diretório 
```

<strong>Recomenda-se utilizar um ambiente virtual <a href="https://docs.python.org/3/library/venv.html">venv</a> para instalar as dependencias:</strong>
 
```bash
python3 -m venv env # Cria o ambiente virtual
# Para LINUX:
source ./env/bin/activate
# Para WINDOWS:
env\Scripts\activate.bat
```

2) Utilizando o pip, instale as dependencias do projeto:
``` bash
    pip install -r requirements.txt
```

3) Gere o build da aplicação:
``` bash
# No linux:
pyinstaller -w -F src/main.py -n "territory" --console
# No windows:
python -m PyInstaller -w -F src/main.py -n "territory" --console
```
</br>
Caso tudo tenha ocorrido corretamete, deve ter sido criado o arquivo executavel dentro da pasta <strong>/dist/territory</strong>

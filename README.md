## DevOps&ML
Está projeto tem o objetivo de integra uma rede de Petri com a máquina de estado para monitoras e atualiza modelos de inferência de apredizagem de dados continuamente, demandado apartir do comportamento do modelo atual frente a novos dados na execução do sistema.

### Setup
1. Abra o terminal de comando e certifique de que o Python já não está instalado.
```
cmd
$ python --version
```
2. Navegue para o diretorio do projeto.
3. Gere o ambiente inicial:
```
$ python -m venv env
```
4. Ativar o Ambiente virtual:
```
$ env\Scripts\activate
```
5. Efetuar instalação do Django
```
(env)$ pip install -r requirements.txt
```
6. Erguer o servidor socket
```
(env)$ python SocketServer.py
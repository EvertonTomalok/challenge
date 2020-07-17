# Makefile

## Setup

- `make necessary-packs` -> instala os pacotes necessários no SO.
- `make setup` -> Instala o necessário para rodar a aplicação localmente (fora dos containers).
- `make setup-dev` -> Também instala as dependências de desenvolvimento/testes localmente (fora dos containers).
- `make prod` -> utilizado pelo dockerfile para criar as dependências, e rodar os testes necessários e executar o linter.
- `make prod-no-tests` -> utilizado pelo dockerfile para criar as dependências, mas não executa os testes necessários e o linter.

## Aplicação

### Build 

- `make up` -> Inicia a aplicação.
- `make down` -> Desliga a aplicação.
- `make restart` -> Reinicia a aplicação.
- `make build` -> Instala todas as dependências do projeto e inicia a aplicação, para toda vez que esse comando for rodado, todo o escopo de containers será reconstruído. 
Esta regra não leva em consideração o `linter` e os `testes` do projeto.
- `make sbuild` -> Mesma instrução acima, porém irá rodar com permissão `root`.
- `make build-prod`: Mesma função  do build, mas realiza os `testes` e executa o `linter` antes de construir a imagem. Se houver alguma falha, a imagem não é construida.
- `make sbuild-prod`: Mesma intrução acima, mas roda com permissão `root`


### Celery workers

- `scale-worker` -> Escala para 5 workers Celery, sem recriar a aplicação
- `single-worker` -> Downgrade para apenas 1 worker.

## Testes

### Unitário

- `make test` -> Realiza os testes.
- `make test-cov` -> Gera um relátorio html sobre a cobertura de testes da aplicação, na pasta `htmlcov`.
- `make html-coverage` -> Abre o `google-chrome` e exibe o relátorio de cobertura dos testes.


### End-To-End


- `make e2e`


Obs.: Necessário servidor ativo e as dependências do projeto instaladas em sua máquina ( `make setup` )



## Padrão de escrita

- `make lint` -> Procura por melhoria no código
- `make format` -> Aplica de forma automática melhorias no código, como ordenação de `imports` e outras features.

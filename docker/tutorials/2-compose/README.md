# API de Gerenciamento de Tarefas

Uma aplicação simples em Flask que fornece uma API RESTful para gerenciar tarefas com operações CRUD. A aplicação usa MySQL para armazenamento de dados e é containerizada usando Docker.

## Pré-requisitos

- Docker
- Docker Compose

## Começando

1. Clone este repositório
2. Navegue até o diretório do projeto
3. Execute o seguinte comando para construir e iniciar os contêineres:

```bash
make up
```

Alternativamente, você pode usar o comando Docker Compose diretamente:

```bash
docker-compose up -d
```

Isso iniciará dois contêineres:
- Uma aplicação Flask rodando na porta 5000
- Um banco de dados MySQL rodando na porta 3306

## Endpoints da API

### Obter todas as tarefas
```
GET /tasks
```

### Obter uma tarefa específica
```
GET /tasks/{task_id}
```

### Criar uma nova tarefa
```
POST /tasks
```
Corpo da requisição:
```json
{
  "title": "Título da tarefa",
  "description": "Descrição da tarefa",
  "status": "pendente"
}
```
Nota: Apenas "title" é obrigatório. "description" e "status" são opcionais.

### Atualizar uma tarefa
```
PUT /tasks/{task_id}
```
Corpo da requisição:
```json
{
  "title": "Título atualizado",
  "description": "Descrição atualizada",
  "status": "concluída"
}
```
Nota: Todos os campos são opcionais. Apenas os campos fornecidos serão atualizados.

### Excluir uma tarefa
```
DELETE /tasks/{task_id}
```

## Exemplos de Uso

### Criar uma tarefa
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Aprender Docker", "description": "Aprender Docker e Docker Compose", "status": "em-andamento"}'
```

### Obter todas as tarefas
```bash
curl -X GET http://localhost:5000/tasks
```

### Obter uma tarefa específica
```bash
curl -X GET http://localhost:5000/tasks/1
```

### Atualizar uma tarefa
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "concluída"}'
```

### Excluir uma tarefa
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

## Parando a Aplicação

Para parar os contêineres, execute:

```bash
make down
```

Para parar os contêineres e remover os volumes (isso excluirá todos os dados), execute:

```bash
make clean
```

Alternativamente, você pode usar os comandos Docker Compose diretamente:

```bash
docker-compose down
```

```bash
docker-compose down -v
```

## Comandos do Makefile

Este projeto inclui um Makefile para simplificar as operações do Docker Compose. Aqui estão os comandos disponíveis:

- `make docker-build`: Constrói a imagem Docker da aplicação usando o Dockerfile
- `make build`: Constrói os serviços definidos no docker-compose.yml
- `make up`: Inicia os contêineres em modo detached (background)
- `make down`: Para e remove os contêineres
- `make logs`: Exibe os logs de todos os serviços
- `make logs-app`: Exibe os logs apenas do serviço da aplicação
- `make logs-db`: Exibe os logs apenas do serviço do banco de dados
- `make ps`: Lista os contêineres em execução
- `make restart`: Reinicia todos os serviços
- `make clean`: Para os contêineres, remove os volumes e limpa recursos Docker não utilizados

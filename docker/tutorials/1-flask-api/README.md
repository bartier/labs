# Tutorial Flask API com Docker

## Pré-requisitos

Antes de começar, você precisa ter o Docker e o Git instalados em seu sistema.

### Instalação do Git

#### Windows
1. Baixe o instalador do Git em https://git-scm.com/downloads
2. Execute o instalador e siga as instruções
3. Para usar os comandos Git, abra o Git Bash:
   - Clique com o botão direito em qualquer pasta
   - Selecione "Git Bash Here" no menu de contexto
   - Ou pesquise "Git Bash" no menu Iniciar
4. Verifique a instalação digitando: `git --version`

#### macOS
Execute o seguinte comando no terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

#### Linux (Ubuntu)
Execute o seguinte comando no terminal:

```bash
sudo apt-get update
sudo apt-get install git
```

### Instalação do Docker

#### Windows e macOS
1. Baixe o Docker Desktop em https://www.docker.com/products/docker-desktop
2. Execute o instalador e siga as instruções
3. Verifique a instalação: `docker --version`

#### Linux (Ubuntu)
```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

## Sobre a API Flask

Esta é uma API simples desenvolvida com Flask que gera números aleatórios. A API possui o seguinte endpoint:

- `GET /random`: Retorna um número aleatório entre 1 e 100

## Usando Docker

### Construir e Executar

```bash
# Build da imagem
docker build -t flask-api .

# Executar o container
docker run -d -p 5000:5000 --name flask-container flask-api
```

### Gerenciamento do Container

```bash
# Visualizar logs
docker logs flask-container

# Listar containers
docker ps

# Parar/Iniciar container
docker stop flask-container
docker start flask-container

# Remover container
docker rm flask-container
```

## Testando a API

Após iniciar o container, teste a API usando curl ou Postman:

```bash
# Obter um número aleatório
curl http://localhost:5000/random
```

A resposta será um JSON com um número aleatório:
```json
{"number": 42}
```
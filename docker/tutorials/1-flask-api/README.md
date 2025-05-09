
# Tutorial: API Flask Simples com Docker

Este tutorial guia você na execução de uma API Flask simples que gera números aleatórios, utilizando Docker para containerização. As instruções são fornecidas para Windows, macOS e Linux.

## Pré-requisitos

Antes de começar, você precisará de um terminal ou linha de comando e das seguintes ferramentas instaladas:

1. **Git:** Para clonar o repositório.  
2. **Docker:** Para construir e executar a aplicação containerizada.

### Ambiente de Terminal

- **Windows:** É **altamente recomendado** usar o [Windows Subsystem for Linux (WSL 2)](https://learn.microsoft.com/pt-br/windows/wsl/install). O WSL 2 oferece um ambiente Linux integrado ao Windows, proporcionando a melhor compatibilidade e performance para Docker. Após instalar o WSL (exemplo: Ubuntu via Microsoft Store), você pode abrir o terminal WSL (ex: "Ubuntu" no Menu Iniciar). Alternativamente, para comandos Git *apenas*, você pode usar o Git Bash. No entanto, **todos os comandos `docker` devem ser executados preferencialmente dentro do terminal WSL**.

- **macOS:** Use o aplicativo Terminal padrão (`Applications > Utilities > Terminal`).

- **Linux:** Use o terminal padrão da sua distribuição (ex: GNOME Terminal, Konsole, etc.).

## Instalação do Git

### Windows (com WSL ou Git Bash)

1. **Via WSL:**
    ```bash
    sudo apt update
    sudo apt install git -y
    ```

2. **Via Git Bash (Alternativa):**
    - Baixe o instalador em [https://git-scm.com/downloads](https://git-scm.com/downloads).
    - Execute o instalador e siga as instruções.
    - Abra o Git Bash.

3. **Verificação:**
    ```bash
    git --version
    ```

### macOS (usando Homebrew)

1. Instale o Homebrew (caso ainda não tenha):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Instale o Git:
    ```bash
    brew install git
    ```

3. Verifique:
    ```bash
    git --version
    ```

### Linux (Exemplo para Ubuntu/Debian)

1. Instale o Git:
    ```bash
    sudo apt-get update
    sudo apt-get install git -y
    ```

2. Verifique:
    ```bash
    git --version
    ```

## Instalação do Docker

### Windows e macOS (usando Docker Desktop)

1. Baixe e instale o Docker Desktop em [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

2. **Importante para Windows:** Habilite a integração com o WSL 2 nas configurações:
   `Settings > Resources > WSL Integration`.

3. Verifique:
    ```bash
    docker --version
    ```

### Linux (Exemplo para Ubuntu/Debian)

1. Instale o Docker Engine:
    ```bash
    sudo apt-get update
    sudo apt-get install docker.io -y
    ```

2. Inicie e habilite o serviço:
    ```bash
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

3. (Opcional) Adicione seu usuário ao grupo `docker`:
    ```bash
    sudo usermod -aG docker $USER
    ```

4. Verifique:
    ```bash
    docker --version
    ```

## Começando

1. **Clone o Repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-diretorio-clonado>
    ```

2. **Execute os comandos Docker dentro do diretório clonado.**

## Sobre a API Flask

API simples com Flask que gera números aleatórios.

- `GET /random`: Retorna um número entre 1 e 100 em JSON.

## Usando Docker

### Construir a Imagem Docker

```bash
docker build -t teste .
```

### Executar o Container Docker

```bash
docker run -d -p 9000:8000
```

- `-d`: Modo background
- `-p 9000:8000`: Mapeia porta host:container
- `teste`: Nome da imagem

### Gerenciamento Básico do Container

```bash
# Ver logs
docker logs <ID do container>

# Containers em execução
docker ps

# Parar container
docker stop flask-container

# Iniciar container
docker start flask-container

# Remover container
docker rm flask-container
```

## Testando a API

- **curl (linha de comando):**
    ```bash
    curl http://localhost:9000/random
    ```

- **Navegador:**  
  Acesse [http://localhost:9000/random](http://localhost:9000/random)

Resposta esperada (exemplo):

```json
{
  "number": 42
}
```

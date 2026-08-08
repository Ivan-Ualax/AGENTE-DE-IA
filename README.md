# Mestre AI — MVP 0.1.0

Base inicial do agente de desenvolvimento pessoal descrito no projeto.

## Requisitos

- Python 3.12 ou superior
- Git
- Uma chave de API compatível com o SDK da OpenAI

## Instalação no Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Abra o arquivo `.env` e substitua `coloque_sua_chave_aqui` pela chave real.

## Executar

```powershell
uvicorn app.main:app --reload
```

Acesse: `http://127.0.0.1:8000`

## Testes

```powershell
pytest
```

## Entregue neste marco

- API FastAPI
- Interface web inicial
- Endpoint de saúde
- Endpoint de chat
- Personalidade básica
- Configuração por `.env`
- Testes iniciais

## Próximo marco

Adicionar ferramentas seguras para listar, ler e pesquisar arquivos dentro de um diretório autorizado.

# PMICR (Project for Managing Individual and Corporate Registrations)

> **Planejamento**
Estrutura sólida para organizar dados de forma estratégica e segura.
>
> **Monitoramento**
Acompanhamento contínuo dos registros para garantir integridade e precisão.
>
> **Integração**
Unificação de dados individuais e corporativos em um ecossistema fluido.
>
> **Conformidade**
Adesão rigorosa às normas e padrões de registro vigentes.
>
> **Resultados**
Otimização de processos que gera valor tanto para pessoas quanto para empresas.
>

## Requisitos

- Python 3.14+
- Django 6.0+
- Outras dependências em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd gestao_pessoas
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## Uso

Acesse o sistema em `http://localhost:8000/admin/` para o painel administrativo.

## Testes

Execute os testes unitários:

```bash
# Executar todos os testes
python manage.py test

# Executar testes de um app específico

# Com cobertura

```

## Estrutura de Apps

### Principios seguidos:
1. **Responsabilidade Única**: Cada app tem uma função bem definida
2. **DRY (Don't Repeat Yourself)**: Modelos base reutilizáveis
3. **Testabilidade**: Todos os apps possuem testes unitários
4. **Extensibilidade**: Fácil adicionar novas funcionalidades

### Relacionamentos:
- Cada app especializado estende os modelos de pessoas conforme sua necessidade

## Validações

O sistema inclui validações para documentos brasileiros:
- **CPF**: Validação completa com dígitos verificadores
- **CNPJ**: Validação completa com dígitos verificadores
- **CEP**: Formato e normalização

## Contribuição

1. Faça um fork do projeto


## Licença

Este projeto é licenciado sob a MIT License.

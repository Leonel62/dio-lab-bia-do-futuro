# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades do usuário |
| `transacoes.csv` | CSV | Analisar os gastos e ganhos do cliente para criação das planilhas de análise |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Removi os dados de histórico de atendimento e produtos financeiros, pois não vejo a necessidade de sua presença no que meu agente propõe.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

# CSVs
transacoes = pd.read_csv('data/transacoes.csv')

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos inserir os dados em nosso prompt, garantindo que o agente tenha o melhor contexto possível, lembrando que, em soluções mais robustas, o ideal é que essa informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE E PERFIL:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE:
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Serviço de streaming,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

```

---

## Exemplo de Contexto Montado

O exemplo abaixo adapta os dados da base de conhecimento para apresentar as informações de forma simples, para que parte de sua estrutura possa ser visualizada.

```
Dados do Cliente:
- Nome: João Silva
- Saldo disponível: R$ 5.000

Últimas transações:
- 05/11: Salário - R$ 5000 - entrada
- 10/11: Supermercado - R$ 450 - saída
- 07/11: Streaming - R$ 55 - saída
...
```

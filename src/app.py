import pandas as pd
import requests
import streamlit as st
import json

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434"
MODELO = "gpt-oss"

# CARREGAR DADOS
perfil = json.load(open('../data/perfil_investidor.json', 'r'))
transacoes = pd.read_csv('transacoes.csv')

# CONTEXTO
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil: {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}
"""

# SYSTEM PROMPT
SYSTEM_PROMPT = """Você é o Dinei, um assistente financeiro inteligente.

OBJETIVO:
Ajudar a organizar as finanças dos cliente, as estruturando em tabelas simples e dinâmicas, além de oferecer orientações financeiras.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita, ofereça alternativas e pergunte ao usuário se ele pode colaborar com mais dados
4. Pergunte ao usuário se a tabela satisfaz suas demandas
5. Apenas ofereça ajuda com economias se o cliente pedir
"""

# CHAMAR OLLAMA
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# INTEFACE

st.title("Dinei, Seu Orientador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
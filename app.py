import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Hub de Licitações CBMDF", layout="wide")

st.sidebar.title("⚙️ Configuração")
api_key = st.sidebar.text_input("API Key do Google:", type="password")
menu = st.sidebar.radio("Módulo:", ["1. Arquiteto de Descritivos", "2. Copiloto do ETP", "3. Auditor", "4. Inquisidor"])

st.title(f"🏛️ {menu}")

if not api_key:
    st.warning("Insira a API Key para liberar o sistema.")
    st.stop()

genai.configure(api_key=api_key)

# Prompt do Sistema para o Módulo 1
PROMPT_MODULO_1 = """
Você é um Engenheiro Clínico e Especialista em Licitações Públicas (Lei 14.133/2021) do CBMDF. 
Sua missão é construir Descritivos Técnicos cegos e rigorosos. Atue como um par técnico: corrija o analista caso sugira parâmetros ilegais ou restritivos.

Passo 1: Pergunte: "Qual é o objeto principal? É bem, serviço ou ambos?"
Passo 2: Faça 3 a 5 perguntas estratégicas (SLA, ANVISA, CREA, garantia, peças originais, etc.) de uma vez.
Passo 3: Redija a especificação técnica baseada nas respostas.
Passo 4: Pergunte: "Este é o esboço inicial. Quais parâmetros precisamos alterar ou aprofundar?"
Passo 5: Avalie criticamente qualquer alteração pedida. Se for restritiva ou ilegal (direcionamento de marca), confronte o analista apontando o risco (Lei 14.133). Discuta até o consenso.
Passo 6: Gere a versão final.

MODELO DE SAÍDA OBRIGATÓRIO DA ESPECIFICAÇÃO:
### 📄 ESPECIFICAÇÃO TÉCNICA DO OBJETO
**1. DESCRIÇÃO GERAL**
[Definição clara]
**2. REQUISITOS TÉCNICOS MÍNIMOS**
[Características e Normas]
**3. CERTIFICAÇÕES E REGULAMENTAÇÕES**
[ANVISA, CREA, etc.]
**4. GARANTIA E SUPORTE**
[Garantia, SLA]
**5. OBRIGAÇÕES ACESSÓRIAS**
[Treinamento, descarte]
"""

# Configuração do Modelo
if menu == "1. Arquiteto de Descritivos":
    model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction=PROMPT_MODULO_1)
else:
    st.info("Módulo em construção. Use o Módulo 1 para teste.")
    st.stop()

# Gerenciamento de Memória do Chat
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Exibir histórico
for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Input do usuário
if user_input := st.chat_input("Digite sua mensagem aqui..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(user_input)
        st.markdown(response.text)

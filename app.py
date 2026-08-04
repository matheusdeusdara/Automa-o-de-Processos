import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Hub de Licitações", layout="wide")

# Barra lateral para navegação e API Key
st.sidebar.title("⚙️ Configurações")
api_key = st.sidebar.text_input("Insira sua API Key do Google:", type="password")

st.sidebar.markdown("---")
st.sidebar.title("Navegação")
menu = st.sidebar.radio("Selecione o Módulo:", 
                        ["1. Arquiteto de Descritivos", 
                         "2. Copiloto do ETP", 
                         "3. Auditor de Conformidade", 
                         "4. Auditoria Final (Inquisidor)"])

# Título principal da página
st.title(f"🏛️ {menu}")

# Lógica de bloqueio caso não tenha a chave
if not api_key:
    st.warning("⚠️ Por favor, insira sua API Key na barra lateral para ativar a Inteligência Artificial.")
else:
    # Aqui vamos conectar o motor do Google mais para frente
    genai.configure(api_key=api_key)
    
    st.success("✅ Motor de IA conectado com sucesso!")
    st.info("A interface está pronta. No próximo passo, vamos injetar os Super Prompts aqui dentro!")

import streamlit as st
header = 'Report Elenko'
st.title(f'{header}')



import glob as glob
import pandas as pd
####################################### ANÁLISE DE MERCADO
arquivos = glob.glob('*.jpg')
arquivos = sorted(arquivos)

lista_nomes = []
for arquivo in arquivos:
  nome = (arquivo.split('_')[0])
  lista_nomes.append(nome)

jogadores = list(pd.DataFrame(lista_nomes)[0].unique())

dic_imagens = {}
for nome in jogadores:
  nome_jogador = nome
  slides = glob.glob(f'{nome_jogador}*.jpg')
  slides = sorted(slides)
  dic_imagens.update({nome:slides})
pic = st.selectbox("Análises de Mercado", list(dic_imagens.keys()))
st.image(dic_imagens[pic], use_column_width=True)

#################################### Analíticos
arquivos = glob.glob('analise/*.jpg')
arquivos = sorted(arquivos)

lista_nomes = []
for arquivo in arquivos:
  nome = (arquivo.split('_')[0])
  lista_nomes.append(nome)

jogadores = list(pd.DataFrame(lista_nomes)[0].unique())

dic_imagens = {}
for nome in jogadores:
  nome_jogador = nome.split('/')[-1]
  slides = glob.glob(f'{analise/nome_jogador}*.jpg')
  slides = sorted(slides)
  dic_imagens.update({nome:slides})
pic = st.selectbox("Analíticos", list(dic_imagens.keys()))
st.image(dic_imagens[pic], use_column_width=True)

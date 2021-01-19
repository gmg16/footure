import streamlit as st
header = 'Report Elenko'
st.title(f'{header}')
####################################################


# import glob as glob
# import PIL
# from PIL import Image
# from PIL import Image, ImageDraw, ImageFilter
# from PIL import Image, ImageDraw, ImageFont
# from PIL import ImageOps
# from pdf2image import convert_from_path


# import pandas as pd
# arquivos = glob.glob('/content/*.jpg')
# lista_nomes = []
# for arquivo in arquivos:
#   nome = (arquivo.split('/')[2].split('_')[0])
#   lista_nomes.append(nome)

# jogadores = list(pd.DataFrame(lista_nomes)[0].unique())

# dic_imagens = {}
# for nome in jogadores:
#   nome_jogador = nome
#   slides = glob.glob(f'/content/{nome_jogador}*.jpg')
#   slides = sorted(slides)
#   dic_imagens.update({nome:slides})
# pic = st.selectbox("Análises de Mercado", list(dic_imagens.keys()))
# st.image(dic_imagens[pic], use_column_width=True)
########################################################

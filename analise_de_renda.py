import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.express as px

# Ler o DataFrame
df = pd.read_csv('./input/previsao_de_renda.csv')

# Configurações da página
st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="💸",
     layout="wide"
)

# Título da aplicação
st.title('Análise de Previsão de Renda')
total_linhas = str(len(df))
st.write('Total de observações: ',total_linhas)

sexo_options = ['Todos'] + list(df['sexo'].unique())
sexo = st.sidebar.selectbox('Sexo', sexo_options)
educacao_options = ['Todos'] + list(df['educacao'].unique())
educacao = st.sidebar.selectbox('Educação', educacao_options)
tipo_renda_options = ['Todos'] + list(df['tipo_renda'].unique())
tipo_renda = st.sidebar.selectbox('Tipo de Renda', tipo_renda_options)

# Filtros para idade, renda e tempo de emprego
idade_min = st.sidebar.number_input('Idade Mínima', min_value=int(df['idade'].min()))
idade_max = st.sidebar.number_input('Idade Máxima', min_value=int(df['idade'].min()), max_value=int(df['idade'].max()), value=int(df['idade'].max()))

renda_min = st.sidebar.number_input('Renda Mínima', min_value=float(df['renda'].min()))
renda_max = st.sidebar.number_input('Renda Máxima', min_value=float(df['renda'].min()), max_value=float(df['renda'].max()), value=float(df['renda'].max()))

tempo_emprego_min = st.sidebar.number_input('Tempo de Emprego Mínimo', min_value=float(df['tempo_emprego'].min()))
tempo_emprego_max = st.sidebar.number_input('Tempo de Emprego Máximo', min_value=float(df['tempo_emprego'].min()), 
                                            max_value=float(df['tempo_emprego'].max()), value=float(df['tempo_emprego'].max()))

# Aplicar filtros
filtered_df = df[
    ((df['sexo'] == sexo) if sexo != 'Todos' else True) &
    ((df['educacao'] == educacao) if educacao != 'Todos' else True) &
    (df['idade'] >= idade_min) &
    (df['idade'] <= idade_max) &
    (df['renda'] >= renda_min) &
    (df['renda'] <= renda_max) &
    (df['tempo_emprego'] >= tempo_emprego_min) &
    (df['tempo_emprego'] <= tempo_emprego_max)
]

# Gráficos comparativos
col1, col2 = st.columns(2)

fig_sex = px.pie(filtered_df, names='sexo', values='renda', title='Usuários por Sexo')
fig_sex.update_xaxes(title_text='')
fig_sex.update_yaxes(title_text='')
col1.plotly_chart(fig_sex)

fig_educacao = px.bar(filtered_df, x='educacao', y='renda', title='Renda por Nível Educacional', color = 'sexo')
fig_educacao.update_xaxes(title_text='')
fig_educacao.update_yaxes(title_text='')
col2.plotly_chart(fig_educacao)

fig_tipo_renda = px.bar(filtered_df, x='tipo_renda', y='renda', title='Renda por Tipo', color = 'sexo')
fig_tipo_renda.update_xaxes(title_text='')
fig_tipo_renda.update_yaxes(title_text='')
col1.plotly_chart(fig_tipo_renda)

fig_tempo_emprego = px.scatter(filtered_df, x='tempo_emprego', y='renda', title='Renda por Tempo de Emprego', color = 'sexo')
fig_tempo_emprego.update_xaxes(title_text='')
fig_tempo_emprego.update_yaxes(title_text='')
col2.plotly_chart(fig_tempo_emprego)

fig_estado_civil = px.bar(filtered_df, x='estado_civil', y='renda', title='Renda por Estado Civil', color = 'sexo')
fig_estado_civil.update_xaxes(title_text='')
fig_estado_civil.update_yaxes(title_text='')
col1.plotly_chart(fig_estado_civil)

fig_tipo_residencia = px.bar(filtered_df, x='tipo_residencia', y='renda', title='Renda por Tipo de Residência', color = 'sexo')
fig_tipo_residencia.update_xaxes(title_text='')
fig_tipo_residencia.update_yaxes(title_text='')
col2.plotly_chart(fig_tipo_residencia)

fig_qtd_filhos = px.bar(filtered_df, x='qtd_filhos', y='renda', title='Renda por Quantidade de Filhos', color = 'sexo')
fig_qtd_filhos.update_xaxes(title_text='')
fig_qtd_filhos.update_yaxes(title_text='')
col1.plotly_chart(fig_qtd_filhos)

fig_posse_veiculo = px.bar(filtered_df, x='posse_de_veiculo', y='renda', title='Renda por Posse de Bens - Veículo', color = 'sexo')
fig_posse_veiculo.update_xaxes(title_text='')
fig_posse_veiculo.update_yaxes(title_text='')
col2.plotly_chart(fig_posse_veiculo)

fig_posse_imovel = px.bar(filtered_df, x='posse_de_imovel', y='renda', title='Renda por Posse de Bens - Imóvel', color = 'sexo')
fig_posse_imovel.update_xaxes(title_text='')
fig_posse_imovel.update_yaxes(title_text='')
col1.plotly_chart(fig_posse_imovel)
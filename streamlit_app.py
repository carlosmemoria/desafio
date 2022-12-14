#Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split

condTrue = 'Não há ocorrência do evento que desejamos prever em '
condFalse = 'Existe ocorrência do evento que desejamos prever '
resposta = 'linhas'

st.set_page_config(layout="wide")
# Funções para cada uma das páginas
def home(uploaded_file):

    if uploaded_file:
        st.header('Comece a explorar os dados usando o menu à esquerda')
    else:
        st.header('Para começar, faça o upload de um arquivo')
	
	col1, col2, col3 = st.columns(3)

	with col1:
	    st.header("A cat")
	    st.image("https://static.streamlit.io/examples/cat.jpg")

	with col2:
	    st.header("A dog")
	    st.image("https://static.streamlit.io/examples/dog.jpg")

	with col3:
	    st.header("An owl")
	    st.image("https://static.streamlit.io/examples/owl.jpg")

def data_describe():
    st.header('Estatísticas do Dataframe')
    st.write(df.describe())
		
def data_header():
    st.header('Cabeçalho do Dataframe')
    st.write(df.head())
	
    n = df['target'].value_counts() [0]
    e = df['target'].value_counts() [1]
	
    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	

def bar_plot():

    st.header('Gráfico horizontal')
    fig = px.bar(x = [ df['target'].value_counts() [0], df['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    n = df['target'].value_counts() [0]
    e = df['target'].value_counts() [1]

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))

	
def bar_plot_select():
    df_sample = df.sample(n=200)	
    st.header('Seleção aleatória de 200 entradas do dataset')
    fig = px.bar(x = [ df_sample['target'].value_counts() [0], df_sample['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    n = df_sample['target'].value_counts() [0]
    e = df_sample['target'].value_counts() [1]

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	
	
def bar_plot_select_frac():
    df_sample = df.sample(frac=0.5)	
    st.header('Seleção aleatória de 50% das entradas do dataset')
    fig = px.bar(x = [ df_sample['target'].value_counts() [0], df_sample['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    n = df_sample['target'].value_counts() [0]
    e = df_sample['target'].value_counts() [1]

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	

    
 	
def bar_plot_scikit():
    X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis=1),
                                                    df['target'],
                                                    stratify=df['target'],
                                                    test_size=0.5)
    df_y = pd.DataFrame(y_test)	
    st.header('Utilização da função train_test_split da biblioteca scikit learn')
    
    n = df_y['target'].value_counts() [0]
    e = df_y['target'].value_counts() [1]
	
    fig = px.bar(x = [ df_y['target'].value_counts() [0], df_y['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	
	
# Título e texto de introdução
st.title('Projeto de exploração de dados')
st.text('Este é um aplicativo web permite a exploração de dados em vários formatos de gráficos')

# Configuração da barra lateral
st.sidebar.title('Barra lateral')
upload_file = 'https://drive.google.com/u/0/uc?id=1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt&export=download'
#Navegação na barra lateral
st.sidebar.title('Navegação')
options = st.sidebar.radio('Selecione o que deseja exibir:', ['Home', 'Resumo de Dados', 'Cabeçalho de dados', 'Gráfico de barras horizontal', 
							      'Seleção aleatória de 200 entradas do dataset', 
							      'Seleção aleatória de 50% das entradas do dataset',
							      'Scikit Learn'])

# Verifica se o arquivo foi carregado
if upload_file is not None:
    df = pd.read_parquet(upload_file)

# Opções de navegação
if options == 'Home':
    home(upload_file)
elif options == 'Resumo de Dados':
    data_describe()
elif options == 'Cabeçalho de dados':
    data_header()
elif options == 'Gráfico de barras horizontal':	
	bar_plot()
elif options == 'Seleção aleatória de 200 entradas do dataset':
    bar_plot_select()
elif options == 'Seleção aleatória de 50% das entradas do dataset':
    bar_plot_select_frac()
elif options == 'Scikit Learn':
    bar_plot_scikit()

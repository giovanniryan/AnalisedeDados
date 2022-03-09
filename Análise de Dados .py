#!/usr/bin/env python
# coding: utf-8

# !pip install pandas
# !pip install plotly.express

#  <h2> Passo 1 - Inserção de tabela </h2>

# In[5]:


import pandas as pd 
# importar base de dados para o python (jupyter)
tabela = pd.read_csv(r"C:\Users\giova\OneDrive\Área de Trabalho\Aula 2 - Telecom\telecom_users.csv")

# entender os problemas da tabela
tabela = tabela.drop("Unnamed: 0", axis=1)
# analisar a tabela
display(tabela)


# <h2> Passo 2 - Tratamento de dados </h2>

# In[15]:


# analisar se o python lê corretamente os dados informados (numero como numeros e textos como textos)
print(tabela.info())

# mudar caracteristica de "total gasto" para númerico (pd.to_numeric)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# analisar se há alguma coluna vazia
tabela = tabela.dropna(how = "all", axis=1)

# analisar se há alguma linha vazia
tabela = tabela.dropna(how = "any", axis=0)


# <h2> Parte 3 - Análise Global
#     

# In[20]:


# analisar quantos clientes cancelaram e continuaram com a assinatura
print(tabela["Churn"].value_counts())
# % dos clients
print(tabela["Churn"].value_counts(normalize="True").map('{:.1%}'.format))


# <h2> Parte 4 - Análise Detalhada (Uso de gráficos) </h2>
# 

# In[23]:


# criar o gráfico
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show() # exibir gráfico 
    


# <h2> Bônus </h2>
# <br> <h4> caso queira usar apenas uma tabela:  </h4>

# In[31]:



grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn") 
grafico.show() # exibir gráfico 


# In[ ]:





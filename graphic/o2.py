import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo: anos e valores de temperatura
data = {
    "Year": [1999, 2000, 2001, 2002, 2003, 2004, 
             2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 
             2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Global Temperature Increase (°C)": [0.38, 0.39, 0.53, 0.63, 0.62, 0.53, 
                                         0.68, 0.64, 0.66, 0.54, 0.65, 0.72, 
                                         0.61, 0.64, 0.67, 0.75, 0.90, 1.01, 
                                         0.92, 0.85, 0.98, 1.01, 0.85, 0.89, 1.17]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Gerar gráfico
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Global Temperature Increase (°C)"], marker='o', color='r', label='Global Temperature Increase')
plt.title('Global Temperature Increase (Last 25 Years)')
plt.xlabel('Year')
plt.ylabel('Temperature Increase (°C)')
plt.xticks(df["Year"], rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()

# Exibir o gráfico
plt.show()

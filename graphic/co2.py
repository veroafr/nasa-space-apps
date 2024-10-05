import pandas as pd
import matplotlib.pyplot as plt

# Sample data: years and CO₂ values must have the same length
data = {
    "Year": [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 
             2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
             2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "CO₂ (ppm)": [370.8, 372.8, 374.0, 375.2, 376.7, 377.8, 
                   379.2, 380.5, 382.1, 385.1, 386.5, 389.9, 
                   393.0, 395.2, 396.7, 398.1, 400.0, 403.4, 
                   405.0, 408.5, 410.0, 412.5, 414.1, 415.8, 416.4]  # add a value for 2023
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate graph
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["CO₂ (ppm)"], marker='o', color='b', label='CO₂ Concentration')
plt.title('Atmospheric CO₂ Concentration (Last 25 Years)')
plt.xlabel('Year')
plt.ylabel('CO₂ (ppm)')
plt.xticks(df["Year"], rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

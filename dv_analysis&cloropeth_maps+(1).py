
# coding: utf-8

# In[1]:

import pandas as pd 
import numpy as np 
df_DS = pd.read_csv("https://cocl.us/datascience_survey_data", index_col = 0)
df_DS #read the csv file and export in a DataFrame
      #the file includes results of a survey in the most interesting topics of Data Science


# In[2]:

df_DS.sort_values(['Very interested'], axis = 0,ascending = False, inplace = True)
df_DS #sort values by the attribure Very Interested 


# In[3]:

df_DS.sum(axis =1) # there are people that have replied N/A


# In[4]:

df_DS_percent = df_DS.apply(lambda x: round(x/2233 * 100, 2))
df_DS_percent #scale to the percentage


# In[5]:

ax = df_DS_percent.plot(kind = "bar",
                        figsize = (20,8),
                        color = ['#5cb85c', '#5bc0de', '#d9534f'],
                        width = 0.8
                        )
ax.legend(fontsize = 14)
ax.set_xticklabels(labels = df_DS_percent.index ,fontsize = 14)
#ax.set_yticklabels(labels = np.linspace(0,70,8), fontsize = 14)
ax.axes.get_yaxis().set_ticks([])
ax.set_title("Percentage of Respondents' interest in Data Science Areas", fontsize = 16)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

for i in ax.patches:

    y=i.get_height()

    x=i.get_x()+i.get_width()/2

    label = "{:.2%}".format(y/100)

    ax.annotate(label, xy=(x,y+1), ha='center', fontsize = 14)

#visualize results in bars showing the values as labels on top of each bar


# In[6]:

df_crimeset = pd.read_csv("https://cocl.us/sanfran_crime_dataset")
df_crimeset.head()  #the file includes registration of crimes reported in different areas of San Fransisco


# In[ ]:

crimes_by_district = df_crimeset['PdDistrict'].value_counts().to_frame()
crimes_by_district = crimes_by_district.reset_index()
crimes_by_district.rename({'index': 'Neighborhood', 'PdDistrict': 'Count'}, axis =1,inplace = True )
crimes_by_district #gather values by each reported crime area in San Fransisco


# In[ ]:

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium


# In[27]:

get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson -O san_fransisco.json')


# In[32]:

crime_san_fransisco = r'san_fransisco.json'
san_fransisco_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)


# In[33]:

san_fransisco_map.choropleth(
    geo_data=crime_san_fransisco,
    data=crimes_by_district,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Fransisco'
)


san_fransisco_map #visualize crime frequency via a choropleth map


# In[ ]:




# In[ ]:




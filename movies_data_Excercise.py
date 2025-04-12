#  In this exercise i work on the movies_data.csv and analyise it and make some changes and save it 


import pandas as pd 
import plotly.express as px 


data = pd.read_csv(r'C:\Users\HP\Desktop\Languages\Python\Pandas\movies_data.csv')
print(data.head(5))

#  make a new column and apply some value 

data['year_classify'] = data.apply([lambda x:'before year' if x['release_year'] < 2000 else 'after_year'],axis = 1)
print(data)

# Save the file name final_movie_data.csv in the csv mode

data.to_csv('final_movie_data.csv',index=False)

#  Gives the all the Hollywood movie 

print(data[data['industry'] == 'Hollywood'].to_string())


# Filter the movies after the release year 2010

filtered_data = data[data['release_year'] >=2010]
print(filtered_data.to_string())


#  Sort the movies according to their imbd rating 

datanew = data.sort_values(by=['imdb_rating'],ascending=False)
print(datanew.to_string())
print(datanew['title'])  # sort the values by imdb_rating and returns the title of the movie

# check the movies is made in how many language 

print(data['language'].unique())



#  Plot the graph between imdb_rating and budget . Gives the relation between the imdb_Rating and the their budget

figure = px.bar(data,x='imdb_rating',y='budget',title='Graph between the imdb_rating and budget')
figure.show()


#  Make a new column of the profit 

data['profit'] = data.apply(lambda x: x['revenue'] - x['budget'],axis = 1)
print(data.to_string())


data.to_csv('new_movies_data.csv')


#  Group by concept is used in it 

g = data.groupby('industry')
for key,data in g:
    print("Key",key)
    print("Data",data.to_string())
print(g.size())



print(g.get_group('Bollywood'))


#  Grouping the values by the custom method 


def grouper(data,idx,col):
    value = data[col].loc[idx]
    if 1 <= value <=3.9:
        return 'poor'
    elif 4<= value <= 7.9:
        return 'average'
    elif 8<= value <= 10:
        return 'good'
    else:
        return 'others'
        
g = data.groupby(lambda idx: grouper(data,idx,'imdb_rating'))
for key,data in g:
    print('key',key)
    print('data',data.to_string())
    
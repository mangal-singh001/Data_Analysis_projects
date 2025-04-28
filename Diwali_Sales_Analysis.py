import pandas as pd   
import matplotlib.pyplot as plt  
import seaborn as sns    

df = pd.read_csv(r'C:\Users\HP\Desktop\Languages\Python\Data_Analysis_projects\Diwali Sales Data.csv',encoding='ISO-8859-1')
print(df)  # return data of the file 
print(df.info())   # retun the information of the file 
print(df.head(5).to_string())  # Returns the top 5 row 
print(df.shape)   # return the shape of the file how many rows and column 
print(df.describe()) # return the statistical information like mean, count ,std etc 


print(df.isnull().sum())   # check the any null value in the column 
df.drop(['Status','unnamed1'],axis=1,inplace=True)  # Drop the entire column 
df.dropna(inplace=True)   # drop a row if any value is null
df['Amount'] = df['Amount'].astype('int')  # set the int datatype
print(df['Amount'].dtypes)
print(df.info())
print(df['Amount'].isnull().sum())
print(df[['Age','Orders','Amount']].describe())  
print(df['State'].unique())


#  Convert the data 0 or 1 in Marital_Status to yes or no 

def conv(val):
    if val == 0:
        return 'No'
    else:
        return 'Yes'
    
df['Marital_Status'] = df['Marital_Status'].apply(conv)
print(df['Marital_Status'])


# By this graph we know that we have more female customer than man 

ax = sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

ax = sns.countplot(x='Gender',data=df,hue='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# returns the how many people is married or not 


ax = sns.countplot(x='Marital_Status',data=df)
ax.bar_label(ax.containers[0])
plt.title("Graph shows that the how many customer is married")
plt.show()


# Rename the column Marital_Status to Shaddi


print(df.columns)

print(df.rename(columns = {'Marital_Status':'Shaddi'}).columns)



# plotting a bar chart for gender vs total amount
# in it i m plotting large numbers, but Matplotlib is automatically the y-axis to scientific notation (e.g., 1e7), and the ticks are in millions 



sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
plt.show()
print(sales_gen)


# this graph shows us the which age group has the most female or male is the customer 


ax = sns.countplot(x='Age Group',data=df,hue='Gender')
for bar in ax.containers:
    ax.bar_label(bar)
plt.show()



# Plot the draph between the total Amount vs Age group 
# From this graph we can see that most of the buyers are of age group between 26-35 yrs female 


sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_age)
plt.show()


# Total number of orders from top 10 states 
#  Most of the order is from the Uttar Pradesh 

sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Orders',data=sales_state)
plt.show()


#  Total amount vs state from top 10 states 
# From the below graph we can see that most of the orders & Total sales/amount are from Uttar pradesh, Maharastra and Kranataka respectively


sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Amount',data=df)
plt.show()


# total amount vs marital_Status and further divided in male or female 
# from the below graph we can see that most of the buyers are married(women)  and they have high purchasing power 



sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
plt.show()


#  Anaysis based on the occupation

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x='Occupation',data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# From the below graph we can see that most of the buyers are working in IT,Healthcare 

sales_occupation = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Occupation',y='Amount',data=df)
plt.show()




# Analysis based on the Product Category

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x='Product_Category',data=df)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45,ha='right')
for bars in ax.containers:
    ax.bar_label(bars)
plt.tight_layout()   # adjusts spacing so nothing is cut off
plt.show()


# From the Below graphs we can see that most of the sold products are from Food,Clothing and Electronics category 

sns.set(rc={'figure.figsize':(20,5)})
sales_Product = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
ax = sns.barplot(x='Product_Category',y='Amount',data=sales_Product)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45,ha='right')

plt.tight_layout()
plt.show()
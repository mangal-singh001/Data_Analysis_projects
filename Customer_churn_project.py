import numpy as np   
import pandas as pd   
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv(r'C:\Users\HP\Desktop\Languages\Python\Data_Analysis_projects\Customer Churn.csv')
print(df.info())
print(df.head()) 


#  Blank spaces in TotalCharges is replaces by the 0 

df['TotalCharges'] = df['TotalCharges'].replace(' ','0')
df['TotalCharges'] = df['TotalCharges'].astype("float")
print(df.info())


#  Checks the any null value is present in the csv file 


df1 = df.isnull().sum().sum()
print(df1)

#  Provides statistical summary of the colmns of the file 

print(df.describe().to_string())

#  checks any dupicate value in the csv file 

print(df.duplicated().sum())
print(df['customerID'].duplicated().sum())


#  convert 0 and 1 values of senior citizen to yes/no to make it easier to understand

def conv(val):
    if val == 1:
        return "Yes"
    else:
        return "No"
    
df['SeniorCitizen'] = df['SeniorCitizen'].apply(conv)
print(df['SeniorCitizen'])


#  Gives the number of customer is churn out 

ax = sns.countplot(x='Churn',data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of customer by Churn")
plt.show()


#  Now checks the what's the percentage of people to be churn out  in the form of percentage by using the piew chart

plt.figure(figsize=(3,4))
gb = df.groupby("Churn").agg({'Churn':"count"})
print(gb)
plt.pie(gb['Churn'],labels=gb.index,autopct="%1.2f%%")
plt.title("Percentage of Churn Customer",fontsize=10)
plt.show()

#  From the given pie chart we can conclude that 26.45% of our customer have Churned out 
#  Now let's explore the reason behind it .

# hue = on the basis of Churn is further classify the gender
 

plt.figure(figsize=(4,4))
ax = sns.countplot(x='gender',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title("Churn by Gender")
plt.show() 


# Analysis the file based on the senior citizen 

plt.figure(figsize=(4,4))
sns.countplot(x='SeniorCitizen',data=df,hue='Churn')
plt.title("Churn by SeniorCitizen")
plt.show()   


# Gives the percentage of SeniorCitizen to be Churn out or not by Stacked bar chart 


total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# #  Plot
fig, ax = plt.subplots(figsize=(4,4))

# #  plot the bars 

total_counts.plot(kind='bar',stacked=True,ax=ax, color=['#1f77b4','#ff7f0e'])  # customize colors if desired 

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x,y = p.get_xy()
    ax.text(x + width / 2, y + height / 2,f'{height:.1f}%',ha='center',va='center')
  
  
plt.title('Churn by SeniorCitizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn',bbox_to_anchor=(0.9,0.9))  # Customize legend location 
plt.show()


# Comparative a greater percentage of people in senior citizen category have churned 



#  Analysis of the file based on the tenure to be churned out 

# people who have used our services for a long time have atayed and people who have used our servies for 1 or 2 months have Churned 

plt.figure(figsize=(9,4))
sns.histplot(x='tenure',data=df,bins=72,hue='Churn')
plt.show()


#  Based on the Contract



plt.figure(figsize=(5,5))
ax = sns.countplot(x='Contract',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title("Count of customer by Contract")
plt.show()

#  people who have month to month contract are likely to churn then from the one year 


print(df.columns.values)



columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()



# The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.





plt.figure(figsize=(6,5))
ax = sns.countplot(x='PaymentMethod',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title("Count of customers PAyment Method")
plt.xticks(rotation = 45)
plt.show()



# customer is likely to churn when he is using electronic check as a payment method.  
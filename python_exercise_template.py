# import pandas, numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from collections import Counter
from tigerml.eda import Analyser

# Create the required data frames by reading in the files
df=pd.read_excel('SaleData.xlsx')
df1=pd.read_csv("imdb.csv",escapechar='\\')
df2=pd.read_csv('diamonds.csv')
df3=pd.read_csv('movie_metadata.csv')


# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
    ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region   
def sales_year_region(df):   
    # write code to return pandas dataframe
    df['yr'] = df.OrderDate.apply(lambda x: x.strftime('%Y'))
    syr = df.groupby(['yr','Region'])["Sale_amt"].sum().reset_index()
    return syr

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    curr_time = pd.to_datetime("now")
    def day_left(x):
        t=str(x)
        return t[0:3]
    
    df['days_difference'] = curr_time - df['OrderDate']
    df['days_diff']=df['days_difference'].apply(day_left)
    df=df.drop(['days_difference'],axis=1)
    return df  

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
    x=df.groupby(['Manager'])['SalesMan'].unique().reset_index()
    return x

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    s=df.groupby('Region')['Units'].sum().reset_index()
    r=df.groupby('Region')['SalesMan'].nunique().reset_index()
    new_df=pd.merge(r,s,how='inner',on='Region')
    new_df.rename(columns={'SalesMan':'salesmen_count','Units' : 'total_sales'}, inplace=True)
    return new_df


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    b=df.groupby('Manager')['Sale_amt'].sum().reset_index()
    total_1=b['Sale_amt'].sum()
    b['percent_sales ']=(b['Sale_amt']/total_1)*100
    b=b.drop(['Sale_amt'],axis=1)
    return b
    

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
    p=df.iloc[4]['imdbRating']
    return p

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here
    l=[]
    mydict={}
    short = df[df['duration']==df['duration'].min()]['title'].reset_index().iloc[0][1]
    long = df[df['duration']==df['duration'].max()]['title'].reset_index().iloc[0][1]
    #l['shortest_run_time_movie_name']=short
    #l['longest_run_time_movie_name']=long
    l.append(short)
    l.append(long)
    movie=['shortest_run_time_movie_name','longest_run_time_movie_name']
    mydict['movie']=movie
    mydict['name']=l
    res=pd.DataFrame(mydict)
    
    return res

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here
    '''
    a=df.groupby(['year','imdbRating'])['title'].unique().reset_index()
    a['title']=a['title'].apply(lambda x: x[0])
    b=df.drop(['imdbRating','year'],axis=1)
    new_df=pd.merge(a,b,how='inner',on='title')
    return new_df
    '''
    ls=df.sort_values(['year','imdbRating'],ascending=[True,False])
    return ls
    
# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
    
	# write code here
    result_1 = df[(df['gross'] > 20000000) & (df['budget'] < 10000000) & (df['duration'] >= 30) & (df['duration'] <= 180)]
    #result = df[(df['duration'] >= 30) & (df['duration'] <= 180)]
    return result_1

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
    result=len(df)-len(df.drop_duplicates())
    return result

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
    df = df[pd.notnull(df['carat']) & pd.notnull(df['cut'])]
    return df
    
# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here 
    t=df._get_numeric_data()
    return t

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
    df['x'].fillna((df['x'].mean()), inplace=True)
    df['y'].fillna((df['y'].mean()), inplace=True)
    df["z"].fillna(method ='ffill', inplace = True)
    for i,j in enumerate(df['z']):
        if j=='None':
            df['z'][i]='1'
            
    df['z']=df['z'].apply(lambda x: float(x))
    
    for i,j in enumerate(df['depth']):    
        if (df['depth'][i]>60):
            df['volume']=df['x']*df['y']*df['z']
        else:
            df['volume']=8
    
    return df
    

# Q15 impute missing price values with mean
def impute(df):
	# write code here
    df['price'].fillna((df['price'].mean()), inplace=True)
    return df



    


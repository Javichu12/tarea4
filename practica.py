# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:40:18 2022

@author: javie
"""
#arrays:

import pandas as pd
import numpy as np
import sys










#readtable

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_table('D:/DAM1/Programacion/practicaexamenrecuperacion/movies.dat', engine='python', sep='::', header=None, names=movieHeader, encoding='latin1')


print('---------------------: \n%s' %movies)

ratings=pd.read_table('D:/DAM1/Programacion/practicaexamenrecuperacion/ratings.dat', engine='python', sep='::', header=None, names=('user_id', 'movie_id', 'rating', 'timestamp'))


users=pd.read_table('D:/DAM1/Programacion/practicaexamenrecuperacion/users.dat', engine='python', sep='::', header=None, names=('user_id', 'gender', 'age', 'ocupation', 'zip'))





mergeRatingsmovies= pd.merge(movies,ratings)
userRatingsMoviesDF= pd.merge(users,mergeRatingsmovies)

  
    uno = userRatingsMoviesDF.copy()
    uno = uno.pivot_table(index=['movie_id','title'],
                        values=['rating'],
                        columns=['gender'],  
                        aggfunc=[np.mean],
                        fill_value=-1,
                        margins=True)

    uno_query=uno.query("movie_id ==260 | movie_id ==1196 | movie_id ==1210 | movie_id ==2628")

  
    uno_query.to_csv('C:/ExamenRecuperacion/Ejercicio1_JavierPerezMaeso.csv',sep=';')



    df_2 = userRatingsMoviesDF.copy()

    df_2 = df_2.pivot_table(index=['movie_id','title'],
                        values=['rating'],
                        aggfunc=[np.mean],                        
                        fill_value=-1,
                        margins=True)


    df_sort=df_2.sort_values(by='title',ascending=False) 

    df_sort.to_csv('C:/ExamenRecuperacion/Ejercicio2_JavierPerezMaeso.csv',sep=';')



    df_3 = userRatingsMoviesDF.copy()
    df_3 = df_3.pivot_table(index=['genders'],
                        values=['age'],                      
                        fill_value=-1 )

    df_terror=df_3.query("genders=='Horror'")
    df_terror.to_csv('C:/ExamenRecuperacion/Ejercicio3_JavierPerezMaeso.csv',sep=';')

                        


    df_4 = userRatingsMoviesDF.copy()

    df_4['rating']=df_4['rating']*2

    df_4.to_csv('C:/ExamenRecuperacion/Ejercicio4_JavierPerezMaeso.csv',sep=';')
    
    
if operacion==5:
    sys.exit()

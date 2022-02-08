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



    dos= userRatingsMoviesDF.copy()

    dos= dos.pivot_table(index=['movie_id','title'],
                        values=['rating'],
                        aggfunc=[np.mean],                        
                        fill_value=-1,
                        margins=True)


    dos=dos.sort_values(by='title',ascending=False) 

    dos.to_csv('C:/ExamenRecuperacion/Ejercicio2_JavierPerezMaeso.csv',sep=';')



    ejercicio3 = userRatingsMoviesDF.copy()
    ejercicio3= ejercicio3.pivot_table(index=['genders'],
                        values=['age'],                      
                        fill_value=-1 )

    ejercicio3=ejercicio3.query("genders=='Horror'")
    ejercicio3.to_csv('C:/ExamenRecuperacion/Ejercicio3_JavierPerezMaeso.csv',sep=';')

                        


    ejercicio4= userRatingsMoviesDF.copy()

    ejercicio4['rating']=ejercicio4['rating']*2

    ejercicio4.to_csv('C:/ExamenRecuperacion/Ejercicio4_JavierPerezMaeso.csv',sep=';')
    
    



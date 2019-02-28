# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:11:17 2019

@author: f556085
"""

import datetime
from pydal import DAL, Field

def model():
    dbinfo = 'sqlite://storage.sqlite'
    folder = "./database"
    
    db = DAL(dbinfo, folder=folder, pool_size=1)
    table(db)
    return db

def table(db):
    
    db.define_table("user",
                Field("name", 'string'),
                Field("email", 'string'),
                Field('password', 'password')
                )
    
    db.define_table("genero",
                    Field("nome", 'string')
                    )
    
    db.define_table("musica",
                    Field("nome", 'string'),
                    Field('cantor', 'string'),
                    Field('album', 'string'),
                    Field('arquivo', 'string'),
                    Field('tempo', 'string'),
                    Field('genero', 'list:reference estilos'),
                    )
    
    db.define_table("preferidas",
                    Field("musica", 'reference musica'),
                    Field("user", 'reference user')
                    )
    
    
      
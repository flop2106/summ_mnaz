#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:38:16 2020

@author: flop2106

To Do:
    
1) Embed Lazada vs shopee scraper 
2) show result of lazada vs shopee in 2 table
3) Create html template with css - - to include waiting for result in the html
"""

from flask import Flask, render_template, redirect, url_for, request, flash
import webscraping_v2_urllib_flask as web
import timeit
import time
from threading import Thread

app = Flask(__name__)


titlelist=[]
hreflist=[]
summarize=[]
keywords=[]
lenghtsummarize=[]
lists=[]
summ_r=[]
global update


def webscrapper():
    x="y"
    while (x=="y"):
        global titlelist
        global hreflist
        global summarize
        global keywords
        global lenghtsummarize
        global lists
        global summ_r
        titlelist,hreflist,summarize,keywords,lenghtsummarize,lists,summ_r=web.main()

        time.sleep(3600)

@app.route("/")
def home(): 
    #titlelist,hreflist,summarize,keywords,lenghtsummarize,lists=web.main()
    
    return render_template("home.html",lenlist=len(titlelist),titlel=titlelist, href=hreflist, summarize=summarize, key=keywords,lenghtsumm=lenghtsummarize,lists=lists,summ_r=summ_r)



#@app.route('/result',methods=['POST','GET'])
#def result():
    #if request.method == "POST":
        
        #searchinput = request.form["searchinput"]
        #find ways to add ads while waiting
        #if searchinput!="":    
        #flash('LOADING.....','load')
        #render_template("loading.html")
        #titlelazada,pricelazada,loclazada,titleshopee,priceshopee,locshopee=ls.main(searchinput) 
        #titlelazada=['1''2'];pricelazada=['1''2'];loclazada=['1''2']

        #return render_template("result.html", titlel=titlelazada,pricel=pricelazada,locl=loclazada, lenl=len(titlelazada))

    
    
    

if __name__ == "__main__":
    #app.secret_key="Super Secret"
    Thread(target=webscrapper).start()
    app.run(debug=True) 
    

         




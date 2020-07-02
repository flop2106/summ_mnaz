from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer 
from googlesearch import search
import time
import timeit
from selenium.webdriver.chrome.options import Options
import urllib3
import requests

lemmatizer=WordNetLemmatizer()
stop_words=set(stopwords.words('english'))
CHROME_PATH = '/usr/bin/google-chrome'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH
def get_wordnet_pos(word):
    #Map POS tag to first character lemmatize() accepts
    tag=nltk.pos_tag([word])[0][1][0].upper()
    tag_dict={"J":wordnet.ADJ,
              "N":wordnet.NOUN,
              "V":wordnet.VERB,
              "R":wordnet.ADV}
    return tag_dict.get(tag,wordnet.NOUN)
def extraction_news(hreflist,titlelist):
    article=hreflist.copy()
    listsa=hreflist.copy()
    for h in hreflist:
        
        #article.append(h)
        #article.append(titlelist[hreflist.index(h)])
        #driver = webdriver.Chrome(executable_path='/home/flop2106/Downloads/usr/lib/chromium-browser/chromedriver',options=chrome_options)
        #driver = webdriver.Chrome(executable_path='/home/flop2106/Downloads/usr/lib/chromium-browser/chromedriver')
        try:
            #driver.get(h)
            
            driver=requests.get(h)
        except:
            lists=[]
            continue
        print("\nArticles Number: "+str(hreflist.index(h)+1))
        print('\nOpening '+str(h))
        time.sleep(2)
        
        #content = driver.page_source
        
        soup = BeautifulSoup(driver.content,features="lxml")

        body=soup.find('body')
        textlist=[]
        
        url=[]
        lists=[]
        for i in range(1,5):
            
                try:    
                    for header in body.find_all('h'+str(i)):
                        header1=header.text.strip().split(" ")
                        if re.match("(^[0-9])",header1[0]) and header1[0].endswith("."):
                            
                            lists.append(header.text.strip())
                except:
                    
                    pass
            #try:
            
            
            
            
        try:
            texts=body.find_all('p')
            
            for text in texts:
                if text.find('href')!=None or text.find('a')!=None or text.find('em')!=None or text.find('u'):
                    pass
                else:
                    textlist.append(text.text)
        except:
            pass
        article[hreflist.index(h)]=textlist
        listsa[hreflist.index(h)]=lists
        hreflist[hreflist.index(h)]=driver.url
        
        #driver.close()
                
    return article,listsa
def chromenews(search,articledec, articleno,typeoftext):
    #driver = webdriver.Chrome(executable_path='/home/flop2106/Downloads/usr/lib/chromium-browser/chromedriver',options=chrome_options)
    
    
    if typeoftext=="S" or typeoftext=="s":
        driver=requests.get('https://news.google.com/search?q='+search+'&hl=en-MY&gl=MY&ceid=MY%3Aen')
        #driver.get()
    else:
        #driver.get('https://news.google.com/topstories?hl=en-MY&gl=MY&ceid=MY:en')
        driver=requests.get('https://news.google.com/topstories?hl=en-MY&gl=MY&ceid=MY:en')
    #content = driver.page_source
    soup = BeautifulSoup(driver.content,features="lxml")
    
    #name=soup.findall('a', attrs={'href':'World'})
    #hrefworld=name.get('href')
    hreflist=[]
    titlelist=[]
    #get 100 of google news
    for a in soup.findAll('article'):
            #websites=a
            #print(a)
            name=a.find('a', attrs={'class':'DY5T1d'})
            hrefdata=name.get('href')
            hreflist.append(hrefdata)
            title=name.text
            titlelist.append(title)
    #driver.quit()
    for i in range(len(titlelist)):
        hreflist[i]="https://news.google.com"+hreflist[i][1:]
    
    if articledec=="S":
        return  titlelist[:articleno],hreflist[:articleno]
    else:
        return titlelist,hreflist

def google():
    query=input("Search : ")
    numinput=int(input("How many result? : "))
    
    href=[]
    #for j in search(query, tld="com", num=100, stop=None, pause=2):
    for j in search(query, num=numinput, stop=numinput, pause=2):
        href.append(j)
    return (href,query)
def searchdata(wordlist,wordtocheck):
    result="N"
    for words in wordlist:
        if re.match(r'\b'+words+r'\b',wordtocheck):
            result="Y"
            
            break
    return(result)
# Get all data from web.
def extraction(hreflist):
    article=[]
    from selenium.webdriver.chrome.options import Options
    CHROME_PATH = '/usr/bin/google-chrome'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    for h in hreflist:
        article.append(h)
        #driver = webdriver.Chrome(executable_path='/home/flop2106/Downloads/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
        result='n'
        print('\nOpening '+str(h))
        try:
            driver=requests.get(h)
            #driver.get(h)
            result='y'
        except:
            pass
        if result=='y':
            #content = driver.page_source
            soup = BeautifulSoup(driver.content,features="lxml")
        
            for a in soup.findAll('p'):
                #print(a)
                article.append(a.text)
        #driver.quit()
    return article    

# apend all the words from same website
def articlcompilation(article):
    article_compilation=[]
    for i in range(len(article)):
        a=article[i].split(":")
        
        if a[0]=="https" or a[0]=="http":
            #print('yes')
            article_compilation.append(article[i])
            article_compilation.append(str(""))
            pass
        else:
            #textappend=textappend+' '+article[i]d
            #article_compilation.append(article[i])
            #ac=article_compilation[-1].split(":")
            #if ac[0]=="https" or a[0]=="http":
            #    article_compilation.append(article[i])
            #    pass
            #else:
            article_compilation[-1]=str(article_compilation[-1])+" "+str(article[i])
    return article_compilation
# Calculate percentage for words in each article.
def wordcalculation(article_compilation):
    
    combination=[]
    combinationword=[]
    combinationcount=[]
    combinationpercentage=[]

    
    for articles in article_compilation:
        wordrev=[]
        wordcount=[]
        percentage=[]
        a=articles.split(":")
        if a[0]=="https" or a[0]=="http":
            combination.append(articles)
            combinationword.append(articles)
            combinationcount.append(articles)
            combinationpercentage.append(articles)
        
            continue
        
        else:
            articles=re.sub(r"[^a-zA-Z0-9]+", ' ', articles)
            sentence=articles.split(' ')
            for words in sentence:
                words=words.lower()
                if words=="":
                    pass
                elif words.isnumeric():
                    pass
                elif words in stop_words:
                    
                    pass
                #elif words in query.split(' '):
                #    pass
                elif len(words)<3:
                    pass
                elif len(wordrev)>0:
                    words=lemmatizer.lemmatize(words,get_wordnet_pos(words))
                    resultsearch=searchdata(wordrev,words)
                    if resultsearch=='Y':
                        wordcount[wordrev.index(words)]=wordcount[wordrev.index(words)]+1
                        pass
                    else:
                        wordrev.append(words)
                        wordcount.append(1)
                        pass
                else:
                   words=lemmatizer.lemmatize(words,get_wordnet_pos(words))
                   wordrev.append(words)
                   wordcount.append(1)
                   pass
            
                   
            percentage=np.zeros(len(wordcount))
        
            for h in range(len(wordcount)):
                percentage[h]=wordcount[h]/(max(wordcount))
           
            combinationword.append(wordrev)
            combinationcount.append(wordcount)
            combinationpercentage.append(percentage)
        
        
    return combinationword,combinationcount,combinationpercentage,combination

    ##how to ensure calculation came from only one article, and put in a list.
def summaryresults(article_compilation,combinationword,combinationpercentage):
    summary=[]
    j=0
    for articles in article_compilation:
        #print(j)
        a=articles.split(":")
        if a[0]=="https" or a[0]=="http":
            summary.append(articles)
            j=j+1
            continue
        else:
            wordsfull=articles.split(" ")
            text=[]
            wordslist=combinationword[j]
            wordspercentage=combinationpercentage[j]
            threshold=np.average(wordspercentage)
            if str(threshold)=='nan':
                threshold=float(0.5)
            if threshold==1:
                threshold=float(0.5)
            
            top=sorted(wordspercentage,reverse=True)#Descending
            try:
                top10=top[10]
            except:
                top10=threshold
            print(str(j)+" Threshold: "+str(top10)) 
            for words in wordsfull:
                words=re.sub(r"[^a-zA-Z0-9]+"," ",words)
                if words!="":
                    words=lemmatizer.lemmatize(words,get_wordnet_pos(words))
                for i in range(len(wordslist)):
                       
                    if words==wordslist[i]:
                        try:
                            if wordspercentage[i]>top10:
                                text.append(words)
                        except:
                            pass
            text=list(dict.fromkeys(text))
            summary.append(text)
            j=j+1
    
    return summary

def summary(article_comp,combinationword,combinationpercentage,summarylenght):
    try:
        # convert article into paragraph    
        paragraph=article_comp.splitlines()
        ### Try to remove redundancy
        paragraph=list(dict.fromkeys(paragraph))
        ###
        paragraph=[x for x in paragraph if x]
        full_paragraph=[]
        for para in paragraph:
            if len(para.split(" "))>3:
                para=para.strip()
                full_paragraph.append(para)
                
        all_sentences=[]
        for full in full_paragraph:
            if all_sentences==[]:
                all_sentences=full
            else:
                all_sentences=all_sentences+'. '+full
    
        #print(all_sentences)
        presentences=all_sentences.split('. ')
        sentences=[]
        for sen in presentences:
            if ":" in sen or "/" in sen:
                pass
            elif sen!=" " and len(sen.split())>3:
                sen=sen.lstrip()
                sentences.append(sen)
        
        # remove punctuatons, numbers and special characters
        #sentences=sentences.replace('\n',"")
        #sentences=pd.Series(sentences).str.replace("\'s",'')
        #sentences=pd.Series(sentences).str.replace("\xa0","")
        clean_sentences=pd.Series(sentences).str.replace(r'\([^)]*\)',' ')
        clean_sentences=pd.Series(clean_sentences).str.replace('"'," ")
        clean_sentences=pd.Series(clean_sentences).str.replace(r"'s\b"," ")
        clean_sentences=pd.Series(clean_sentences).str.replace('[^a-zA-Z]',' ')
        
        # make alphabet lowercase
        clean_sentences=[s.lower() for s in clean_sentences]
        
        #remove stopwords
        def remove_stopwords(sen):
            sen_new=" ".join([i for i in sen if i not in stop_words])
            return sen_new
        # remove stopwords from sentences
        clean_sentences=[remove_stopwords(r.split()) for r in clean_sentences]
        dictpercentage=dict()
        for j in range(len(combinationword)):
            dictpercentage[combinationword[j]]=combinationpercentage[j]
        
        sentencespercentage_comb=[]
        for cs in clean_sentences:
            sentencepercentage=0
            cs=cs.split(' ')
            for w in cs:
                
                for j in range(len(combinationword)):
                    if w==combinationword[j]:
                        
                        sentencepercentage=sentencepercentage+ dictpercentage[w]
            
            
            if len(cs)>0:
                #print(len(cs))
                #print(sentencepercentage)
                sentencespercentage_comb.append(sentencepercentage/len(cs))
                #print('%: '+str(sentencepercentage/len(cs)))
            else:
                sentencespercentage_comb.append(0)
        #print(sentencespercentage_comb)
        top=sorted(sentencespercentage_comb,reverse=True)
        
        try:
            topsorted=top[summarylenght]
        except:
            topsorted=top[int(len(top)/2)]
        summarize=str()
        summarize_clean=str()
        countsentences=0
        sentences_results=[]
        for i in range(len(sentencespercentage_comb)):
            if sentencespercentage_comb[i]>=topsorted: 
                summarize=summarize+sentences[i]+". "
                sentences_results.append(sentences[i])
                summarize_clean=summarize_clean+clean_sentences[i]+". "
                countsentences=countsentences+1
        lenghtsummarize=(1-(countsentences/len(sentencespercentage_comb)))*100
        lenghtsummarize=format(lenghtsummarize, '.2f')
        
        keywords=[]
        sort_keyword=sorted(combinationpercentage,reverse=True)
        top_keyword=sort_keyword[5]
        #print("top_keyword: "+str(top_keyword))
        countkw=0
        for i in range(len(combinationword)):
            if combinationpercentage[i]>=top_keyword:
                keywords.append(combinationword[i])
                countkw=countkw+1
                if countkw==5:
                    break
            
        #print(summarize)
        #print(keywords)
        #print(lenghtsummarize)
            
        return summarize,keywords,lenghtsummarize,sentences_results    
    except:
        return [],[],[],[]

def main():
    
    googleornews="N"
    start = timeit.default_timer()
    if googleornews=='G' or googleornews=='g':
        summarylenght=int(input('Summarize Article into how many sentences?: '))
        hreflist,query=google()
    else:
        summarylenght=5
        typeoftext="T"
    if typeoftext=="S" or typeoftext=="s":
        searchnews=input("What do you want to search?: ")
        searchnews=searchnews.replace(" ","+")
    else:
        searchnews=None
    
    #### articledec="A"
    articledec="A"
    articleno=str()
    if articledec=="S" or articledec=="s":
        articleno=int(input("How many articles needed? : "))
        
    
    titlelist,hreflist= chromenews(searchnews,articledec, articleno,typeoftext)
    article,lists= extraction_news(hreflist,titlelist)
    



    article=extraction(hreflist)
    
    article_compilation=articlcompilation(article)    
    #query=searchnews   
    combinationword,combinationcount,combinationpercentage,combination=wordcalculation(article_compilation)
    keywords=summaryresults(article_compilation,combinationword,combinationpercentage)
    count=0
    summarize=[]
    summl=[]
    keywords=[]
    lenghtsummarize=[]
    for i in range(len(article_compilation)):
        a=article_compilation[i].split(":")
        if a[0]=="https" or a[0]=="http":
            #print(hreflist[i])
            continue
        elif article_compilation[i]!='':
            count=count+1
            summ,key,lsum,summ_r=summary(article_compilation[i],combinationword[i],combinationpercentage[i],summarylenght)
        else:
            summ=[]
            key=[]
            lsum=[]
            summ_r=[]
        summl.append(summ_r)
        summarize.append(summ)
        keywords.append(key)
        lenghtsummarize.append(lsum)
        print(' ')
        print('article number: '+str(count))
        try:
            print(titlelist[len(summarize)-1].upper())
            print(hreflist[len(summarize)-1])
        except:
            pass
            
        print('\n'+str(summarize[-1]))
        print('\nKeywords: \n'+ str(keywords[-1]))
        print('\nSummarized by: '+str(lenghtsummarize[-1]))
    stop = timeit.default_timer()
    seconds=stop-start
    seconds=seconds%(24*3600)
    hour=seconds//3600
    seconds %= 3600
    minutes=seconds//60
    seconds%=60
        
    print('\nTime: '+ '%d:%02d:%02d'%(hour,minutes,seconds))
            
    return titlelist,hreflist,summarize,keywords,lenghtsummarize,lists,summl        
            






#Find ways to summarize each, show also top 5 keywords.
#used below to further summarize the articles, remain only keywords. find average percentage for each article first

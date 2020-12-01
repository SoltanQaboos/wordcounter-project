from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            #increase
            worddic[word] += 1
        else:
            #add to the dictionary
            worddic[word] = 1

    sortdeword = sorted(worddic.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortdeword':sortdeword})

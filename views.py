from django.shortcuts import render
from django.http import HttpResponse
import operator


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'Help.html')

def lesson(request):
    return render(request, 'lessons.html')

def newsletter(request):
    return render(request, 'Newsletter.html')

def calendar(request):
    return render(request, 'Calendar1.html')

def test(request):
    return render(request, 'test.html')

def count(request):
    fulltext = request.GET['name']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=False)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})

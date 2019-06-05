from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    # return HttpResponse("hello 111111111 ")
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext, "\t", fulltext, "\t", type(fulltext))
    wordlist = fulltext.split()
    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            # increase
            word_dictionary[word] += 1
        else:
            # add to the word_dictionary
            word_dictionary[word] = 1
    sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})

    # return render(request, "count.html", {'word_dictionary': word_dictionary.items()})
    # lesson 16 - counting words  ---minutes 9-13


def about(request):
    # about our company
    return render(request, 'about.html')

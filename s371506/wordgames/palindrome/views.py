from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, './palindrome/index.html')

def palindrome_check(request, word):
    clean_word = word.replace(" ", "").lower()
    
    is_plnd = clean_word == clean_word[::-1]
    
    context_data = {
        'test_word' : clean_word,
        'is_palindrome' : is_plnd,
    }
    return render(request, './palindrome/palindrome_check.html', context_data)
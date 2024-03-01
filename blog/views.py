from django.shortcuts import render

posts = [
     {
        'author' : 'Manthan',
        'title' : "blog post 1",
        'content': 'march 2002'
     },
      {
        'author' : 'Shetty',
        'title' : "blog post 2",
        'content': 'April 2002'
     }
]

def home(request):
    context = {
         'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html',{'title': 'About'})

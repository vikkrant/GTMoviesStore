from django.shortcuts import render
from django.shortcuts import render
movies = [
    {
        'id': 1, 'name': 'Grown Ups', 'price': 11.99,
        'description': 'A reunion comedy.'
    },
    {
        'id': 2, 'name': 'Avengers: Endgame', 'price': 15.99,
        'description': 'It has all led to this. The Infinity Saga culminates in a 3-hour epic.'
    },
    {
        'id': 3, 'name': 'The Dark Knight Rises', 'price': 10.99,
        'description': 'Christian Bale\'s Batman returns for his swan song.'
    },
    {
        'id': 4, 'name': 'Tenet', 'price': 14.99,
        'description': 'Entropy takes center-stage in this time-warping thriller.',
    },
{
        'id': 5, 'name': 'Hit Man', 'price': 7.99,
        'description': 'Glen Powell and Adria Arjona in a twisted thriller where the lines between '
                       'good and eveil are blurred like never before.',
    },
]
def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

def show(request, id):
    movie = movies[id - 1]
    template_data = {}
    template_data['title'] = movie['name']
    template_data['movie'] = movie
    return render(request, 'movies/show.html', {'template_data': template_data})
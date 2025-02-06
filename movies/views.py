
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
    search_term = request.GET.get('search')
    template_data = {}
    if search_term:
        if search_term.lower() == "grown ups" :
            template_data['movies'] = [movies[0]]
        elif search_term.lower() == "avengers: endgame" or search_term.lower() == "avengers endgame":
            template_data['movies'] = [movies[1]]
        elif search_term.lower() == "the dark knight rises":
            template_data['movies'] = [movies[2]]
        elif search_term.lower() == "tenet":
            template_data['movies'] = [movies[3]]
        elif search_term.lower() == "hit man":
            template_data['movies'] = [movies[4]]
    else:
        template_data['movies'] = movies
    template_data['title'] = 'Movies'
    return render(request, 'movies/index.html',
                  {'template_data': template_data})
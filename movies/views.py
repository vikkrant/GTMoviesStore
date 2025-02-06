
from django.shortcuts import render
movies = [
    {
        'id': 1, 'name': 'Grown Ups', 'price': 11.99,
        'description': 'A reunion comedy.',
        'image':'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRo4HAwpQt84GdMwBs8oB4_DZwx8QuRYWJ7m1UKip6kP4KKMT13jBiCSKRD6PajvN4MGwbzsQ'
    },
    {
        'id': 2, 'name': 'Avengers: Endgame', 'price': 15.99,
        'description': 'It has all led to this. The Infinity Saga culminates in a 3-hour epic.',
        'image':'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQBV4DwisDoIO-v1M44sNNYtyOM2GSL3q-vijXQyB_VDuZqyop8NgiZQajBO-3oqbbzfuXIcA'
    },
    {
        'id': 3, 'name': 'The Dark Knight Rises', 'price': 10.99,
        'description': 'Christian Bale\'s Batman returns for his swan song.',
        'image':'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQQHtvd1nGFx5jyEtLrkG6zjGXyuM6By82nUufnlZHo2oLlWHkGYyMXsTdZbdKclDK-aK64dg'
    },
    {
        'id': 4, 'name': 'Tenet', 'price': 14.99,
        'description': 'Entropy takes center-stage in this time-warping thriller.',
        'image':'https://www.usatoday.com/gcdn/authoring/authoring-images/2024/01/26/USAT/72360800007-ap-24025554216395.jpg?crop=2023,2699,x0,y150'
    },
{
        'id': 5, 'name': 'Hit Man', 'price': 7.99,
        'description': 'Glen Powell and Adria Arjona in a twisted thriller where the lines between '
                       'good and evil are blurred like never before.',
        'image':'https://static0.colliderimages.com/wordpress/wp-content/uploads/sharedimages/2025/01/01690084_poster_w780.jpg'
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
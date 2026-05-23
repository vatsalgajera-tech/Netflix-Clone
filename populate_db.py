import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netflix_clone.settings')
django.setup()

from core.models import Category, Genre, Content, Banner

def run():
    print("Clearing old data...")
    Category.objects.all().delete()
    Genre.objects.all().delete()
    Content.objects.all().delete()
    Banner.objects.all().delete()

    categories = {
        'Action': Category.objects.create(name="Action & Adventure", description="Exciting action movies."),
        'Drama': Category.objects.create(name="Dramas", description="Compelling emotional stories."),
        'Comedy': Category.objects.create(name="Comedies", description="Laugh out loud comedies."),
        'Sci-Fi': Category.objects.create(name="Sci-Fi & Fantasy", description="Otherworldly adventures."),
        'Crime': Category.objects.create(name="Crime & Thriller", description="Mystery and crime."),
        'Other': Category.objects.create(name="Trending Now", description="What everyone is watching.")
    }

    genre_objects = {}

    print("Fetching real content from TVmaze API to guarantee valid posters...")
    try:
        response = requests.get('https://api.tvmaze.com/shows')
        all_shows = response.json()[:100]  # Get top 100 shows
    except Exception as e:
        print(f"Error fetching shows: {e}")
        all_shows = []

    for idx, show in enumerate(all_shows):
        title = show.get('name')
        
        # Remove HTML tags from the summary to make it plain text
        summary_html = show.get('summary', 'No description available.')
        soup = BeautifulSoup(summary_html, "html.parser")
        description = soup.get_text()
        
        # Keep description to 4-5 lines max.
        long_desc = description
        if len(long_desc.split('.')) > 5:
            long_desc = '.'.join(long_desc.split('.')[:4]) + '.'

        language = show.get('language', 'English')
        genres = show.get('genres', [])
        image_data = show.get('image')
        poster_url = image_data.get('original') if image_data else ''
        
        premiered = show.get('premiered', '2020-01-01')
        year = int(premiered.split('-')[0]) if premiered else 2020
        
        # Determine Category based on Genres
        cat = categories['Other']
        if 'Action' in genres or 'Adventure' in genres: cat = categories['Action']
        elif 'Drama' in genres or 'Romance' in genres: cat = categories['Drama']
        elif 'Comedy' in genres: cat = categories['Comedy']
        elif 'Science-Fiction' in genres or 'Fantasy' in genres: cat = categories['Sci-Fi']
        elif 'Crime' in genres or 'Thriller' in genres or 'Mystery' in genres: cat = categories['Crime']

        # Half as Movies, Half as Series
        c_type = 'Series' if idx < 50 else 'Movie'
        c_duration = "Multiple Seasons" if c_type == 'Series' else "2h 15m"

        # Create Content
        c = Content.objects.create(
            title=title,
            description=long_desc,
            content_type=c_type,
            release_year=year,
            duration=c_duration,
            language=language,
            rating="TV-MA",
            poster_url=poster_url,
            category=cat
        )

        # Handle Genres
        for g_name in genres:
            if g_name not in genre_objects:
                genre_objects[g_name] = Genre.objects.create(name=g_name)
            c.genres.add(genre_objects[g_name])

    print("Creating Banners...")
    Banner.objects.create(
        title="Beetlejuice",
        subtitle="A couple of recently deceased ghosts contract the services of a bio-exorcist in order to remove the obnoxious new owners of their house.",
        button_text="Play Now",
        redirect_url="/detail/1/",
        is_active=True,
    )

    print(f"Successfully added {Content.objects.count()} Movies and TV Shows (100 TOTAL) with real posters!")

if __name__ == '__main__':
    run()

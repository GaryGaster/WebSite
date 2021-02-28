from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main import views


class TestUrls(SimpleTestCase):

    # Test section home
    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    # Test section movies
    def test_movies_list_is_resolved(self):
        url = reverse('movies-home')
        self.assertEqual(resolve(url).func.view_class, views.MovieListView)

    def test_movies_users_list_is_resolved(self):
        url = reverse('user-movies', args=['username'])
        self.assertEqual(resolve(url).func.view_class, views.UserMovieListView)

    def test_movie_detail_is_resolved(self):
        url = reverse('movie-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.MovieDetailView)

    def test_movie_create_is_resolved(self):
        url = reverse('movie-create')
        self.assertEqual(resolve(url).func.view_class, views.MovieCreateView)

    def test_movie_update_is_resolved(self):
        url = reverse('movie-update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.MovieUpdateView)

    def test_movie_delete_is_resolved(self):
        url = reverse('movie-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.MovieDeleteView)

    def test_movie_upvote_is_resolved(self):
        url = reverse('movie-upvote', args=['1'])
        self.assertEqual(resolve(url).func, views.movie_upvote)

    # Test section series
    def test_series_list_is_resolved(self):
        url = reverse('series-home')
        self.assertEqual(resolve(url).func.view_class, views.SerialListView)

    def test_series_users_list_is_resolved(self):
        url = reverse('user-series', args=['username'])
        self.assertEqual(resolve(url).func.view_class, views.UserSerialListView)

    def test_serial_detail_is_resolved(self):
        url = reverse('serial-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.SerialDetailView)

    def test_serial_create_is_resolved(self):
        url = reverse('serial-create')
        self.assertEqual(resolve(url).func.view_class, views.SerialCreateView)

    def test_serial_update_is_resolved(self):
        url = reverse('serial-update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.SerialUpdateView)

    def test_serial_delete_is_resolved(self):
        url = reverse('serial-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.SerialDeleteView)

    def test_serial_upvote_is_resolved(self):
        url = reverse('serial-upvote', args=['1'])
        self.assertEqual(resolve(url).func, views.serial_upvote)

    # Test section anime
    def test_anime_list_is_resolved(self):
        url = reverse('anime-home')
        self.assertEqual(resolve(url).func.view_class, views.AnimeListView)

    def test_anime_users_list_is_resolved(self):
        url = reverse('user-anime', args=['username'])
        self.assertEqual(resolve(url).func.view_class, views.UserAnimeListView)

    def test_anime_detail_is_resolved(self):
        url = reverse('anime-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.AnimeDetailView)

    def test_anime_create_is_resolved(self):
        url = reverse('anime-create')
        self.assertEqual(resolve(url).func.view_class, views.AnimeCreateView)

    def test_anime_update_is_resolved(self):
        url = reverse('anime-update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.AnimeUpdateView)

    def test_anime_delete_is_resolved(self):
        url = reverse('anime-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.AnimeDeleteView)

    def test_anime_upvote_is_resolved(self):
        url = reverse('anime-upvote', args=['1'])
        self.assertEqual(resolve(url).func, views.anime_upvote)

    # Test section actors
    def test_actors_list_is_resolved(self):
        url = reverse('actors-home')
        self.assertEqual(resolve(url).func.view_class, views.ActorListView)

    def test_actor_detail_is_resolved(self):
        url = reverse('actor-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.ActorDetailView)

    def test_actor_create_is_resolved(self):
        url = reverse('actor-create')
        self.assertEqual(resolve(url).func.view_class, views.ActorCreateView)

    def test_actor_update_is_resolved(self):
        url = reverse('actor-update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.ActorUpdateView)

    def test_actor_delete_is_resolved(self):
        url = reverse('actor-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, views.ActorDeleteView)

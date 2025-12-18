import requests


class APIKinopoisk:
    def __init__(self, BASE_URL_API, API_KEY):
        self.base_url = BASE_URL_API
        self.api_key = API_KEY
        self.headers = {
            'X-API-KEY': API_KEY,
            'Content-Type': 'application/json',
        }

    def films_by_director(self, director: str) -> requests.Response:
        """Поиск фильмов по имени режиссёра."""
        params = {"name": director}
        return requests.get(
            f"{self.base_url}/v1/persons",
            headers=self.headers,
            params=params
        )

    def search_films_by_keywords(self, keyword: str) -> requests.Response:
        """Поиск фильмов по ключевым словам."""
        params = {"keyword": keyword}
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params=params
        )

    def search_films_by_genre(self, genre: str) -> requests.Response:
        """Поиск фильмов по жанру."""
        params = {"genres": genre}
        return requests.get(
            f"{self.base_url}/v2.1/films/filters",
            headers=self.headers,
            params=params
        )

    def search_films_by_emoticons(self, title: str) -> requests.Response:
        """Поиск фильмов с использованием смайликов."""
        params = {"query": title}
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params=params
        )

    def search_for_movies_with_random_letters(self, title: str) \
            -> requests.Response:
        """Поиск по произвольному набору букв."""
        params = {"query": title}
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params=params
        )

    def search_special_chars(self, title: str) -> requests.Response:
        """Поиск по произвольному набору букв."""
        params = {"query": title}
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params=params
        )

    def search_whitespace(self, title: str) -> requests.Response:
        """Поиск с пробелом."""
        params = {"query": title}
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params=params
        )

    def post_request_not_allowed(self) -> requests.Response:
        """POST-запрос к GET-эндпоинту."""
        return requests.post(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=self.headers,
            json={}
        )

    def invalid_api_key(self, invalid_key: str) -> requests.Response:
        """Запрос с некорректным API-ключом."""
        headers = {
            "X-API-KEY": invalid_key,
            "Content-Type": "application/json"
        }
        return requests.get(
            f"{self.base_url}/v2.1/films/search-by-keyword",
            headers=headers
        )

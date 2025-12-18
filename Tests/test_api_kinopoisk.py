import pytest
import allure
from Thesis_Kinopoisk.config import BASE_URL_API, API_KEY
from Thesis_Kinopoisk.Pages.api_kinopoisk import APIKinopoisk
from Thesis_Kinopoisk.test_data import API_SEARCH_QUERIES, API_EXPECTED_STATUS


@allure.feature("API Тесты Кинопоиска")
@pytest.mark.api
class TestAPIKinopoisk:

    @pytest.fixture(scope="class")
    def api_client(self):
        """Инициализация клиента API."""
        return APIKinopoisk(BASE_URL_API, API_KEY)

    @allure.title("Поиск фильмов по режиссёру")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_films_by_director(self, api_client):
        director = API_SEARCH_QUERIES["director"]

        with (allure.step(f"Выполняем поиск по режиссёру '{director}'")):
            response = api_client.films_by_director(director=director)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["success"]

        with allure.step("Проверяем, что результаты не пустые"):
            assert len(response.json()['items']) > 0

        with allure.step("Проверяем, что в результатах есть фильмы "
                         "Хаяо Миядзаки"):
            for film in response.json()['items']:
                assert film.get('nameRu') == "Хаяо Миядзаки"

    @allure.title(f"Поиск фильмов по ключевым словам")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_films_by_keywords(self, api_client):
        keywords = API_SEARCH_QUERIES["keywords"]

        with allure.step("Выполняем поиск по ключевым словам"):
            response = api_client.search_films_by_keywords(keywords)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["success"]

        with allure.step("Проверяем, что результаты не пустые"):
            assert len(response.json()['films']) > 0

        with allure.step("Проверяем, что в результатах есть фильмы ветер"):
            films = response.json()['films']
            assert any("ветер" in film.get('nameRu', '').lower()
                       for film in films)

    @allure.title("Поиск фильмов по жанру")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_films_by_genre(self, api_client):
        genre = API_SEARCH_QUERIES["genre"]

        with allure.step("Выполняем поиск по жанру"):
            response = api_client.search_films_by_genre(genre=genre)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["success"]

        with allure.step("Проверяем, что результаты не пустые"):
            assert len(response.json()['genres']) > 0

        with allure.step("Проверяем, что в результатах есть фильмы аниме"):
            genres = response.json().get('genres', [])
            assert "аниме" in [g.get('genre', '') for g in genres]

    @allure.title("Поиск фильмов с использованием смайликов")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_films_by_emoticons(self, api_client):
        emoticons = API_SEARCH_QUERIES["emoticons"]

        with allure.step("Выполняем поиск фильмов с использованием смайликов"):
            response = api_client.search_films_by_emoticons(emoticons)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["bad_request"]

        with allure.step("Проверяем, что фильмов не найдено"):
            films = response.json().get("films", [])
            assert len(films) == 0

    @allure.title("Поиск по произвольному набору букв")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_for_movies_with_random_letters(self, api_client):
        random_letters = API_SEARCH_QUERIES["random_letters"]

        with allure.step("Выполняем поиск по произвольному набору букв"):
            response = api_client.search_for_movies_with_random_letters(
                random_letters)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["bad_request"]

        with allure.step("Проверяем, что фильмов не найдено"):
            films = response.json().get("films", [])
            assert len(films) == 0

    @allure.title("Поиск по спецсимволам")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_special_chars(self, api_client):
        special_chars = API_SEARCH_QUERIES["special_chars"]

        with allure.step("Выполняем поиск по произвольному набору букв"):
            response = api_client.search_special_chars(special_chars)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["bad_request"]

        with allure.step("Проверяем, что фильмов не найдено"):
            films = response.json().get("films", [])
            assert len(films) == 0

    @allure.title("Поиск по пробелу")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_whitespace(self, api_client):
        whitespace = API_SEARCH_QUERIES["whitespace"]

        with allure.step("Выполняем поиск по пробелу"):
            response = api_client.search_whitespace(whitespace)

        with allure.step("Проверяем статус код"):
            assert response.status_code == API_EXPECTED_STATUS["bad_request"]

        with allure.step("Проверяем, что фильмов не найдено"):
            films = response.json().get("films", [])
            assert len(films) == 0

    @allure.title("POST-запрос к GET-эндпоинту")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_post_request_not_allowed(self, api_client):

        with allure.step("Отправляем POST-запрос к эндпоинту, ожидающему GET"):
            response = api_client.post_request_not_allowed()

        with allure.step("Проверяем статус-код 500"):
            assert response.status_code == API_EXPECTED_STATUS["server_error"]

    @allure.title("Запрос с некорректным API-ключом")
    @allure.story("Расширенный поиск")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_invalid_api_key(self, api_client):
        invalid_key = API_SEARCH_QUERIES["invalid_key"]

        with allure.step(f"Отправляем запрос с неверным API-ключом: "
                         f"{invalid_key}"):
            response = api_client.invalid_api_key(invalid_key)

        with allure.step("Проверяем статус-код 401 (Unauthorized)"):
            assert response.status_code == API_EXPECTED_STATUS["unauthorized"]

"""
Константы для тестовых данных (поисковые запросы, ожидаемые результаты).
"""

# Запросы для UI-тестов:
UI_SEARCH_QUERIES = {
    "cyrillic": "Царство",
    "latin": "Kingdom",
    "year": "2012",
    "hieroglyphs": "三國",
    "partial": "King",
    "empty": "",
}

# Ожидаемые фрагменты текста в результатах:
UI_EXPECTED_TEXT = {
    "cyrillic": "Царство",
    "latin": "Kingdom",
    "year": "2012",
    "partial": "King",
}

# Запросы для API-тестов:
API_SEARCH_QUERIES = {
    "director": "Хаяо Миядзаки",
    "keywords": "ветер",
    "genre": "аниме",
    "emoticons": "😃😃😃",
    "random_letters": "gvrdkfgs",
    "special_chars": "@#!$@",
    "whitespace": " ",
    "invalid_key": "1234"
}

# Ожидаемые статусы ответов API:
API_EXPECTED_STATUS = {
    "success": 200,
    "bad_request": 400,
    "unauthorized": 401,
    "server_error": 500,
}

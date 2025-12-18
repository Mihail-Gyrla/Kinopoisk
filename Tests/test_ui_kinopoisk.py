from Thesis_Kinopoisk.Pages.ui_kinopoisk import UIKinopoisk
from Thesis_Kinopoisk.test_data import UI_SEARCH_QUERIES, UI_EXPECTED_TEXT
import pytest
import allure


@allure.feature("Поиск фильмов")
@pytest.mark.ui
class TestUIKinopoiskSearch:

    @allure.title("Поиск на Кириллице")
    @allure.story("UI")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cyrillic_search(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["cyrillic"]
        expected_text = UI_EXPECTED_TEXT["cyrillic"]

        with allure.step(f"Поиск фильма с названием '{query}'"):
            kinopoisk_page.search(query)

        with allure.step("Ожидание результатов поиска"):
            results = kinopoisk_page.get_search_results()

        with allure.step("Проверка результатов поиска"):
            print(f"Найдено элементов: {len(results)}")
            assert len(results) > 0
            assert any(expected_text in elem.text for elem in results)

    @allure.title("Поиск на Латинице")
    @allure.story("UI")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_latin_text(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["latin"]
        expected_text = UI_EXPECTED_TEXT["latin"]

        with allure.step(f"Поиск фильма с названием '{query}'"):
            kinopoisk_page.search(query)

        with allure.step("Ожидание результатов поиска"):
            results = kinopoisk_page.get_search_results()

        with allure.step("Проверка результатов поиска"):
            print(f"Найдено элементов: {len(results)}")
            assert len(results) > 0
            assert any(expected_text in elem.text for elem in results)

    @allure.title("Поиск по году выхода фильма")
    @allure.story("UI")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_by_year(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["year"]
        expected_text = UI_EXPECTED_TEXT["year"]

        with allure.step(f"Поиск фильма с названием '{query}'"):
            kinopoisk_page.search(query)

        with allure.step("Ожидание результатов поиска"):
            results = kinopoisk_page.get_search_results()

        with allure.step("Проверка результатов поиска"):
            with allure.step("Проверка результатов поиска"):
                print(f"Найдено элементов: {len(results)}")
                assert len(results) > 0
                assert any(expected_text in elem.text for elem in results)

    @allure.title("Поиск фильма с иероглифами")
    @allure.story("UI")
    @allure.severity(allure.severity_level.NORMAL)
    def test_hieroglyphs_text(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["hieroglyphs"]

        with allure.step(f"Поиск фильма с названием '{query}'"):
            kinopoisk_page.search(query)

        with allure.step("Ожидание результатов поиска"):
            results = kinopoisk_page.get_search_results()

        with allure.step("Проверка результатов поиска"):
            assert len(results) > 0

    @allure.title("Поиск по части названия")
    @allure.story("UI")
    @allure.severity(allure.severity_level.MINOR)
    def test_partial_search(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["partial"]
        expected_text = UI_EXPECTED_TEXT["partial"]

        with allure.step(f"Поиск фильма по части названия '{query}'"):
            kinopoisk_page.search(query)

        with allure.step("Ожидание результатов поиска"):
            results = kinopoisk_page.get_search_results()

        with (allure.step("Проверка результатов поиска")):
            print(f"Найдено элементов: {len(results)}")
            assert len(results) > 0
            assert any(expected_text in elem.text for elem in results)

    @allure.title("Поиск с пустым запросом")
    @allure.story("UI")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_search(self, kinopoisk_page: UIKinopoisk):
        query = UI_SEARCH_QUERIES["empty"]

        with allure.step(f"Выполнить поиск с пустым запросом ('{query}')"):
                kinopoisk_page.search(query)

        with allure.step("Проверить наличие кнопок 'Случайный фильм' "
                         "или 'Навигатор по лучшим фильмам'"):
            random_movie_buttons = kinopoisk_page.get_random_movie_buttons()
            assert random_movie_buttons, "Кнопки не найдены"
            button_texts = [button.text for button in random_movie_buttons]

            expected_texts = ["Случайный фильм", "Навигатор по лучшим фильмам"]

            assert any(any(expected_text in text
                           for expected_text in expected_texts)
                       for text in button_texts), \
                (f"Ожидаемые кнопки {expected_texts} "
                 f"не найдены среди текстов: {button_texts}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from Thesis_Kinopoisk.config import BASE_URL


class UIKinopoisk:
    DEFAULT_WAIT = 10
    SEARCH_INPUT_SELECTOR = "input[name='kp_query']"
    SEARCH_RESULTS_SELECTOR = ".search_results.search_results_last"
    MOVIE_METRICS_SELECTOR = ".js-serp-metrika"
    RANDOM_MOVIE_BUTTON_SELECTOR = ".randomMovieButton"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=BASE_URL):
        """Открывает указанную страницу."""
        self.driver.get(url)

    def search(self, query):
        """
        Выполняет поиск по запросу.
        :param query: строка запроса
        """
        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT)
        search_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.SEARCH_INPUT_SELECTOR))
        )
        search_input.clear()
        if query:
            search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def wait_for_elements(self, selector):
        """
        Ожидает появления элементов по CSS-селектору.
        :param selector: CSS-селектор
        :param timeout: время ожидания в секундах
        :return: список элементов
        """
        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT)
        return wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, selector)))

    def get_search_results(self):
        """Возвращает элементы результатов поиска."""
        return self.driver.find_elements(
            By.CSS_SELECTOR, self.SEARCH_RESULTS_SELECTOR
        )

    def get_metrics_results(self):
        """Возвращает элементы метрик фильмов."""
        return self.driver.find_elements(
            By.CSS_SELECTOR, self.MOVIE_METRICS_SELECTOR
        )

    def get_random_movie_buttons(self):
        """Возвращает кнопки «Случайный фильм»."""
        return self.driver.find_elements(
            By.CSS_SELECTOR, self.RANDOM_MOVIE_BUTTON_SELECTOR
        )

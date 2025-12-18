import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Thesis_Kinopoisk.Pages.ui_kinopoisk import UIKinopoisk


def pytest_addoption(parser):
    """Добавляем параметр --test-type для выбора режима тестов."""
    parser.addoption(
        "--test-type",
        action="store",
        default="all",
        choices=["ui", "api", "all"],
        help="Режим запуска: 'ui', 'api' или 'all'"
    )


@pytest.fixture(scope="session")
def driver():
    """
    Фикстура для настройки и управления WebDriver.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def kinopoisk_page(driver):
    """
    Фикстура для инициализации страницы Кинопоиска.
    """
    page = UIKinopoisk(driver)
    page.open()
    return page

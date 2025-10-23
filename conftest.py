import pytest
import allure
from playwright.sync_api import sync_playwright
from pages_selector.main_page import MainPage


@pytest.fixture(scope="session")
def browser_context_args():
    """Настройки браузера для всех тестов"""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "record_video_dir": "test-results/videos/",
        "record_video_size": {"width": 1920, "height": 1080}
    }


@pytest.fixture(scope="function")
def main_page(page):
    """Фикстура для главной страницы"""
    return MainPage(page)


@pytest.fixture(scope="function", autouse=True)
def setup_test(page):
    """Настройка перед каждым тестом"""
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(30000)
    yield
    # Очистка после теста
    if page:
        page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "page" in item.funcargs:
                page = item.funcargs["page"]
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Не удалось создать скриншот: {e}")



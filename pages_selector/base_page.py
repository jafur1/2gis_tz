from playwright.sync_api import Page
import allure
from typing import Optional
from urllib.parse import urljoin


class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://effective-mobile.ru"
    
    def navigate(self, url: str = None) -> None:
        """Переход на страницу"""
        if url and url.startswith(("http://", "https://")):
        # Если передан полный URL, используем как есть
            target_url = url
        else:
        # Иначе объединяем с базовым URL
            target_url = urljoin(self.base_url, url or "")
        with allure.step(f"Переход на страницу {target_url}"):
            self.page.goto(target_url)
            self.page.wait_for_load_state("networkidle")
    
    def wait_for_element(self, selector: str, timeout: int = 10000) -> None:
        """Ожидание появления элемента"""
        with allure.step(f"Ожидание элемента {selector}"):
            self.page.wait_for_selector(selector, timeout=timeout)
    
    def click_element(self, selector: str, timeout: int = 10000) -> None:
        """Клик по элементу"""
        with allure.step(f"Клик по элементу {selector}"):
            self.page.click(selector, timeout=timeout)
    
    def get_text(self, selector: str) -> str:
        """Получение текста элемента"""
        return self.page.text_content(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        """Проверка видимости элемента"""
        try:
            return self.page.is_visible(selector)
        except:
            return False
    
    def get_current_url(self) -> str:
        """Получение текущего URL"""
        return self.page.url
    
    def take_screenshot(self, name: str = "screenshot") -> None:
        """Создание скриншота"""
        screenshot = self.page.screenshot()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    
    def scroll_to_element(self, selector: str) -> None:
        """Прокрутка к элементу"""
        self.page.locator(selector).scroll_into_view_if_needed()
    
    def wait_for_url_change(self, expected_url: str, timeout: int = 10000) -> None:
        """Ожидание изменения URL"""
        with allure.step(f"Ожидание перехода на {expected_url}"):
            self.page.wait_for_url(expected_url, timeout=timeout)




from playwright.sync_api import Page
import allure
from .base_page import BasePage
from .main_selector import NavigationMain, MainPage, ButtonLink


class MainPage(BasePage):
    """Класс для работы с главной страницей effective-mobile.ru"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    @allure.step("Переход на главную страницу")
    def navigate_to_main(self) -> None:
        """Переход на главную страницу"""
        self.navigate()
        self.wait_for_page_load()
    
    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self) -> None:
        """Ожидание полной загрузки страницы"""
        self.page.wait_for_load_state("networkidle")
        # Ждем появления основных элементов
        try:
            self.wait_for_element(MainPage.HEADER, timeout=5000)
        except:
            pass  # Если header не найден, продолжаем
    
    @allure.step("Проверка видимости навигационного меню")
    def is_navigation_visible(self) -> bool:
        """Проверка видимости навигационного меню"""
        return self.is_element_visible(NavigationMain.NAVIGATION_MENU)
    
    @allure.step("Клик по ссылке 'О нас'")
    def click_about_link(self) -> None:
        """Клик по ссылке 'О нас'"""
        self.click_element(NavigationMain.ABOUT_LINK)
    
    @allure.step("Клик по ссылке 'Контакты'")
    def click_contacts_link(self) -> None:
        """Клик по ссылке 'Контакты'"""
        self.click_element(NavigationMain.CONTACTS_LINK)
    
    @allure.step("Клик по ссылке 'Услуги'")
    def click_services_link(self) -> None:
        """Клик по ссылке 'Услуги'"""
        self.click_element(NavigationMain.SERVICES_LINK)
    
    @allure.step("Клик по ссылке 'Портфолио'")
    def click_portfolio_link(self) -> None:
        """Клик по ссылке 'Портфолио'"""
        self.click_element(NavigationMain.PORTFOLIO_LINK)
    
    @allure.step("Клик по ссылке 'Блог'")
    def click_blog_link(self) -> None:
        """Клик по ссылке 'Блог'"""
        self.click_element(NavigationMain.BLOG_LINK)
    
    @allure.step("Клик по ссылке 'Карьера'")
    def click_career_link(self) -> None:
        """Клик по ссылке 'Карьера'"""
        self.click_element(NavigationMain.CAREER_LINK)
    
    @allure.step("Проверка наличия основных секций")
    def check_main_sections(self) -> dict:
        """Проверка наличия основных секций на странице"""
        sections = {
            "header": self.is_element_visible(MainPage.HEADER),
            "footer": self.is_element_visible(MainPage.FOOTER),
            "hero": self.is_element_visible(MainPage.HERO_SECTION),
            "services": self.is_element_visible(MainPage.SERVICES_SECTION),
            "about": self.is_element_visible(MainPage.ABOUT_SECTION),
            "contacts": self.is_element_visible(MainPage.CONTACTS_SECTION)
        }
        return sections
    
    @allure.step("Получение всех ссылок навигации")
    def get_navigation_links(self) -> list:
        """Получение всех ссылок навигации"""
        links = []
        try:
            # Ищем все ссылки в навигации
            nav_links = self.page.locator("nav a, header a").all()
            for link in nav_links:
                href = link.get_attribute("href")
                text = link.text_content()
                if href and text:
                    links.append({"text": text.strip(), "href": href})
        except Exception as e:
            allure.attach(f"Ошибка при получении ссылок: {str(e)}", "error", allure.attachment_type.TEXT)
        return links
    
    @allure.step("Проверка контактной информации")
    def check_contact_info(self) -> dict:
        """Проверка наличия контактной информации"""
        contact_info = {
            "phone": self.is_element_visible(ButtonLink.PHONE_LINK),
            "email": self.is_element_visible(ButtonLink.EMAIL_LINK),
            "contact_button": self.is_element_visible(ButtonLink.CONTACT_BUTTON)
        }
        return contact_info
    
    @allure.step("Прокрутка к секции")
    def scroll_to_section(self, section_selector: str) -> None:
        """Прокрутка к определенной секции"""
        self.scroll_to_element(section_selector)
    
    @allure.step("Получение заголовка страницы")
    def get_page_title(self) -> str:
        """Получение заголовка страницы"""
        return self.page.title()
    
    @allure.step("Получение мета-описания")
    def get_meta_description(self) -> str:
        """Получение мета-описания страницы"""
        try:
            meta_desc = self.page.locator('meta[name="description"]').get_attribute("content")
            return meta_desc or ""
        except:
            return ""



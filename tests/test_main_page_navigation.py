import pytest
import allure
from playwright.sync_api import expect
from pages_selector.main_page import MainPage
from pages_selector.main_selector import NavigationMain


@allure.epic("Главная страница effective-mobile.ru")
@allure.feature("Навигация по разделам")
class TestMainPageNavigation:
    """Тесты навигации по главной странице"""
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("critical")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigate_to_about_page(self, main_page: MainPage):
        """Тест перехода на страницу 'О нас'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
            main_page.take_screenshot("main_page_loaded")
        
        with allure.step("Проверка наличия ссылки 'О нас'"):
            about_links = main_page.page.locator(NavigationMain.ABOUT_LINK)
            assert about_links.count() > 0, "Ссылка 'О нас' не найдена на странице"
        
        with allure.step("Клик по ссылке 'О нас'"):
            main_page.click_about_link()
            main_page.wait_for_page_load()
        
        with allure.step("Проверка URL страницы 'О нас'"):
            current_url = main_page.get_current_url()
            main_page.take_screenshot("about_page")
            
            # Проверяем, что URL содержит about или мы на правильной странице
            assert ("about" in current_url.lower() or 
                   "о-нас" in current_url.lower() or 
                   "company" in current_url.lower()), \
                f"Неверный URL после перехода на 'О нас': {current_url}"
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("critical")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigate_to_contacts_page(self, main_page: MainPage):
        """Тест перехода на страницу 'Контакты'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
            main_page.take_screenshot("main_page_loaded")
        
        with allure.step("Проверка наличия ссылки 'Контакты'"):
            contacts_links = main_page.page.locator(NavigationMain.CONTACTS_LINK)
            assert contacts_links.count() > 0, "Ссылка 'Контакты' не найдена на странице"
        
        with allure.step("Клик по ссылке 'Контакты'"):
            main_page.click_contacts_link()
            main_page.wait_for_page_load()
        
        with allure.step("Проверка URL страницы 'Контакты'"):
            current_url = main_page.get_current_url()
            main_page.take_screenshot("contacts_page")
            
            # Проверяем, что URL содержит contact или мы на правильной странице
            assert ("contact" in current_url.lower() or 
                   "контакт" in current_url.lower()), \
                f"Неверный URL после перехода на 'Контакты': {current_url}"
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("high")
    @pytest.mark.navigation
    def test_navigate_to_services_page(self, main_page: MainPage):
        """Тест перехода на страницу 'Услуги'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка наличия ссылки 'Услуги'"):
            services_links = main_page.page.locator(NavigationMain.SERVICES_LINK)
            if services_links.count() > 0:
                with allure.step("Клик по ссылке 'Услуги'"):
                    main_page.click_services_link()
                    main_page.wait_for_page_load()
                
                with allure.step("Проверка URL страницы 'Услуги'"):
                    current_url = main_page.get_current_url()
                    main_page.take_screenshot("services_page")
                    
                    assert ("service" in current_url.lower() or 
                           "услуг" in current_url.lower()), \
                        f"Неверный URL после перехода на 'Услуги': {current_url}"
            else:
                pytest.skip("Ссылка 'Услуги' не найдена на странице")
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("high")
    @pytest.mark.navigation
    def test_navigate_to_portfolio_page(self, main_page: MainPage):
        """Тест перехода на страницу 'Портфолио'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка наличия ссылки 'Портфолио'"):
            portfolio_links = main_page.page.locator(NavigationMain.PORTFOLIO_LINK)
            if portfolio_links.count() > 0:
                with allure.step("Клик по ссылке 'Портфолио'"):
                    main_page.click_portfolio_link()
                    main_page.wait_for_page_load()
                
                with allure.step("Проверка URL страницы 'Портфолио'"):
                    current_url = main_page.get_current_url()
                    main_page.take_screenshot("portfolio_page")
                    
                    assert ("portfolio" in current_url.lower() or 
                           "портфолио" in current_url.lower() or
                           "work" in current_url.lower()), \
                        f"Неверный URL после перехода на 'Портфолио': {current_url}"
            else:
                pytest.skip("Ссылка 'Портфолио' не найдена на странице")
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("medium")
    @pytest.mark.navigation
    def test_navigate_to_blog_page(self, main_page: MainPage):
        """Тест перехода на страницу 'Блог'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка наличия ссылки 'Блог'"):
            blog_links = main_page.page.locator(NavigationMain.BLOG_LINK)
            if blog_links.count() > 0:
                with allure.step("Клик по ссылке 'Блог'"):
                    main_page.click_blog_link()
                    main_page.wait_for_page_load()
                
                with allure.step("Проверка URL страницы 'Блог'"):
                    current_url = main_page.get_current_url()
                    main_page.take_screenshot("blog_page")
                    
                    assert ("blog" in current_url.lower() or 
                           "блог" in current_url.lower() or
                           "news" in current_url.lower()), \
                        f"Неверный URL после перехода на 'Блог': {current_url}"
            else:
                pytest.skip("Ссылка 'Блог' не найдена на странице")
    
    @allure.story("Переходы по основным разделам")
    @allure.severity("medium")
    @pytest.mark.navigation
    def test_navigate_to_career_page(self, main_page: MainPage):
        """Тест перехода на страницу 'Карьера'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка наличия ссылки 'Карьера'"):
            career_links = main_page.page.locator(NavigationMain.CAREER_LINK)
            if career_links.count() > 0:
                with allure.step("Клик по ссылке 'Карьера'"):
                    main_page.click_career_link()
                    main_page.wait_for_page_load()
                
                with allure.step("Проверка URL страницы 'Карьера'"):
                    current_url = main_page.get_current_url()
                    main_page.take_screenshot("career_page")
                    
                    assert ("career" in current_url.lower() or 
                           "карьер" in current_url.lower() or
                           "job" in current_url.lower() or
                           "vacancy" in current_url.lower()), \
                        f"Неверный URL после перехода на 'Карьера': {current_url}"
            else:
                pytest.skip("Ссылка 'Карьера' не найдена на странице")
    
    @allure.story("Проверка структуры главной страницы")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_main_page_structure(self, main_page: MainPage):
        """Тест проверки структуры главной страницы"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
            main_page.take_screenshot("main_page_structure")
        
        with allure.step("Проверка наличия основных секций"):
            sections = main_page.check_main_sections()
            
            # Проверяем наличие header и footer
            assert sections["header"], "Header не найден на странице"
            assert sections["footer"], "Footer не найден на странице"
            
            # Логируем информацию о найденных секциях
            allure.attach(
                str(sections),
                name="Найденные секции",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Проверка навигационного меню"):
            assert main_page.is_navigation_visible(), "Навигационное меню не видно"
        
        with allure.step("Получение ссылок навигации"):
            nav_links = main_page.get_navigation_links()
            allure.attach(
                str(nav_links),
                name="Ссылки навигации",
                attachment_type=allure.attachment_type.JSON
            )
            
            assert len(nav_links) > 0, "Ссылки навигации не найдены"
    
    @allure.story("Проверка контактной информации")
    @allure.severity("high")
    @pytest.mark.smoke
    def test_contact_information(self, main_page: MainPage):
        """Тест проверки контактной информации на главной странице"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка контактной информации"):
            contact_info = main_page.check_contact_info()
            
            allure.attach(
                str(contact_info),
                name="Контактная информация",
                attachment_type=allure.attachment_type.JSON
            )
            
            # Проверяем наличие хотя бы одного способа связи
            has_contact = any(contact_info.values())
            assert has_contact, "Контактная информация не найдена на странице"
    
    @allure.story("Проверка мета-информации")
    @allure.severity("medium")
    def test_page_meta_information(self, main_page: MainPage):
        """Тест проверки мета-информации страницы"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка заголовка страницы"):
            title = main_page.get_page_title()
            assert title, "Заголовок страницы пустой"
            assert len(title) > 0, "Заголовок страницы должен содержать текст"
            
            allure.attach(title, name="Заголовок страницы", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Проверка мета-описания"):
            description = main_page.get_meta_description()
            if description:
                allure.attach(description, name="Мета-описание", attachment_type=allure.attachment_type.TEXT)
                assert len(description) > 0, "Мета-описание должно содержать текст"


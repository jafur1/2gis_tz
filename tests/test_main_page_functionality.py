import pytest
import allure
from playwright.sync_api import expect
from pages_selector.main_page import MainPage
from pages_selector.main_selector import ButtonLink


@allure.epic("Главная страница effective-mobile.ru")
@allure.feature("Функциональность")
class TestMainPageFunctionality:
    """Тесты функциональности главной страницы"""
    
    @allure.story("Проверка интерактивных элементов")
    @allure.severity("high")
    @pytest.mark.regression
    def test_contact_button_functionality(self, main_page: MainPage):
        """Тест функциональности кнопки 'Связаться'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
            main_page.take_screenshot("main_page_before_contact_click")
        
        with allure.step("Поиск кнопки 'Связаться'"):
            contact_buttons = main_page.page.locator(ButtonLink.CONTACT_BUTTON)
            if contact_buttons.count() > 0:
                with allure.step("Клик по кнопке 'Связаться'"):
                    contact_buttons.first.click()
                    main_page.wait_for_page_load()
                    main_page.take_screenshot("after_contact_button_click")
                
                with allure.step("Проверка результата клика"):
                    current_url = main_page.get_current_url()
                    # Проверяем, что произошел переход или открылась форма
                    assert (current_url != main_page.base_url or 
                           main_page.is_element_visible("form") or
                           main_page.is_element_visible(".modal") or
                           main_page.is_element_visible(".popup")), \
                        "Кнопка 'Связаться' не работает"
            else:
                pytest.skip("Кнопка 'Связаться' не найдена на странице")
    
    @allure.story("Проверка интерактивных элементов")
    @allure.severity("high")
    @pytest.mark.regression
    def test_order_button_functionality(self, main_page: MainPage):
        """Тест функциональности кнопки 'Заказать'"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Поиск кнопки 'Заказать'"):
            order_buttons = main_page.page.locator(ButtonLink.ORDER_BUTTON)
            if order_buttons.count() > 0:
                with allure.step("Клик по кнопке 'Заказать'"):
                    order_buttons.first.click()
                    main_page.wait_for_page_load()
                    main_page.take_screenshot("after_order_button_click")
                
                with allure.step("Проверка результата клика"):
                    current_url = main_page.get_current_url()
                    # Проверяем, что произошел переход или открылась форма
                    assert (current_url != main_page.base_url or 
                           main_page.is_element_visible("form") or
                           main_page.is_element_visible(".modal") or
                           main_page.is_element_visible(".popup")), \
                        "Кнопка 'Заказать' не работает"
            else:
                pytest.skip("Кнопка 'Заказать' не найдена на странице")
    
    @allure.story("Проверка контактных ссылок")
    @allure.severity("medium")
    @pytest.mark.regression
    def test_phone_links(self, main_page: MainPage):
        """Тест проверки телефонных ссылок"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Поиск телефонных ссылок"):
            phone_links = main_page.page.locator(ButtonLink.PHONE_LINK)
            if phone_links.count() > 0:
                with allure.step("Проверка атрибутов телефонных ссылок"):
                    for i in range(phone_links.count()):
                        link = phone_links.nth(i)
                        href = link.get_attribute("href")
                        text = link.text_content()
                        
                        allure.attach(
                            f"Телефонная ссылка {i+1}: {text} -> {href}",
                            name=f"Телефонная ссылка {i+1}",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        
                        assert href and href.startswith("tel:"), \
                            f"Некорректная телефонная ссылка: {href}"
                        assert text and text.strip(), \
                            f"Пустой текст телефонной ссылки"
            else:
                pytest.skip("Телефонные ссылки не найдены на странице")
    
    @allure.story("Проверка контактных ссылок")
    @allure.severity("medium")
    @pytest.mark.regression
    def test_email_links(self, main_page: MainPage):
        """Тест проверки email ссылок"""
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Поиск email ссылок"):
            email_links = main_page.page.locator(ButtonLink.EMAIL_LINK)
            if email_links.count() > 0:
                with allure.step("Проверка атрибутов email ссылок"):
                    for i in range(email_links.count()):
                        link = email_links.nth(i)
                        href = link.get_attribute("href")
                        text = link.text_content()
                        
                        allure.attach(
                            f"Email ссылка {i+1}: {text} -> {href}",
                            name=f"Email ссылка {i+1}",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        
                        assert href and href.startswith("mailto:"), \
                            f"Некорректная email ссылка: {href}"
                        assert text and text.strip(), \
                            f"Пустой текст email ссылки"
            else:
                pytest.skip("Email ссылки не найдены на странице")
    
    @allure.story("Проверка адаптивности")
    @allure.severity("medium")
    @pytest.mark.regression
    def test_mobile_responsiveness(self, main_page: MainPage):
        """Тест адаптивности для мобильных устройств"""
        with allure.step("Установка мобильного viewport"):
            main_page.page.set_viewport_size({"width": 375, "height": 667})
        
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
            main_page.take_screenshot("mobile_view")
        
        with allure.step("Проверка основных элементов в мобильном виде"):
            # Проверяем, что основные элементы все еще видны
            assert main_page.is_navigation_visible() or main_page.is_element_visible(".mobile-menu"), \
                "Навигация не видна в мобильном виде"
            
            # Проверяем наличие основных секций
            sections = main_page.check_main_sections()
            assert sections["header"], "Header не виден в мобильном виде"
    
    @allure.story("Проверка производительности")
    @allure.severity("low")
    @pytest.mark.regression
    def test_page_load_performance(self, main_page: MainPage):
        """Тест производительности загрузки страницы"""
        with allure.step("Измерение времени загрузки"):
            import time
            start_time = time.time()
            
            main_page.navigate_to_main()
            
            end_time = time.time()
            load_time = end_time - start_time
            
            allure.attach(
                f"Время загрузки: {load_time:.2f} секунд",
                name="Время загрузки",
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Проверяем, что страница загружается за разумное время
            assert load_time < 10, f"Страница загружается слишком долго: {load_time:.2f} секунд"
    
    @allure.story("Проверка консольных ошибок")
    @allure.severity("medium")
    @pytest.mark.regression
    def test_console_errors(self, main_page: MainPage):
        """Тест проверки ошибок в консоли"""
        console_errors = []
        
        def handle_console_message(msg):
            if msg.type == "error":
                console_errors.append(msg.text)
        
        with allure.step("Настройка обработчика консольных сообщений"):
            main_page.page.on("console", handle_console_message)
        
        with allure.step("Переход на главную страницу"):
            main_page.navigate_to_main()
        
        with allure.step("Проверка консольных ошибок"):
            if console_errors:
                error_text = "\n".join(console_errors)
                allure.attach(
                    error_text,
                    name="Консольные ошибки",
                    attachment_type=allure.attachment_type.TEXT
                )
                
                # Проверяем, что нет критических ошибок
                critical_errors = [error for error in console_errors 
                                 if "404" not in error and "favicon" not in error.lower()]
                assert len(critical_errors) == 0, f"Найдены критические ошибки: {critical_errors}"
            else:
                allure.attach("Консольных ошибок не найдено", 
                            name="Консольные ошибки", 
                            attachment_type=allure.attachment_type.TEXT)


# навигация
class NavigationMain:
    NAVIGATION_MENU = "nav"
    ABOUT_LINK = "a[href*='about'], a:has-text('О нас'), a:has-text('О компании')"
    CONTACTS_LINK = "a[href*='contact'], a:has-text('Контакты')"
    SERVICES_LINK = "a[href*='service'], a:has-text('Услуги')"
    PORTFOLIO_LINK = "a[href*='portfolio'], a:has-text('Портфолио')"
    BLOG_LINK = "a[href*='blog'], a:has-text('Блог')"
    CAREER_LINK = "a[href*='career'], a:has-text('Карьера')"
    
    # основные блоки
class MainPage:
    HEADER = "header"
    FOOTER = "footer"
    HERO_SECTION = ".hero, .banner, .main-banner"
    SERVICES_SECTION = ".services, .our-services"
    ABOUT_SECTION = ".about, .about-us"
    CONTACTS_SECTION = ".contacts, .contact-us"
    
    # кнопок и форм
class ButtonLink:
    CONTACT_BUTTON = "button:has-text('Связаться'), a:has-text('Связаться')"
    ORDER_BUTTON = "button:has-text('Заказать'), a:has-text('Заказать')"
    PHONE_LINK = "a[href^='tel:']"
    EMAIL_LINK = "a[href^='mailto:']"
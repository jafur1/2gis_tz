"""
Конфигурация для тестов effective-mobile.ru
"""
import os
from typing import Dict, Any


class Config:
    """Класс конфигурации для тестов"""
    
    # Базовые настройки
    BASE_URL = "https://effective-mobile.ru"
    TIMEOUT = 10000
    NAVIGATION_TIMEOUT = 30000
    
    # Настройки браузера
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    
    # Настройки viewport
    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1920"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "1080"))
    
    # Настройки параллельности
    WORKERS = int(os.getenv("WORKERS", "1"))
    
    # Настройки отчетов
    ALLURE_RESULTS_DIR = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
    ALLURE_REPORT_DIR = os.getenv("ALLURE_REPORT_DIR", "allure-report")
    TEST_RESULTS_DIR = os.getenv("TEST_RESULTS_DIR", "test-results")
    
    # Настройки видео
    RECORD_VIDEO = os.getenv("RECORD_VIDEO", "false").lower() == "true"
    VIDEO_DIR = os.path.join(TEST_RESULTS_DIR, "videos")
    
    # Настройки скриншотов
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    SCREENSHOT_DIR = os.path.join(TEST_RESULTS_DIR, "screenshots")
    
    # Настройки логирования
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.path.join(TEST_RESULTS_DIR, "test.log")
    
    # Настройки для различных окружений
    ENVIRONMENTS = {
        "local": {
            "base_url": "https://effective-mobile.ru",
            "timeout": 10000,
            "headless": False
        },
        "ci": {
            "base_url": "https://effective-mobile.ru",
            "timeout": 30000,
            "headless": True
        },
        "staging": {
            "base_url": "https://staging.effective-mobile.ru",
            "timeout": 15000,
            "headless": True
        }
    }
    
    @classmethod
    def get_environment_config(cls, env: str = None) -> Dict[str, Any]:
        """Получение конфигурации для определенного окружения"""
        if env is None:
            env = os.getenv("TEST_ENV", "local")
        
        return cls.ENVIRONMENTS.get(env, cls.ENVIRONMENTS["local"])
    
    @classmethod
    def get_browser_args(cls) -> Dict[str, Any]:
        """Получение аргументов браузера"""
        return {
            "headless": cls.HEADLESS,
            "slow_mo": cls.SLOW_MO,
            "viewport": {
                "width": cls.VIEWPORT_WIDTH,
                "height": cls.VIEWPORT_HEIGHT
            }
        }
    
    @classmethod
    def get_context_args(cls) -> Dict[str, Any]:
        """Получение аргументов контекста браузера"""
        args = {
            "viewport": {
                "width": cls.VIEWPORT_WIDTH,
                "height": cls.VIEWPORT_HEIGHT
            },
            "ignore_https_errors": True
        }
        
        if cls.RECORD_VIDEO:
            args["record_video_dir"] = cls.VIDEO_DIR
            args["record_video_size"] = {
                "width": cls.VIEWPORT_WIDTH,
                "height": cls.VIEWPORT_HEIGHT
            }
        
        return args



from selenium.webdriver.common.by import By


class TestLocators:
    input_registration_name_locator = By.XPATH, "(//form[@class='Auth_form__3qKeq mb-20']//input)[1]"  # Ввод имени на странице регистрации
    input_registration_login_locator = By.XPATH, "(//form[@class='Auth_form__3qKeq mb-20']//input)[2]"  # Ввод логина (почты) на странице регистрации
    input_registration_password_locator = By.XPATH, "//input[@type='password']"  # Ввод пароля на странице регистрации
    registration_button_locator = By.XPATH, "//button[text()='Зарегистрироваться']"  # Кнопка регистрации на странице регистрации
    registration_error_text_locator = By.XPATH, "//p[@class='input__error text_type_main-default']"
    header_login_page_locator = By.XPATH, "//div/h2[text()='Вход']"  # Заголовок Вход на странице логина
    input_email_login_page_locator = By.XPATH, "//input[@name='name']"  # Ввод логина (почты) на странице логина
    input_password_login_page_locator = By.XPATH, "//input[@name='Пароль']"  # Ввод логина(почты) на странице логина
    login_page_button_locator = By.XPATH, "//button[text()='Войти']"  # Кнопка Войти
    make_order_button_locator = By.XPATH, "//button[text()='Оформить заказ']"  # Кнопка Оформить заказ
    login_main_page_button_locator = By.XPATH, "//button[text()='Войти в аккаунт']"  # Кнопка входа в аккаунт
    login_button_locator = By.XPATH, "//a[@href='/login']"  # Кнопка логина
    user_account_header_button_locator = By.XPATH, "//p[text()='Личный Кабинет']"  # Кнопка перехода в личный кабинет
    constructor_button_locator = By.XPATH, "//p[text()='Конструктор']"  # Кнопка перехода на страницу конструктора
    header_constructor_page_locator = By.XPATH, "//h1[text()='Соберите бургер']"  # Заголовок Собери бургер
    logout_button_locator = By.XPATH, "//button[text()='Выход']"  # Кнопка выхода из аккаунта
    constructor_sauce_button_locator = By.XPATH, "//span[text()='Соусы']"  # Таб Соусы
    constructor_fillings_button_locator = By.XPATH, "//span[text()='Начинки']"  # Таб Начинки
    constructor_buns_button_locator = By.XPATH, "//span[text()='Булки']"  # Таб Булки
    logo_locator = By.XPATH, "//*[name()='svg' and @width='290']"  # Лого
    constructor_sauce_active_button_locator = By.XPATH, "//div[contains(@class, 'current')]/span[text()='Соусы']"  # Активный таб Соусы
    constructor_buns_active_button_locator = By.XPATH, "//div[contains(@class, 'current')]/span[text()='Булки']"  # Активный таб Булки
    constructor_fillings_active_button_locator = By.XPATH, "//div[contains(@class, 'current')]/span[text()='Начинки']"  # Активный таб Начинки

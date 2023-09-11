import time
import selectors_main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://demo.app.stack-it.ru/fl/")

login = driver.find_element(By.XPATH, selectors_main.LOGIN_XPATH)
login.send_keys("DEMOWEB")

password = driver.find_element(By.XPATH, selectors_main.PASSWORD_XPATH)
password.send_keys("awdrgy")

submit_button = driver.find_element(By.XPATH, selectors_main.SUBMIT_BTN_XPATH)
submit_button.click()

# Нажатие кнопки когда другой пользователь уже авторизован
try:
    modal_stack = driver.find_element(By.XPATH, selectors_main.MODAL_STACK_XPATH)
except:
    modal_stack = False
print('modal_stack = ', modal_stack)
if modal_stack:
    stack_button = driver.find_element(By.XPATH, selectors_main.STACK_BTN_XPATH)
    stack_button.click()

# time.sleep(5)
stack_card_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, selectors_main.STACK_CARD_BTN_XPATH))
    )
stack_card_button.click()


# ''' Тест_1. Добавление района c пустым полем Название района '''
#
# def test_empty_district_field():
#     add_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, selectors_main.ADD_BTN_XPATH))
#     )
#     add_button.click()
#
#     add_district_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, selectors_main.ADD_DISTRICT_BTN_XPATH))
#     )
#     add_district_button.click()
#
#     enter_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, selectors_main.ENTER_BTN_XPATH))
#     )
#         # driver.find_element(By.XPATH, selectors_main.ENTER_BTN_XPATH)
#     enter_button.click()
#     # time.sleep(5)
#
#     message = driver.find_element(By.XPATH, selectors_main.MESSAGE_XPATH)
#     print(message.text)
#     assert "Поле не может быть пустым" in message.text
#
#
# ''' Тест_2. Создание Района с невалидным Названием (Состоит из пробелов) '''
#
# def test_not_valid_district_field():
#     # time.sleep(5)
#     input_district_name = driver.find_element(By.XPATH, selectors_main.INPUT_DISTRICT_NAME_XPATH)
#     input_district_name.send_keys("       ")
#     enter_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, selectors_main.ENTER_BTN_XPATH))
#         )
#     enter_button.click()
#     message = ''
#     try:
#         message = driver.find_element(By.XPATH, selectors_main.MESSAGE_XPATH)
#         print(message.text)
#         message = message.text
#     except:
#         print("Тест_2. Валидация данных поля Название района работает некорректно")
#     assert "Введите корректное название" in message
#     time.sleep(5)


''' Тест_3. Удаление Района c вложенными записями '''

def test_delete_destrict():
    # time.sleep(5)
    select_district = driver.find_element(By.XPATH, selectors_main.SELECT_DISTRICT_XPATH)
    driver.execute_script('arguments[0].click();', select_district)
    driver.find_element(By.XPATH, selectors_main.DELETE_DISTRICT_XPATH).click()
    driver.find_element(By.XPATH, selectors_main.YES_BUTTON_XPATH).click()
    message = ''
    try:
        time.sleep(2)
        message = driver.find_element(By.XPATH, selectors_main.MESSAGE_2_XPATH)
        print('Текст всплывающего сообщения: ', message.text)
        message = message.text
    except:
        print("Тест_3. Проверка запрета на удаление провалена")
    assert "Нельзя удалить данный уровень из-за вложенных записей" in message
    time.sleep(10)

# driver.quit()


# Селекторы формы авторизации
LOGIN_XPATH = "//input[@data-cy='login']"
PASSWORD_XPATH = "//input[@data-cy='password']"
SUBMIT_BTN_XPATH = "//button[@data-cy='submit-btn']"
STACK_BTN_XPATH = "//button[@data-cy='stack-btn']"  # Кнопка Продолжить вход, когда уже авторизован
MODAL_STACK_XPATH = "//div[@data-test-id='stack-yes-no']"

# Селекторы Главного меню
STACK_CARD_BTN_XPATH = "//a[@data-test-id='Адреса проживающих']"

# Селекторы страницы Адреса проживающих
ADD_BTN_XPATH = "//button[@data-cy='btn-add']"
ADD_DISTRICT_BTN_XPATH = "//div[@class='v-list-item__title font-weight-regular' and text()='Район']"

# Селекторы Модального окна добавления Района
ENTER_BTN_XPATH = "//span[@class='v-btn__content' and text()='Внести']"
MESSAGE_XPATH = "//div[@class='v-messages__message']"
INPUT_DISTRICT_NAME_XPATH = "//input[@data-test-id='Название района']"

# Селекторы для выбора и удаления Района
SELECT_DISTRICT_XPATH = "//input[@type='checkbox']"
DELETE_DISTRICT_XPATH = "//button[@data-cy='btn-delete']"
YES_BUTTON_XPATH = "//button/span[@class='v-btn__content' and text()='Да']"
MESSAGE_2_XPATH = "//span[@text()='Нельзя удалить данный уровень из-за вложенных записей']"
COUNT_BEFORE_XPATH = "//thead[@data-cy='stack-table-head']"
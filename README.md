# Sprint_5
Автотесты для Stellar Burgers
Что проверяют тесты:
Регистрация 
test_registration.py 
Создание уникального логина generate_email
1. Успешная регистрация - с валидными данными (имя, email, пароль 6+ символов) test_successful_registration
2. Регистрация с пустым именем - система не должна пропускать 
test_registration_with_empty_name
3. Регистрация с невалидным email - различные некорректные форматы email 
test_registration_with_invalid_email
4. Регистрация с коротким паролем - пароли менее 6 символов
test_registration_with_short_password
5. Регистрация с существующим email - попытка повторной регистрации
test_registration_with_exciting_email

Вход: 
1. вход по кнопке «Войти в аккаунт» на главной test_login_main_page_button,
2. вход через кнопку «Личный кабинет» test_login_personal_account_button, 
3. вход через кнопку в форме регистрации test_login_registration_form,
4. вход через кнопку в форме восстановления пароля test_login_via_password_recovery_form.

Переход в Личный кабинет: 
1. Переход в Личный кабинет неавторизованного пользователя test_redirect_to_personal_account_unauthorized
2. Переход в Личный кабинет авторизованного пользователя test_redirect_to_personal_account_authorized

Переход из личного кабинета в конструктор :
test_navigation_to_constructor.py

1.Переход в Конструктор из Личного кабинета test_switching_to_constructor_from_personal_account
2. Переход в Конструктор из Ленты заказов test_switching_to_constructor_from_order_feed
3. Переход по логотипу из Личного кабинета test_switching_logo_from_personal_account
4. Переход по логотипу из Ленты заказов test_redirect_via_logo_from_order_feed

Выход из аккаунта:
test_log_out_account.py
1.  Выход из аккаунта через Личный кабинет test_logout_from_personal_account

Раздел «Конструктор»: 
test_constructor_section.py
1. Переход между разделами конструктора test_constructor_section

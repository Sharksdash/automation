import time
# Импортируем webdriver(набор команд для управления браузером)
#from selenium import webdriver
# Вызываем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
#time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#driver.get("https://google.ru")
#time.sleep(5)
# Метод find_element_by_xpath позволяет найти нужный элемент на сайте
# Обсудим его чуть позже
# Ищем элемент поля поиска
#textfield = driver.find_element_by_xpath("//textarea[@name='q']")
# Напишем текст в поле поиска
#textfield.send_keys("погода на завтра")
#time.sleep(5)
# Укажем путь к кнопке поиска
#submit_button = driver.find_element_by_xpath("//div[@jsname='VlcLAe']//input[@class='gNO89b']")
# Нажмём на кнопку поиска с помощью команды .click()
#submit_button.click() # После нажатия на кнопку должны появиться результаты поиска
#time.sleep(5)
# Добавим команду, с помощью которой браузер будет сам закрываться после проведения теста
#driver.quit()


#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("file:///C:/Users/%D0%A0%D0%B0%D0%B8%D0%BB%D1%8C/Desktop/%D0%9A%D1%83%D1%80%D1%81%D1%8B%20be%20tester/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80.html") # это обычно что-то наподобие: file:///C:/Users/.....
#elementByLinkText = driver.find_element_by_link_text("Перейти к содержимому")
#elementByPartialLinkText = driver.find_element_by_partial_link_text("Пере")
#driver.quit()

#import time
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
#driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
#login = driver.find_element_by_name("username") # объявляем переменную login, задаём ей значение селектора поля логин
#login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
#password = driver.find_element_by_name("password") # объявляем переменную password, задаём ей значение селектора поля пароль
#password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
#login_btn = driver.find_element_by_css_selector(".oxd-button") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
#login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
#time.sleep(3)
#pim_btn = driver.find_element_by_link_text("PIM")
#pim_btn.click()
#time.sleep(3)
#add_btn = driver.find_element_by_link_text("Add Employee")
#add_btn.click()
#time.sleep(3)
#fn = driver.find_element_by_name("firstName")
#fn.send_keys("David")
#ln = driver.find_element_by_name("lastName")
#ln.send_keys("Jonson")
#eng = driver.find_element_by_css_selector(".oxd-grid-2 .oxd-input")
#eng.send_keys("DJ")
#log_btn = driver.find_element_by_css_selector(".oxd-form-actions .oxd-button--secondary")
#log_btn.click()
#driver.quit()


#import time
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
#Логин в систему
#driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
#time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
#login = driver.find_element_by_name("username") # объявляем переменную login, задаём ей значение селектора поля логин
#login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
#password = driver.find_element_by_name("password") # объявляем переменную password, задаём ей значение селектора поля пароль
#password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
#login_btn = driver.find_element_by_css_selector(".oxd-button") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
#login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
#time.sleep(3)
#pim_btn = driver.find_element_by_link_text("PIM")
#pim_btn.click()
#time.sleep(3)
#enjoy = driver.find_element_by_link_text("Employee List")
#enjoy.send_keys("0221")
#search_btn = driver.find_element_by_css_selector(".orangehrm-left-space")
#search_btn.click()
#time.sleep(3)
#delete_btn = driver.find_element_by_css_selector(".bi-trash")
#delete_btn.click()
#time.sleep(3)
#delete_yes_btn = driver.find_element_by_css_selector(".oxd-button--label-danger")
#delete_yes_btn.click()
#driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
login = driver.find_element_by_name("user-name")
login.send_keys("standard_user")
pw = driver.find_element_by_name("password")
pw.send_keys("secret_sauce")
login_btn = driver.find_element_by_name("login-button")
login_btn.click()
time.sleep(3)
t1 = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
t1.click()
t2 = driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
t2.click()
t3 = driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
t3.click()
cart = driver.find_element_by_class_name("shopping_cart_link")
cart.click()
time.sleep(3)
items_count = driver.find_elements_by_class_name("cart_item")
if len(items_count) == 3:
    print("В корзине 3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))



#import time
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#from selenium.webdriver.support.select import Select
#driver.maximize_window()
#driver.get("https://demo.us.espocrm.com/")
#time.sleep(3)
#language_selector=driver.find_element_by_id("field-language")
#select= Select(language_selector)
#select.select_by_value("en_GB")
#login_btn= driver.find_element_by_id("btn-login")
#login_btn.click()
#time.sleep(3)
#activities_btn=driver.find_element_by_id("nav-tab-group-group-8")
#activities_btn.click()
#Tasks_btn=driver.find_element_by_link_text("Tasks")
#Tasks_btn.click()
#time.sleep(3)
#driver.quit()

#from selenium.webdriver.support.select import Select

#language_selector= driver.find_element_by_id("field-language")
#select= Select(language_selector)
#select.select_by_value("en_GB")

#activities_btn=driver.find_element_by_id("nav-tab-group-group-8")
#activities_btn.click()
#Tasks_btn=driver.find_element_by_link_text("Tasks")
#Tasks_btn.click()

#activities_selector=driver.find_element_by_id("nav-tab-group-group-8")
#select= Select(activities_selector)
#select.select_by_link_text("Tasks")



#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.execute_script("alert('Скрипт выполнен успешно!');")


                #Задание 2
#from selenium import webdriver
#import time
#from selenium.webdriver.support.select import Select
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.get("http://demo.automationtesting.in/Register.html")
#first_name = driver.find_element_by_xpath("//input[@placeholder='First Name']")
#first_name.send_keys("Venrose")
#last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
#last_name.send_keys("General")
#email = driver.find_element_by_xpath("//input[@ng-model='EmailAdress']")
#email.send_keys("65432143f@mail.ru")
#phone = driver.find_element_by_xpath("//input[@ng-model='Phone']")
#phone.send_keys("8800555353")
#gender = driver.find_element_by_xpath("//input[@value='Male']")
#gender.click()
#country = driver.find_element_by_id("countries")
#select = Select(country)
#select.select_by_value("Japan")
#date_of_birth_year = driver.find_element_by_id("yearbox")
#select_year = Select(date_of_birth_year)
#select_year.select_by_value("1999")
#date_of_birth_month = driver.find_element_by_css_selector("div:nth-child(3) > select")
#select_month = Select(date_of_birth_month)
#select_month.select_by_value("May")
#date_of_birth_day = driver.find_element_by_id("daybox")
#select_day = Select(date_of_birth_day)
#select_day.select_by_value("15")
#password = driver.find_element_by_id("firstpassword")
#password.send_keys("7654321rs")
#password_two = driver.find_element_by_id("secondpassword")
#password_two.send_keys("7654321rs")
#photo_file = (r'C:\Users\Раиль\Desktop\photo_2022-11-27_21-11-17.jpg')
#file_upload = driver.find_element_by_id("imagesrc")
#file_upload.send_keys(photo_file)
#driver.execute_script("window.scrollBy(0, 300);")
#submit_btn = driver.find_element_by_id("submitbtn")
#submit_btn.click()
#time.sleep(3)
#current_page = driver.current_url
#print(current_page)
#



#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#alert_script = driver.execute_script("alert('Скрипт выполнен успешно!');") # вызываем окно alert
#alert = driver.switch_to.alert # переключаемся в область окна alert; обратите внимание, “()” после switch_to.alert не нужны
#alert_text = alert.text # получаем текст с помощью команды .text
#print(alert_text) # выводим содержимое в консоли
#alert.accept() # нажимаем на “OK” в окне alert



            #Задание 3 модальные окна
#from selenium import webdriver
#import time
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.get("https://demo.automationtesting.in/WebTable.html")
#switch_to = driver.find_element_by_link_text("SwitchTo")
#switch_to.click()
#alerts = driver.find_element_by_link_text("Alerts")
#alerts.click()
#time.sleep(3)
#alert_btn = driver.find_element_by_css_selector("#OKTab > button")
#alert_btn.click()
#alert = driver.switch_to.alert
#alert_expected_text = "I am an alert box!"
#alert_text = alert.text
#alert.accept()
#time.sleep(3)
#current_url = driver.current_url
#time.sleep(3)
#tab_2=driver.execute_script("window.open();")
#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
#river.get("https://demo.automationtesting.in/Alerts.html")
#time.sleep(3)
#modal = driver.find_element_by_css_selector(".nav-tabs > li:nth-child(2)")
#modal.click()
#display_btn = driver.find_element_by_css_selector("#CancelTab > button")
#display_btn.click()
#confirm=driver.switch_to.alert
#confirm.dismiss()
#time.sleep(3)
#third_tab = driver.execute_script("window.open();")
#window_after_second = driver.window_handles[2]
#driver.switch_to.window(window_after_second)
#driver.get(current_url)
#time.sleep(3)
#text_send = driver.find_element_by_css_selector(".nav-tabs > li:nth-child(3)")
#text_send.click()
#txt2 = driver.find_element_by_css_selector("#Textbox > button")
#txt2.click()
#prompt= driver.switch_to.alert
#prompt.send_keys("УРА! ЗАДАНИЕ ВЫПОЛНЕНО!")
#prompt.accept()
#driver.quit()


                        #Задание 4
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.get("https://demo.automationtesting.in/WebTable.html")
#more_btn=driver.find_element_by_link_text("More")
#more_btn.click()
#loader_btn=driver.find_element_by_link_text("Loader")
#loader_btn.click()
#run_btn=WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable((By.ID,"loader"))
#)
#run_btn.click() #после нажатия накнопку Run не открыватся модальоне окно, далее примерно написал код
#lorem_text = WebDriverWait(driver, 20).until(
#EC.text_to_be_present_in_element((By.*, "мой селектор"), "Lorem"))
#save_changes_btn = WebDriverWait(driver, 20).until(
#EC.element_to_be_clickable((By..*, "мой селектор"))
#)
#save_changes_btn.click()
#driver.quit()


                        #Задание 5
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.implicitly_wait(5)
#driver.get("https://demo.automationtesting.in/WebTable.html")
#more_btn=driver.find_element_by_link_text("More")
#more_btn.click()
#dynamic_data_btn=driver.find_element_by_link_text("Dynamic Data")
#dynamic_data_btn.click()
#title = driver.find_element_by_tag_name("h3")
#title_text = title.text
#assert title_text == "Loading the data Dynamically"
#get_dynamic_data_btn=driver.find_element_by_id("save")
#get_dynamic_data_btn.click()
#сайт не реагирует на кнопку get dynamic data, дальнейшая проверка невозможна


#                    Задание 6
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.implicitly_wait(5)
#driver.get("https://demo.automationtesting.in/WebTable.html")
#more_btn=driver.find_element_by_link_text("More")
#more_btn.click()
#file_upload_btn=driver.find_element_by_link_text("File Upload")
#file_upload_btn.click()
#picture=("C:\Users\Раиль\Desktop\photo_2022-11-27_21-11-17.jpg")
#select_file=driver.find_element_by_id("input-4")
#select_file.send_keys(picture)
#Видимо сайт упавший, работает с трудом, но после выбора картинки нет ответной реакции, поэтому далее написал примерно
#remove_btn = driver.find_element_by_id("remove")
#remove_btn.click()
#txt_file = ("C:\Users\Раиль\Desktop\Пустой")
#txt_file_upload.send_keys(txt_file)
#close_red_message = driver.find_element_by_id("error message")
#close_red_message.click()
#driver.quit()

                        #Задание 7
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.implicitly_wait(5)
#driver.get("https://demo.automationtesting.in/WebTable.html")
#more_btn=driver.find_element_by_link_text("More")
#more_btn.click()
#project_btn=driver.find_element_by_link_text("JQuery ProgressBar")
#project_btn.click()
#project_bar=WebDriverWait(driver,10).until(
#    EC.invisibility_of_element_located((By))
#)
#start_download = driver.find_element_by_id("downloadButton")
#start_download.click()
#close_btn_text = WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.ID, "cancel"), "Cancel Download")
#)
#close_btn = driver.find_element_by_id("close")
#close_btn.click()
#start_download.click()
#end_text = WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.ID, "txt complete"), "Complete!")
#)
#driver.quit()
#В данном задании не реагировала кнопка загрузки, так что после отмены тоде написал лишь примерный вариант последовательности

                    #Задание 8
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.implicitly_wait(5)
#driver.get("https://demo.automationtesting.in/WebTable.html")
#switch_to_btn=driver.find_element_by_link_text("SwitchTo")
#switch_to_btn.click()
#windows_btn=driver.find_element_by_link_text("Windows")
#windows_btn.click()
#new_tab = driver.current_window_handle #открыл новую стр
#open_tab_btn = driver.find_element_by_css_selector(".active .btn .btn-info")
#open_tab_btn.click()
#second_tab = driver.window_handles[1] #переключился закрыл и снова переключился
#driver.switch_to.window(second_tab)
#driver.close()
#driver.switch_to.window(new_tab)
#multiple_tab = driver.find_element_by_css_selector("li:nth-child(3) > a.analystic")
#multiple_tab.click()
#multiple_btn = driver.find_element_by_css_selector("#Multiple > button")
#multiple_btn.click()
#driver.switch_to.window(driver.window_handles[2]) #переход на новую страницу и сравнение ссылок
#http_check = WebDriverWait.until(
#    EC.url_to_be("https://demo.automationtesting.in/Index.html")
#)
#tab_number = WebDriverWait.until(
#    EC.number_of_windows_to_be(3)
#)
#print(tab_number)
#email = driver.find_element_by_id("email")
#email.send_keys("7654321rs90@gmail.ru")
#send_btn = driver.find_element_by_id("enterimg")
#send_btn.click()
#last_check = WebDriverWait.until(
#    EC.url_to_be("https://demo.automationtesting.in/Register.html")
#)
#driver.quit()

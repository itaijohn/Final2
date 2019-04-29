from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/Users/user/Downloads/chromedriver.exe')
driver.get("http://192.168.99.100:5000/")

text = driver.find_element_by_tag_name("body").text
print(text)
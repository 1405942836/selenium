# 简单使用

from selenium import webdriver          # 导入浏览器驱动


driver = webdriver.Chrome()             # 初始化
driver.get('https://www.baidu.com')     # 打开百度首页

print(driver.title)                     # 打印网页标题

driver.quit()                           # 关闭浏览器

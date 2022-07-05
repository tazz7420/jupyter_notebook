import os,selenium,pyperclip
from selenium import webdriver
print ('The coordinate system must be WGS84.')
OpenFileName = input('The fullpath of file which you want to search address. EX.D:\\pythontest2.txt'+ '\n')
OpenFileName2 = input('recording road name. EX.D:/pythontest4.txt'+'\n')
driver = webdriver.Chrome()
import fileinput,time
from time import sleep
file = open(OpenFileName)
driver.get('https://www.google.com.tw/maps/@23.4857501,120.0843006,7z?hl=zh-TW')
windows = driver.window_handles
driver.switch_to.window(windows[-1])
for line in file:
	if str.upper(line) == 'END':
		print ('done')
		break
	else:
		driver.get('https://www.google.com.tw/maps/@23.4857501,120.0843006,7z?hl=zh-TW')
		sleep(1.50)
		searchAddress=driver.find_element_by_id('searchboxinput')
		sleep(1.50)
		searchAddress.send_keys(line)
		sleep(7.50)
		searchAddress=driver.find_element_by_id('searchbox-searchbutton').click()
		getAddress=driver.find_element_by_class_name('lRsTH-Tswv1b-JIbuQc-icon-LgbsSe').click()
		txtAddress=pyperclip.paste()
		try:
			file2=open(OpenFileName2,'a', encoding = 'big5')
			file2.write(txtAddress+'\n')
		except:
			try:
				file2=open(OpenFileName2,'a', encoding = 'gbk')
				file2.write(txtAddress+'\n')
			except:
				file2=open(OpenFileName2,'a', encoding = 'utf-8')
				file2.write(txtAddress)
				file2.close
				file2.read
				file2=open(OpenFileName2,'a', encoding = 'big5')
				file2.write('\n')
		file2.close
		file2.read
		print (txtAddress)
	pass
file.close
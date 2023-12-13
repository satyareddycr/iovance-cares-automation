import random
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from TestData import environment_urls
#from TestData import credentials
import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.support.select import Select

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://iovancecares--caresqa.sandbox.my.site.com/hospitalPortalCommercial/s/login')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=30)

# verifying & entering the username
try:
	print('Searching for the user name input box =======> ',
	      end='')
	username_input = driver.find_element(By.XPATH,
	                                     '//*[@placeholder="Email"]')
	print('Successfully found the username input')
	if username_input.is_displayed():
		print('Entering the username in username input =======> ',
		      end='')
		username_input.send_keys('carol@iovance.com.caresqa')
		print('Entered the username in username input')
except exceptions as e:
	print(f'Element not found : {e}')

# verifying & entering the password
try:
	print('Searching for the Password input box =======> ',
	      end='')
	username_input = driver.find_element(By.XPATH,
	                                     '//*[@placeholder="Password"]')
	print('Successfully found the password input')
	if username_input.is_displayed():
		print('Entering the passkey in password input =======> ',
		      end='')
		username_input.send_keys('IovanceQA@12')
		print('Entered the passkey in password input')
except exceptions as e:
	print(f'Element not found : {e}')

# verifying & clicking on the signin button
try:
	print('Clicking on the sign in button ========> ',
	      end='')
	signin_button = driver.find_element(By.XPATH,
	                                    '//*[text()="Sign in"]')
	signin_button.click()
	print('Successfully clicked on the sign in button')
except exceptions as e:
	print(f'Element not found : {e}')
# selecting location & role
time.sleep(5)
try:
	if driver.page_source.__contains__('Location'):
		print("Select Location pop up is displayed.. Please select anyone from the dropdown  ======> ",
		      end='')
		location = Select(driver.find_element(By.TAG_NAME,
		                                      "select"))
		time.sleep(3)
		location.select_by_visible_text("Santa Monica (Official Test)")
		print(f'Selected role as {location.first_selected_option.text}')
		time.sleep(3)
		role = Select(driver.find_element(By.XPATH,
		                                  "//*[text()='Select Role']/following::select"))
		role.select_by_visible_text("Cell Therapy Coordinator")
		print(f'Selected role as {role.first_selected_option.text}')
		go_button = driver.find_element(By.XPATH,
		                                "//button[text()='Go']")
	else:
		print('Pop up is not displayed')
except exceptions as e:
	print(f"Element not found : {e}")

# verifying & clicking on the REGISTER NEW PATIENT & PLACE ORDER button
try:
	print('Clicking on the REGISTER NEW PATIENT & PLACE ORDER button ========> ',
	      end='')
	register_patient_button = driver.find_element(By.XPATH,
	                                              '//*[text()="REGISTER NEW PATIENT & PLACE ORDER"]')
	register_patient_button.click()
	print('Successfully clicked on the REGISTER NEW PATIENT & PLACE ORDER button')
except exceptions as e:
	print(f'Element not found : {e}')

# generating the new patient name
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

# verifying & entering the first name in patient field
try:
	print('Entering the first name in the first name input box ======> ',
	      end='')
	first_name_input = driver.find_element(By.XPATH,
	                                       '//*[text()="First"]/parent::*//input')
	first_name_input.send_keys('Autotest_' + formatted_datetime)
	print('Successfully entered first name in the first name input box')
except exceptions as e:
	print(f'Element not found : {e}')

# verifying & entering the last name in patient field
try:
	print('Entering the last name in the last name input box ======> ',
	      end='')
	last_name_input = driver.find_element(By.XPATH,
	                                      '//*[text()="Last"]/parent::*//input')
	last_name_input.send_keys('cigniti')
	print('Successfully entered last name in the last name input box')
except exceptions as e:
	print(f'Element not found : {e}')

# verifying & entering the date of birth in patient field
try:
	print('Entering the date of birth in the date of birth input box ======> ',
	      end='')
	dob_input = driver.find_element(By.XPATH,
	                                '//*[text()="Patient DOB"]/parent::*//input')
	dob_input.click()
	WebDriverWait(driver,
	              20).until(EC.presence_of_element_located((By.XPATH, "//*[@title='Previous Month']")))
	time.sleep(3)
	year_dropdown = Select(driver.find_element(By.XPATH,
	                                           "//*[text()='Pick a Year']/following::select"))
	year_dropdown.select_by_visible_text(str(random.randint(1970,2020)))
	date = driver.find_element(By.XPATH,
	                           "//*[text()='1']")
	date.click()
	# dob_input.send_keys('Oct 1, 2023')
	print('Successfully entered date of birth in the date of birth input box')
except exceptions as e:
	print(f'Element not found : {e}')

# verifying & clicking the gender(male) in patient field
try:
	print('Clicking on the gender (male) radio button ======> ',
	      end='')
	gender_radio_button = driver.find_element(By.XPATH,
	                                          '//*[text()="Gender"]/parent::*//label/span[1]')
	gender_radio_button.click()
	print('Successfully clicked on the gender (male) radio button')
except exceptions as e:
	print(f'Element not found : {e}')

# get five digit random code
zipcode = random.randint(12121,
                         98989)

# verifying & entering the patient zipcode in patient field
try:
	print('Entering the zip code in the zip code input box ======> ',
	      end='')
	zipcode_input = driver.find_element(By.XPATH,
	                                    '//*[text()="Patient Zip Code"]/parent::*//input')
	zipcode_input.send_keys(zipcode)
	print('Successfully entered the zip code in the zip code input box')
except exceptions as e:
	print(f'Element not found : {e}')

# Selecting the treating physician
try:
	print('Selecting the treating physician in the patient fields =======> ',
	      end='')
	
	treating_physician_el = driver.find_element(By.TAG_NAME,
	                                            'select')
	treating_physician_dropdown = Select(treating_physician_el)
	
	# Iterate through the options and select the one containing 'test'
	time.sleep(5)
	for option in treating_physician_dropdown.options:
		if 'Test' in option.text:
			treating_physician_dropdown.select_by_visible_text(option.text)
			print(f'Successfully selected {option.text} as treating physician')
			break
	else:
		sys.stderr.write('No option containing "Test" found in the dropdown')
except Exception as e:
	print(f'An error occurred: {e}')


# entering the next button
def click_button(button_name,click='yes'):
	try:
		print(f'Clicking on the {button_name} button =======> ',
		      end='')
		button = driver.find_element(By.XPATH,
		                                  f'//button[text()="{button_name}"]')
		WebDriverWait(driver,30,poll_frequency=3).until(EC.visibility_of(button))
		driver.execute_script("arguments[0].scrollIntoView();", button)
		if button.is_displayed():
			if click=="yes":
			    button.click()
			    print(f'Successfully clicked on the {button_name} button')
			else:
				print(f"Successfully verified {button_name} button is existed")
			if button_name=="Reserve Slot":
				delivery_date_input=driver.find_element(By.XPATH, "//*[text()='Delivery Date']/following::input")
				delivery_date=delivery_date_input.get_attribute("value")
				while delivery_date=="":
					time.sleep(2)
					delivery_date=delivery_date_input.get_attribute("value")
			#WebDriverWait(driver,15).until(EC.invisibility_of_element(button))
		else:
			print('Unable to click on next button')
	except exceptions as e:
		print(f'Element not found : {e}')


click_button(button_name='Next')
#get coi number
try:
	print("Verifying the coi number on the Indication page ======> ",end="")
	coi_text=driver.find_element(By.XPATH, "//*[starts-with(text(),'COI:')]")
	WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(text(),'COI:')]")))
	print("Successfully verified coi number is existed on the Indication page")
	click_button(button_name="Next",click=None)
	coi_number = coi_text.text.split(': ')[-1]
	with open("coi_number.txt",
	          "w") as file:
		file.write(coi_number)
	#print(os.environ["coi_number"])
except NoSuchElementException as e:
	print(f"Element not found : {e}")


# selecting the indication melanoma
time.sleep(10)
try:
	WebDriverWait(driver,
	              timeout=50).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'),
	                                                                 'Indication'))
	print('Selecting the indication in the patient fields =======> ',
	      end='')
	
	indicaton = driver.find_element(By.TAG_NAME,
	                                'select')
	indicaton_dropdown = Select(indicaton)
	
	# Iterate through the options and select the one containing 'test'
	time.sleep(5)
	indicaton_dropdown.select_by_visible_text('Melanoma')
	if indicaton_dropdown.first_selected_option.text == 'Melanoma':
		print('Successfully selected melanoma from the indication dropdown')
except exceptions as e:
	print(f'An error occurred: {e}')

# clicking on the next button
click_button(button_name='Next')

# uploading the patient consent form

try:
	print('Clicking on the signed patient consent form =======> ',
	      end='')
	upload_button = driver.find_element(By.ID,
	                                    'PCF')
	WebDriverWait(driver,
	              timeout=15).until(EC.element_to_be_clickable(upload_button))
	upload_button.click()
	print('Successfully clicked on the signed patient consent form =======> ',
	      end='')
	# Locate the file input element (replace 'fileInput' with the actual ID or other attribute of your file input)
	time.sleep(5)
	file_input = driver.find_element(By.XPATH,
	                                 "//*[@type='file']")
	
	WebDriverWait(driver,
	              timeout=15).until(EC.element_to_be_clickable(file_input))
	time.sleep(3)
	file_input.send_keys("C:/Users/e007848/ACCELQAgent/AgentInstances/agent/user_data/TestData/Patient Consent Form.pdf")
	# Specify the full path to the file you want to upload
	# file_path = r'C:\Users\e007848\ACCELQAgent\AgentInstances\agent\user_data\TestData\Patient Consent Form.pdf'
	
	# Use send_keys to set the file path to the file input element
	# file_input.send_keys("C:\\Users\\e007848\\ACCELQAgent\\AgentInstances\\agent\\user_data\\TestData\\Patient Consent Form.pdf")
	'''file_input.click()
	keyboard=Controller()
	keyboard.type("C:\\Users\\e007848\\ACCELQAgent\\AgentInstances\\agent\\user_data\\TestData\\Patient Consent Form.pdf")
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)'''
	driver.find_element(By.XPATH,
	                    '//*[@icon-name="utility:success"]')
	time.sleep(3)
	WebDriverWait(driver,
	              30).until(EC.visibility_of_element_located((By.XPATH,
	                                                          "//*[text()='Done']")))
	done_button = driver.find_element(By.XPATH,
	                                  "//*[text()='Done']")
	done_button.click()
	print('Successfully uploaded patient consent form')
	WebDriverWait(driver,
	              30).until(EC.invisibility_of_element((driver.find_element(By.XPATH,
	                                                                        "//*[text()='Done']"))))
	time.sleep(3)
except exceptions as e:
	print(f'An error occurred: {e}')

click_button(button_name='Next')
# opt out the patient details
try:
	print('Selecting the checkbox, I would like to opt out of all Iovance support options ========> ',
	      end='')
	WebDriverWait(driver,
	              20).until(EC.presence_of_element_located((By.XPATH,
	                                                        '//*[contains(text(),"I would")]/parent::*/span[1]')))
	opt_out_checkbox = driver.find_element(By.XPATH,
	                                       '//*[contains(text(),"I would")]/parent::*/span[1]')
	opt_out_checkbox.click()
	if opt_out_checkbox.is_selected():
		print('Successfully selected the checkbox, I would like to opt out of all Iovance support options')
except exceptions as e:
	print(f'An error occurred: {e}')
click_button(button_name='Next')

# selecting the slot
try:
	valid_dates = driver.find_elements(By.XPATH,
	                                   "//td[@data-is-valid='true']")
	WebDriverWait(driver,
	              20).until(EC.element_to_be_clickable(valid_dates[-1]))
	print("Selecting the slot from the available slots =======>",
	      end='')
	valid_dates[-1].click()
	time.sleep(5)
	print('Successfully selected last slot from the valid dates')
except exceptions as e:
	print(f'An error occurred: {e}')

# selecting the time from the dropddown
try:
	time_input = driver.find_element(By.XPATH,
	                                 "//*[text()='Pick-Up Time']/following::input")
	WebDriverWait(driver,
	              20).until(EC.element_to_be_clickable(time_input))
	driver.execute_script("arguments[0].scrollIntoView();",
	                      time_input)
	time.sleep(2)
	time_input.click()
	time.sleep(1)
	timer = driver.find_element(By.XPATH,
	                           "//span[contains(text(),':0')]")
	timer.click()
except exceptions as e:
	print(f'An error occurred: {e}')


# Selecting the treating physician
try:
	print('Selecting the tumor procuremnet surgeon in the patient fields =======> ',
	      end='')
	
	tumor_procurement_surgeon = driver.find_element(By.TAG_NAME,
	                                                'select')
	tumor_procurement_surgeon_dropdown = Select(tumor_procurement_surgeon)
	
	# Iterate through the options and select the one containing 'test'
	time.sleep(5)
	for option in tumor_procurement_surgeon_dropdown.options:
		if 'Test' in option.text:
			tumor_procurement_surgeon_dropdown.select_by_visible_text(option.text)
			print(f'Successfully selected {option.text} as tumor procurement surgeon')
			break
	else:
		sys.stderr.write("No option containing 'Test' found in the dropdown")
except exceptions as e:
	print(f'An error occurred: {e}')


click_button(button_name="Reserve Slot")
click_button(button_name="Next")
click_button(button_name="Agree")
click_button(button_name="Confirm")
click_button(button_name="Submit TIL Order")


# verify the order request is submitted
try:
	verify_text=driver.find_element(By.XPATH, "//*[text()='YOUR ORDER REQUEST HAS BEEN SUBMITTED']")
	print("Verifying the order request has been submitted =======> ", end="")
	WebDriverWait(driver,15).until(EC.visibility_of(verify_text))
	print("Successfully verified Order request has been submitted ")
except NoSuchElementException as e:
	print(f"Element not found : {e}")
	
	
# clicking on the close button
try:
	close_button=driver.find_element(By.XPATH, "//header/button")
	print("Clicking on the close button  =======> ",end="")
	close_button.click()
	print("Successfully clicked on the close button")
	WebDriverWait(driver,15).until(EC.invisibility_of_element(close_button))
except NoSuchElementException as e:
	print(f"Element not found : {e}")
	
click_button(button_name="Request Pick-Up Reschedule",click=None)
driver.close()

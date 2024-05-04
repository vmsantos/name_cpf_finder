import os
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open a text file to write the results
result_file_name = f"cpf_results_{secrets.token_hex(4)}.txt"
result_file = open(result_file_name, 'w')

# Read CPFs from the text file
with open('good_cpf_results.txt', 'r') as file:
    cpfs = [line.strip() for line in file]

# Reverse the list of CPFs
cpfs.reverse()

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the webpage
initial_url = 'https://contasirregulares.tcu.gov.br/ordsext/f?p=105:21:::NO:::'
driver.get(initial_url)

# Click on the label
label_element = driver.find_element(By.CSS_SELECTOR, 'label[for="P21_FINS_ELEITORAIS_1"]')
label_element.click()

# Counter for checked CPFs
checked_cpfs_count = 0

# Loop through each CPF in reverse order
for cpf in cpfs:
    # Set CPF value using JavaScript
    js_script = f"apex.item('P21_CPF_FE').setValue('{cpf}');"
    driver.execute_script(js_script)
    
    # Submit the form
    js_submit_script = "apex.submit({request:'EMITIR'});"
    driver.execute_script(js_submit_script)
    time.sleep(0.1)  # Adjust the delay as needed
    
    # Check if the result is "BAD"
    if "O CPF digitado está incorreto" in driver.page_source:
        result = f"{cpf}: BAD\n"
    else:
        # Extract full name
        try:
            full_name_element = driver.find_element(By.XPATH, "//div[contains(text(), 'Nome completo:')]/b")
            full_name = full_name_element.text
            result = f"{cpf}: {full_name}\n"
        except Exception as e:
            print(f"Failed to extract full name for CPF {cpf}. Error: {e}")
            result = f"{cpf}: Failed to extract full name\n"
        
        # Check if the full name matches "RODRIGO CRUZ SILVA"
        if full_name.upper() == "JOAO SILVA":
            print(f"Full name '{full_name.upper}' found. Stopping the script.")
            result_file.write(cpf + ' ' + result)
            break
    
    # Write the result to the result file
    result_file.write(cpf + ' ' + result)
    
    # Increment the counter for checked CPFs
    checked_cpfs_count += 1
    
    # Check if 10 CPFs have been checked
    if checked_cpfs_count % 10 == 0:
        print("Results saved for 10 CPFs. Continuing...")
    
    # Go back to the initial URL to check the next CPF
    driver.get(initial_url)

# Close the result file
result_file.close()

# Close the webdriver
driver.quit()

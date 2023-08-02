import re as re
from datetime import time

import pandas as pd

import time

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import subprocess

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

Username = ''

Password = ''

dns1 = ''

domainName = ''



def filter_data():
    data = pd.read_excel('Bowie.xlsx', sheet_name='AV LAN Private')

    filtered_data = data[data['Device ID'].str.contains('NVX', case=False)]

    # Reset the index of the filtered_data DataFrame
    filtered_data = filtered_data.reset_index(drop=True)
    return filtered_data


def initialsetup(initial_ips):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    i = 1
    for x in initial_ips:
        webdriver_path = '/path/to/chromedriver'
        driver.get('http://' + x)

        #setting = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "device_admin")))
        #setting.click()

        advanced = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'details-button')))
        advanced.click()

        link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'proceed-link')))
        link.click()
        time.sleep(1)
        # Find the username and password input fields and enter your credentials
        username_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_userid_inputtext')))
        username_field.send_keys(Username)
        time.sleep(1)
        password_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_password_inputtext')))
        confirm_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_confirmpassword_inputtext')))
        password_field.send_keys(Password)
        confirm_field.send_keys(Password)

        # Submit the login form
        time.sleep(1)
        confirm_field.send_keys(Keys.RETURN)
        time.sleep(3)

        driver.execute_script("window.open('');")

        driver.switch_to.window(driver.window_handles[i])

        i = i + 1
        time.sleep(1)

def webbrowseropen(current_ips):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    i = 1
    for x in current_ips:
        webdriver_path = '/path/to/chromedriver'
        driver.get('http://' + x)

        #setting = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "device_admin")))
        #setting.click()

        advanced = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'details-button')))
        advanced.click()

        link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'proceed-link')))
        link.click()
        time.sleep(1)
        # Find the username and password input fields and enter your credentials
        username_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_userid_inputtext')))
        username_field.send_keys(Username)
        time.sleep(1)
        password_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_password_inputtext')))
        password_field.send_keys(Password)
        # Submit the login form
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        driver.execute_script("window.open('');")

        driver.switch_to.window(driver.window_handles[i])

        i = i + 1
        time.sleep(1)

def setHostAndIP(initial_ips, newIps):
    deviceData = filter_data()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    i = 0
    for x in initial_ips:
        ipFiltered = deviceData[deviceData['IP Address'] == newIps[i]]
        webdriver_path = '/path/to/chromedriver'
        driver.get('http://' + x)

        advanced = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'details-button')))
        advanced.click()

        link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'proceed-link')))
        link.click()
        time.sleep(1)
        # Find the username and password input fields and enter your credentials
        username_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_userid_inputtext')))
        username_field.send_keys(Username)
        time.sleep(1)
        password_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_password_inputtext')))
        password_field.send_keys(Password)
        # Submit the login form
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)
        time.sleep(8)

        settings = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'id_devicesettings')))
        settings.click()
        time.sleep(3)

        dhcpSwitch = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'ne-dhcp-1')))
        dhcpSwitch.click()
        time.sleep(1)

        hostName = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'network-host-name')))
        hostName.clear()
        hostName.send_keys(ipFiltered['Hostname'].iloc[0])
        time.sleep(1)

        domain = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'network-domain')))
        domain.clear()
        domain.send_keys(domainName)
        dns = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'network-primary--static-dns')))
        dns.clear()
        dns.send_keys(dns1)
        deviceIP = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'ne-ip-address-1-disabled')))
        deviceIP.clear()
        deviceIP.send_keys(newIps[i])

        deviceSubnet = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'ne-subnet-mask-1-disabled')))
        deviceSubnet.clear()
        deviceSubnet.send_keys('255.255.255.0')

        deviceRouter = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'ne-def-router-1-disabled')))
        deviceRouter.clear()
        deviceRouter.send_keys('10.220.0.1')


        cloudSwitch = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'isHydrogen-cloudenabled')))
        cloudSwitch.click()
        time.sleep(1)

        updateSwitch = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'autoupdate-enabled')))
        updateSwitch.click()
        time.sleep(1)

        driver.execute_script("window.open('');")

        driver.switch_to.window(driver.window_handles[i+1])

        i = i + 1

def pushUpdates(newIps):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    i = 0
    for x in newIps:
        webdriver_path = '/path/to/chromedriver'
        driver.get('http://' + x)
        advanced = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'details-button')))
        advanced.click()

        link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'proceed-link')))
        link.click()
        time.sleep(1)
        # Find the username and password input fields and enter your credentials
        username_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_userid_inputtext')))
        username_field.send_keys(Username)
        time.sleep(1)
        password_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'cred_password_inputtext')))
        password_field.send_keys(Password)
        # Submit the login form
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        dropDown = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-container-row"]/device-detail/cui-detail/div[1]/div/div/div/div[2]/cui-action-menu/p-splitbutton/div/button[2]')))
        dropDown.click()
        time.sleep(1)
        uploadFirmware = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-container-row"]/device-detail/cui-detail/div[1]/div/div/div/div[2]/cui-action-menu/p-splitbutton/div/div/ul/li[5]/a')))
        uploadFirmware.click()
        time.sleep(2)
        file = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fUplaod_DeviceManagement_Firmware_SelectFile"]/div/div[1]/span/input')))
        file.send_keys('C:/Users/bkamide/Desktop/Firmware/CRESTRON/dm-nvx-ed30-enc_7.1.5259.00059_r504078.zip')
        time.sleep(1)
        loadBtn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fUplaod_DeviceManagement_Firmware_SelectFile"]/div/div[1]/p-button[1]/button')))
        loadBtn.click()
        time.sleep(2)

        driver.execute_script("window.open('');")

        driver.switch_to.window(driver.window_handles[i+1])

        i = i + 1


def getmac(current_ips):
    data = pd.read_excel('Bowie.xlsx')
    for x in current_ips:
        arp_output = subprocess.check_output(['arp', '-a', x])
        arp_output = arp_output.decode('utf-8')
        mac_address = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', arp_output)
        print(f"IP: {x} | MAC: {mac_address.group(0)}")



if __name__ == '__main__':
    initial_ips = ['10.220.0.15', '10.220.0.16', '10.220.0.17', '10.220.0.18', '10.220.0.19', '10.220.0.20', '10.220.0.21', '10.220.0.22']

    newIps = ['10.220.0.82', '10.220.0.83', '10.220.0.80', '10.220.0.81', '10.220.0.86', '10.220.0.87', '10.220.0.88', '10.220.0.89']
    #initialsetup(initial_ips)
    #webbrowseropen(initial_ips)
    #setHostAndIP(initial_ips, newIps)
    webbrowseropen(newIps)
    #getmac(newIps)
    #pushUpdates(newIps)
    #print(filter_data())



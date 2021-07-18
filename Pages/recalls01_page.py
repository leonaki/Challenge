from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Config import config

from Pages.base_page import BasePage


class Recalls01Page(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(config.TestData.recalls01url)

    def get_disclaimer(self):
        return WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div')))

    def get_disclaimer_how_it_works(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/a/strong')))

    def click_disclaimer_how_it_works(self):
        return self.find_element_by_css_selector('#advertising-disclosure > div > div > a').click()

    def get_footer_contactus(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[2]/div/a[1]')))

    def get_footer_faq(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[2]/div/a[2]')))

    def get_footer_terms_of_use(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[2]/div/a[3]')))

    def get_footer_privacy_policy(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[2]/div/a[4]')))

    def get_footer_ca_notice(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[2]/div/a[5]')))

    def get_footer_body(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[1]/p[1]')))

    def get_footer_copyright(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/footer/div[2]/div[1]/p[2]')))

    def get_social_facebook(self):
        return WebDriverWait(self, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrpr"]/div[3]/article/div[2]/a[1]')))

    def get_social_twitter(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrpr"]/div[3]/article/div[2]/a[2]')))

    def get_social_email(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            '#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(3)')))

    def get_social_email_to(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            '#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(3)').get_attribute(
            "href").partition("subject")[0][7:]))

    def set_find_my_match(self, message):
        WebDriverWait(self, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input'))).send_keys(message)

    def get_find_my_match(self):
        return WebDriverWait(self, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input')))

    def get_find_my_match_button(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            '#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(9) > div > form > div.wzrd-wg__form-wpr > button')))

    def click_find_my_match_button(self):
        return WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            '#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(9) > div > form > div.wzrd-wg__form-wpr > button'))).click()

    def click_latest_news_first(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar"]/nav[2]/a[1]/div[1]'))).click()

    def click_latest_news_last(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar"]/nav[2]/a[last()]/div[1]'))).click()

    def click_related_new_stories_first(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar"]/nav[1]/a[1]/div[2]'))).click()

    def click_related_new_stories_last(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar"]/nav[1]/a[last()]/div[2]'))).click()


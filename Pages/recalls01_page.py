from selenium import webdriver
from Config import config

from Pages.base_page import BasePage


class Recalls01Page(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(config.TestData.recalls01url)

    def get_disclaimer(self):
        return self.find_element_by_xpath('/html/body/div[1]/div/div')

    def get_disclaimer_how_it_works(self):
        return self.find_element_by_xpath('/html/body/div[1]/div/div/a/strong')

    def get_footer_body(self):
        return self.find_element_by_xpath('/html/body/footer/div[2]/div[1]/p[1]')

    def get_footer_copyright(self):
        return self.find_element_by_xpath('/html/body/footer/div[2]/div[1]/p[2]')

    def get_social_facebook(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/article/div[2]/a[1]/svg/g/path[2]')

    def click_social_facebook(self):
        self.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(1) > svg').click()

    def get_social_twitter(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/article/div[2]/a[1]/svg/g/path[2]')

    def click_social_twitter(self):
        self.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(2) > svg > g > path.ca-icon__colored-fill-2').click()

    def get_social_email(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/article/div[2]/a[1]/svg/g/path[2]')

    def click_social_email(self):
        self.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(3) > svg').click()

    def set_find_my_match(self, message):
        self.find_element_by_xpath('/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input').send_keys(message)

    def get_find_my_match(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input')

    def get_find_my_match_button(self):
        return self.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(9) > div > form > div.wzrd-wg__form-wpr > button')

    def click_find_my_match_button(self):
        self.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(9) > div > form > div.wzrd-wg__form-wpr > button').click()

    def get_latest_news(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/aside/nav[2]/h3')
        # /html/body/main/div[3]/aside/nav[2]/a[last()]
        # /html/body/main/div[3]/aside/nav[2]/a[8]

    def get_related_new_stories(self):
        return self.find_element_by_xpath('/html/body/main/div[3]/aside/nav[1]/h3')

    def click_latest_news_first(self):
        self.find_element_by_xpath('//*[@id="sidebar"]/nav[2]/a[1]/div[2]').click()

    def click_latest_news_last(self):
        self.find_element_by_xpath('//*[@id="sidebar"]/nav[2]/a[last()]/div[2]').click()

    def click_related_new_stories_first(self):
        self.find_element_by_xpath('//*[@id="sidebar"]/nav[1]/a[1]/div[2]').click()

    def click_related_new_stories_last(self):
        self.find_element_by_xpath('//*[@id="sidebar"]/nav[1]/a[last()]/div[2]').click()


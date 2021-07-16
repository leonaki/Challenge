import pytest
from time import sleep
from selenium.webdriver import Chrome
from Config import config
from Pages.recalls01_page import Recalls01Page
from selenium.common.exceptions import WebDriverException


@pytest.fixture
def browser():
    driver = Chrome(config.TestData.CHROME_PATH)
    #sleep(5)
    yield driver
    sleep(5)
    driver.quit()


def est_verify_disclaimer(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC01 - Verifying the disclaimer text")
    assert config.TestData.disclaimerexpectedtext == Recalls01Page.get_disclaimer(browser).text
    print("Disclaimer text is accurate")


def est_disclaimer_how_it_works(browser):
    print("TC02 - Clicking on disclaimer")
    try:
        Recalls01Page.get_disclaimer_how_it_works.click()
        print("Disclaimer link is working fine")
    except WebDriverException:
        print ("Element is not clickable")


def est_verify_footer_body(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC03 - Verifying the footer body text")
    assert config.TestData.footerexpectedbody == Recalls01Page.get_footer_body(browser).text
    print("Footer body text is accurate")


def test_verify_footer_copyright(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC04 - Verifying the footer copyright text")
    assert config.TestData.footerexpectedcopyright == Recalls01Page.get_footer_copyright(browser).text
    print("Footer copyright text is accurate")


def test_social_facebook(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC05 - Click on Facebook social link")
    try:
        Recalls01Page.click_social_facebook(browser)
        sleep(5)
        print("Facebook link is working fine")
    except WebDriverException:
        print("Element is not clickable")


def test_social_twitter(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC06 - Click on Twitter social link")
    try:
        Recalls01Page.click_social_twitter(browser)
        sleep(5)
        print("Twitter link is working fine")
    except WebDriverException:
        print("Element is not clickable")


def test_social_email(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC07 - Click on Email social link")
    try:
        Recalls01Page.click_social_email(browser)
        sleep(5)
        print("Email link is working fine")
    except WebDriverException:
        print("Element is not clickable")

def test_find_my_match(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC08 - Find my match box")
    Recalls01Page.set_find_my_match(browser,'34744')

    assert Recalls01Page.get_find_my_match(browser)
    try:
        Recalls01Page.click_find_my_match_button(browser)
        sleep(5)
        print("Find my match button is working fine")
    except WebDriverException:
        print("Element is not clickable")


def test_latest_news_first(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC09 - Click on First Latest News")

    try:
        Recalls01Page.click_latest_news_first(browser)
        sleep(5)
        print("First listed Latest News exists")
    except WebDriverException:
        print("Element not found")


def test_latest_news_last(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC10 - Click on Last Latest News")

    try:
        Recalls01Page.click_latest_news_last(browser)
        sleep(5)
        print("Last listed Latest News exists")
    except WebDriverException:
        print("Element not found")


def test_related_new_stories_first(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC11 - Click on First New Stories")

    try:
        Recalls01Page.click_latest_news_first(browser)
        sleep(5)
        print("First listed New Stories exists")
    except WebDriverException:
        print("Element not found")


def test_related_new_stories_last(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC12 - Click on Last New Stories")

    try:
        Recalls01Page.click_latest_news_last(browser)
        sleep(5)
        print("Last listed New Stories exists")
    except WebDriverException:
        print("Element not found")
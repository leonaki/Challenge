import pytest
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from Config import config
from Pages.recalls01_page import Recalls01Page
from selenium.common.exceptions import WebDriverException


@pytest.fixture
def browser():
    driver = Chrome(config.TestData.CHROME_PATH)
    yield driver
    sleep(5)
    driver.quit()


def test_verify_disclaimer(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC01 - Verifying the disclaimer text")
    assert config.TestData.disclaimerexpectedtext == Recalls01Page.get_disclaimer(browser).text, "Incorrect text"
    print("     Disclaimer text is accurate")


def test_disclaimer_how_it_works(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC02 - Clicking on disclaimer")
    try:
        Recalls01Page.click_disclaimer_how_it_works(browser)
        print("     Disclaimer link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_contactus(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC03 - Footer Contact Us")
    sleep(5)
    assert config.TestData.contactusurl == Recalls01Page.get_footer_contactus(browser).get_attribute("href"), "Incorrect URL"
    print("     03.1 - Footer Contact us link is accurate")
    try:
        sleep(5)
        Recalls01Page.get_footer_contactus(browser).click()
        sleep(5)
        print("     03.2 - Footer Contact us link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_faq(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC04 - Footer Faq Us")
    sleep(5)
    assert config.TestData.faqurl == Recalls01Page.get_footer_faq(browser).get_attribute("href"), "Incorrect URL"
    print("     04.1 - Footer Faq link is accurate")
    try:
        sleep(5)
        Recalls01Page.get_footer_faq(browser).click()
        sleep(5)
        print("     04.2 - Footer Faq link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_terms_of_use(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC05 - Footer Terms of Use ")
    sleep(5)
    assert config.TestData.terms_of_useurl == Recalls01Page.get_footer_terms_of_use(browser).get_attribute("href"), "Incorrect URL"
    print("     05.1 - Footer Terms of Use link is accurate")
    try:
        sleep(5)
        Recalls01Page.get_footer_terms_of_use(browser).click()
        sleep(5)
        print("     05.2 - Footer Terms of Use link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_privacy_policy(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC06 - Footer Privacy Policy")
    sleep(5)
    assert config.TestData.privacypolicyurl == Recalls01Page.get_footer_privacy_policy(browser).get_attribute("href"), "Incorrect URL"
    print("     06.1 - Footer Privacy Policy link is accurate")
    try:
        sleep(5)
        Recalls01Page.get_footer_privacy_policy(browser).click()
        sleep(5)
        print("     06.2 - Footer Privacy Policy link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_ca_notice(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC07 - Footer CA Privacy Notice")
    sleep(5)
    assert config.TestData.canoticeurl == Recalls01Page.get_footer_ca_notice(browser).get_attribute("href"), "Incorrect URL"
    print("     07.1 - CA Privacy Notice link is accurate")
    try:
        sleep(5)
        Recalls01Page.get_footer_ca_notice(browser).click()
        sleep(5)
        print("     07.2 - Footer CA Privacy Notice link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_verify_footer_body(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC08 - Verifying the footer body text")
    assert config.TestData.footerexpectedbody == Recalls01Page.get_footer_body(browser).text, "     Not valid footer body text"
    print("     Footer body text is accurate")


def test_verify_footer_copyright(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC09 - Verifying the footer copyright text")
    assert config.TestData.footerexpectedcopyright == Recalls01Page.get_footer_copyright(browser).text, "       Not valid footer copyright text"
    print("     Footer copyright text is accurate")


def test_social_facebook(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC10 - Click on Facebook social link")
    try:
        sleep(5)
        Recalls01Page.get_social_facebook(browser).click()
        sleep(5)
        print("     Facebook link is working fine")
    except WebDriverException:
        print("     Element is not clickable")
        pytest.fail()


def test_social_twitter(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC11 - Click on Twitter social link")
    assert config.TestData.twitterurl in Recalls01Page.get_social_twitter(browser).get_attribute("href"), "Not valid URL"

    try:
        sleep(5)
        Recalls01Page.get_social_twitter(browser).click()
        sleep(5)
        print("     Twitter Social link is working fine")
    except WebDriverException:
        print("Element is not clickable")
        pytest.fail()


def test_social_email(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC12 - Test Email social link")
    try:
        sleep(5)
        Recalls01Page.get_social_email(browser).click()
        sleep(5)
        print("     Email link is working fine")
    except WebDriverException:
        print("Element is not clickable")
        pytest.fail()


def test_find_my_match(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC08 - Find my match box")

    Recalls01Page.set_find_my_match(browser, '34744')

    assert Recalls01Page.get_find_my_match(browser), "Find my match textbox is blank"

    try:
        sleep(5)
        Recalls01Page.get_find_my_match_button(browser).click()
        sleep(5)
        print("Find my match button is working fine")
    except WebDriverException:
        print("Element is not clickable")
        pytest.fail()


def test_latest_news_first(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC13 - Click on First Latest News")

    try:
        sleep(5)
        Recalls01Page.click_latest_news_first(browser)
        sleep(5)
        print("     First listed Latest News exists")
    except WebDriverException:
        print("Element not found")
        pytest.fail()


def test_latest_news_last(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC14 - Click on Last Latest News")

    try:
        sleep(5)
        Recalls01Page.click_latest_news_last(browser)
        sleep(5)
        print("     Last listed Latest News exists")
    except WebDriverException:
        print("Element not found")
        pytest.fail()


def test_related_news_first(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC15 - Click on First Related News")

    try:
        sleep(5)
        Recalls01Page.click_related_new_stories_first(browser)
        sleep(5)
        print("     First listed Related News exists")
    except WebDriverException:
        print("     Element not found")
        pytest.fail("Failed")


def test_related_news_last(browser):
    contact_page = Recalls01Page(browser)
    contact_page.open()
    print("TC16 - Click on Last Related News")

    try:
        sleep(5)
        Recalls01Page.click_related_new_stories_last(browser)
        sleep(5)
        print("     Last listed Related News exists")
    except WebDriverException:
        print("     Element not found")
        pytest.fail("Failed")

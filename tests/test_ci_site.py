# packages import section
import pytest
from requests import get
from playwright.sync_api import Page
from time import sleep

# site page fixture to reuse in tests 
@pytest.fixture()
def home_page(page: Page, url="http://localhost:5000/"):
    
    page.goto(url)
    return page

# test checking if site is available
def test_site_availability(url="http://127.0.0.1:5000/"):
    
   response = get(url)
   assert response.ok

# test if a page loaded for a first time is correct
# welcome page contains <p> with site description
def test_first_load(home_page):

    # get element and check if it's <p>
    element = home_page.query_selector("#quote-figure")
    tag_name = element.evaluate("el => el.tagName.toLowerCase()")
    assert tag_name == "p"

# test checking if a page modified after clicking on a button for the first time
def test_text_change(home_page):

    home_page.click("text=Get A Sci-Fi Quote")
    # wait until blockquote is appeared
    assert home_page.wait_for_selector("blockquote")

# test checking if a new text appears after clicking on the button
# for second time after <blockquote> appeared
# add parameters for test re-run
@pytest.mark.parametrize("execution_number", range(2))
def test_blockquote_text_change(home_page, execution_number):

    home_page.click("text=Get A Sci-Fi Quote")

    # wait until blockquote is appeared and save quote text
    home_page.wait_for_selector("blockquote")
    original_text = home_page.inner_text("#quote-figure")

    # press on the button for second time and compare quotes
    home_page.click("text=Get A Sci-Fi Quote")
    # wait until page is updated
    sleep(5)
    home_page.wait_for_selector("blockquote")
    new_text = home_page.inner_text("#quote-figure")
    assert new_text != original_text

# text checking a welcome page displayed on page reload
def test_page_reload(home_page):

    # check if a page have a <p> tag after page reload
    home_page.click("text=Get A Sci-Fi Quote")

    # check if page is changed and run test on reload
    element = home_page.query_selector("blockquote")
    
    # reload the  page
    home_page.reload()
    sleep(5)
    
    # check if after reload page is back to <p>
    element = home_page.query_selector("#quote-figure")
    tag_name = element.evaluate("el => el.tagName.toLowerCase()")
    assert tag_name == "p"

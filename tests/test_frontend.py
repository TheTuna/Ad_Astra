# packages import section
import pytest
from playwright.sync_api import Page
from time import sleep
from app import app as ci_app

@pytest.fixture(scope="session")
def app():
    app = ci_app
    app.config.update({
        "TESTING": True,
    })

    yield app

# test checking welcome page is correct
def test_first_load(page: Page, live_server):

    page.goto(live_server.url())
    # get element and check if it's <p>
    element = page.query_selector("#quote-figure")
    tag_name = element.evaluate("el => el.tagName.toLowerCase()")
    assert tag_name == "p"

# test checking if a page modified after clicking on a button for the first time
def test_text_change(page: Page, live_server):

    page.goto(live_server.url())
    page.click("text=Get A Sci-Fi Quote")
    # wait until blockquote is appeared
    assert page.wait_for_selector("blockquote")

# test checking if a new text appears after clicking on the button
# for second time after <blockquote> appeared
# add parameters for test re-run
@pytest.mark.parametrize("execution_number", range(2))
def test_blockquote_text_change(page: Page, live_server, execution_number):

    page.goto(live_server.url())
    page.click("text=Get A Sci-Fi Quote")

    # wait until blockquote is appeared and save quote text
    page.wait_for_selector("blockquote")
    original_text = page.inner_text("#quote-figure")

    # press on the button for second time and compare quotes
    page.click("text=Get A Sci-Fi Quote")
    # wait until page is updated
    sleep(5)
    page.wait_for_selector("blockquote")
    new_text = page.inner_text("#quote-figure")
    assert new_text != original_text

# text checking a welcome page displayed on page reload
def test_page_reload(page: Page, live_server):

    page.goto(live_server.url())
    # check if a page have a <p> tag after page reload
    page.click("text=Get A Sci-Fi Quote")

    # check if page is changed and run test on reload
    element = page.query_selector("blockquote")
    
    # reload the  page
    page.reload()
    sleep(5)
    
    # check if after reload page is back to <p>
    element = page.query_selector("#quote-figure")
    tag_name = element.evaluate("el => el.tagName.toLowerCase()")
    assert tag_name == "p"

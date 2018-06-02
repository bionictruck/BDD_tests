from selenium import webdriver
# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture


@fixture
def browser_driver(context):
	# -- To run locally
	# context.driver = webdriver.Firefox()

	# this is how you set up a test to run on Sauce Labs
	desired_cap = {
    	'platform': "Mac OS X 10.9",
    	'browserName': "chrome",
    	'version': "31",
}
	context.driver = webdriver.Remote(
    	command_executor='http://jaytrommer:94ff2bf5-5909-4d6b-982a-060448b382bd@ondemand.saucelabs.com:80/wd/hub',
    	desired_capabilities=desired_cap)

def before_feature(context, feature):
	use_fixture(browser_driver, context)

def after_feature(context, feature):
	context.driver.quit()
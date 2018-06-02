# -- FILE: features/steps/profile_steps.py
from behave import given, when, then, step

@given("I am on my profile page")
def step_impl(context):
	context.driver.current_url = "https://www.coursera.org/account-profile"

@when("I am on my profile page")
def step_impl(context):
	context.driver.get("https://www.coursera.org/account-profile")

@when("I enter a <name>")
def step_impl(context):
	for row in context.table:
		context.driver.find_element_by_name("full_name").send_keys('<name>')

@when("I click the Save button")
def step_impl(context):
	context.driver.find_element_by_id("541").click()

@then("I can see my <name> has been saved")
def step_impl(context):
	context.driver.find_element_by_xpath("//*[text()='<name>']")


@then("I can edit my profile")
def step_impl(context):
	context.driver.find_element_by_xpath("//*[text()='Edit my profile']")
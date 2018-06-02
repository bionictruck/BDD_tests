# -- FILE: features/steps/my_course_steps.py
from behave import given, when, then, step

@given('I am on coursera.org')
def step_impl(context):
    context.driver.get("http://www.coursera.org")

@when('I click the Log In link')
def step_impl(context):
	context.driver.find_element_by_link_text("Log In").click()

@when("I enter my email into the Email field")
def step_impl(context):
	context.driver.find_element_by_name("email").send_keys('jaytrommer@outlook.com')

@when("I enter my password into the Password field")
def step_impl(context):
	context.driver.find_element_by_name("password").send_keys('Kar3n_2006!')

@when("I click the Log In button")
def step_impl(context):
	context.driver.find_element_by_css_selector("#authentication-box-content > div > div.Box_120drhm-o_O-displayflex_poyjc-o_O-columnDirection_ia4371.AuthenticationModalContentV1 > div > div.Box_120drhm-o_O-displayflex_poyjc-o_O-columnDirection_ia4371.rc-LoginForm > form > div.Box_120drhm-o_O-displayflex_poyjc-o_O-columnDirection_ia4371.w-100 > button > span").click()

@then("I am shown My Courses")
def step_impl(context):
	context.driver.implicitly_wait(2)
	context.driver.find_element_by_xpath("//*[text()='Last Active']")

@when("I click Inactive Courses")
def step_imp(context):
	context.driver.find_element_by_link_text("Inactive Courses").click()

@when("I click Completed Courses")
def step_impl(context):
	context.driver.find_element_by_link_text("Completed Courses").click()

@when("I click Accomplishments")
def step_impl(context):
	context.driver.find_element_by_link_text("Accomplishments").click()

@when("I click Updates")
def step_impl(context):
	context.driver.find_element_by_link_text("Updates").click()

@when("I click Learning Paths")
def step_impl(context):
	context.driver.find_element_by_link_text("Learning Paths").click()

@then("I see Constitutional Law")
def step_imp(context):
	context.driver.find_element_by_xpath("//*[text()='Constitutional Law']")

@then("I see Programming for Everybody (Python)")
def step_impl(context):
	context.driver.find_element_by_xpath("//*[text()='Programming for Everybody (Python)']")

@then("I see ID Verification")
def step_impl(context):
	context.driver.implicitly_wait(2)
	context.driver.find_element_by_xpath("//*[text()='ID Verification']")

@then("I see Free trials offered now")
def step_impl(context):
	context.driver.find_element_by_xpath("//*[text()='Free trials offered now']")

@then("I see Looking for the perfect course? We're here to help.")
def step_impl(context):
	context.driver.find_element_by_xpath("//*[text()='Get a Learning Path']")
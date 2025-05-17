from src.sel.login_page import LoginPage


def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.execute_login("laczo.bettina+guiteszt@rubin.hu", "Autom@t@t3st2k23")
    # dashboard_page = DashboardPage(driver)
    # assert dashboard_page.actual_heading() == "Dashboard", "Heading is different"

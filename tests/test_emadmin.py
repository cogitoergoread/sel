from tests.empages.login_page import LoginPage


def test_login_functionality(chrome_browser):
    """
    Test the login functionality of the EM2
    """
    url = 'https://em2-teszt.rubin.hu/'
    login_page = LoginPage(chrome_browser)

    # Open Page
    login_page.open_page(url)

    # Enter Username and Password
    login_page.enter_username("laczo.bettina+guiteszt@rubin.hu")
    login_page.enter_password("Autom@t@t3st2k23")

    # Click Login
    login_page.click_login()

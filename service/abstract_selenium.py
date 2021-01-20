import time
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from config.url import urls
from config.elements import elements
from config.user import user


class AbstractSelenium:
    def __init__(self, hidden):
        self.__hidden = hidden
        self.__init_browser(self.__hidden)
        self.__current_url = None

    def __init_browser(self, hidden):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.browser = webdriver.Firefox(firefox_options=firefox_options) if hidden else webdriver.Firefox()
        self.browser.get(urls['login'])

    def __login(self):
        print("Autenticando usuario...")
        self.browser.find_element_by_xpath(elements['login_page']['input_email']).send_keys(user['email'])
        self.browser.find_element_by_xpath(elements['login_page']['btn_continue']).click()
        self.browser.find_element_by_xpath(elements['login_page']['input_password']).send_keys(user['password'])
        self.browser.find_element_by_xpath(elements['login_page']['btn_login']).click()

    def __is_authenticated(self):
        try:
            print(self.browser.find_element_by_xpath(elements['header_confirm']).text)
            return True
        except NoSuchElementException:
            print("Usuário não autenticado")

    def __buy_with_one_click(self, index):
        try:
            self.browser.find_element_by_xpath(elements['bnt_buy_one_click'].format(str(index))).click()
        except NoSuchElementException:
            return False
        return True

    def __bought(self):
        try:
            print(self.browser.find_element_by_xpath(elements['if_bought']).text)
        except NoSuchElementException:
            try:
                print(self.browser.find_element_by_xpath(elements['confirm_bought']).text)
            except NoSuchElementException:
                return False
        return True

    def __confirm_bought(self):
        print(self.browser.find_element_by_xpath(elements['name_ebook']).text,
              self.browser.find_element_by_xpath(elements['confirm_message']).text)

    def __enter_and_buy(self, index):
        try:
            self.browser.find_element_by_xpath(elements['title_ebook'].format(str(index))).click()
        except ElementNotInteractableException:
            self.browser.find_element_by_xpath(elements['img_ebook'].format(str(index))).click()
        if self.__bought():
            pass
        else:
            self.browser.find_element_by_id(elements['btn_buy']).click()
            self.__confirm_bought()

    def start_process(self):
        attempts = 0
        while attempts < 3:
            self.__login()
            if self.__is_authenticated():
                attempts = 3
                self.browser.get(urls['all_ebooks'])
                pages = 0
                while pages < 400:
                    self.__current_url = self.browser.current_url
                    try:
                        for i in range(1, 17):
                            title = self.browser.find_element_by_xpath(elements['title_ebook'].format(str(i)))
                            print("\n\nComprando '" + title.text + "'")
                            if self.__buy_with_one_click(i):
                                if self.__bought():
                                    pass
                                else:
                                    self.__confirm_bought()
                            else:
                                self.__enter_and_buy(i)
                            self.browser.get(self.__current_url)
                        pages += 1
                        self.browser.find_element_by_class_name(elements['btn_next_page']).click()
                        print("\nSaindo da pagina {0}".format(str(pages)) + "\n")
                    except Exception as error:
                        print("\nOcorreu um erro inesperado com o navegador, reiniciando da ultima pagina em 1 minuto... ")
                        self.browser.quit()
                        time.sleep(60)
                        self.__init_browser(self.__hidden)
                        self.__login()
                        self.browser.get(self.__current_url)
            else:
                self.browser.get(urls['login'])
            attempts += 1

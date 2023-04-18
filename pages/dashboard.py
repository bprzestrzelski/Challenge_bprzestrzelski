import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    main_paige_button_xpath = "//div/ul[1]//div[1][@role='button']"
    players_button_xpath = "//div/ul[1]//div[2][@role='button']"
    language_button_xpath = "//div/ul[2]//div[1][@role='button']"
    sign_out_button_xpath = "//div/ul[2]//div[2][@role='button']"
    add_player_button_xpath = "//main/div[3]/div[2]//a"
    dev_team_contact_xpath = "//main/div[3]//a[1][contains(@class, 'MuiButtonBase-root')]"
    last_created_player_xpath = "//main/div[3]/div[3]//a[1]"
    last_updated_player_xpath = "//main/div[3]/div[3]//a[2]"
    last_created_match_xpath = "//main/div[3]/div[3]//a[3]"
    last_updated_match_xpath = "//main/div[3]/div[3]//a[4]"
    last_updated_report_xpath = "//main/div[3]/div[3]//a[5]"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def move_to_add_player(self, click_add):
        time.sleep(5)
        self.click_on_the_element(self.add_player_button_xpath)

from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    expected_title = "Add player"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

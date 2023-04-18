from pages.base_page import BasePage


class Match_Form(BasePage):
    main_page_button_xpath = "//ul[1]/div[@role='button'][1]"
    players_button_xpath = "//ul[1]/div[@role='button'][2]"
    current_player_button_xpath = "//ul[2]/div[@role='button'][1]"
    matches_button_xpath = "//ul[2]/div[@role='button'][2]"
    reports_button_xpath = "//ul[2]/div[@role='button'][3]"
    language_button_xpath = "//ul[3]/div[@role='button'][1]"
    sign_out_button_xpath = "//ul[3]/div[@role='button'][2]"
    date_input_xpath = "//*[@name='date']"
    number_input_xpath = "//*[@name='number']"
    tshirt_color_input_xpath = "//*[@name='tshirt']"

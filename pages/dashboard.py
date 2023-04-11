from pages.base_page import BasePage


class Dashboard(BasePage):
    main_paige_button_xpath = //div/ul[1]//div[1][@role="button"]
    players_button_xpath = //div/ul[1]//div[2][@role="button"]
    language_button_xpath = //div/ul[2]//div[1][@role="button"]
    sign_out_button_xpath = //div/ul[2]//div[2][@role="button"]
    add_player_button_hyperlink = //main/div[3]/div[2]//a
    dev_team_contact_hyperlink_xpath = //main/div[3]//a[1][contains(@class, "MuiButtonBase-root")]
    last_created_player_hyperlink_xpath = //main/div[3]/div[3]//a[1]
    last_updated_player_hyperlink_xpath = //main/div[3]/div[3]//a[2]
    last_created_match_hyperlink_xpath = //main/div[3]/div[3]//a[3]
    last_updated_match_hyperlink_xpath = //main/div[3]/div[3]//a[4]
    last_updated_report_hyperlink_xpath = //main/div[3]/div[3]//a[5]
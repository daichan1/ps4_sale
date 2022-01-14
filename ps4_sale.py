from modules import search_setting
from modules import scraping
from modules import search

print('セール中のゲームタイトルを検索します')

search_game_title = search_setting.set_search_game_title()
search_price = search_setting.set_search_price()
search_range = search_setting.set_search_range(search_price)

game_data = scraping.run()

display_games = search.search_title(game_data, search_game_title)
display_games = search.search_price(display_games, search_price, search_range)

search.value_check(display_games)

search.display_game_list(display_games)
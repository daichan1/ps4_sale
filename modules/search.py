def search_title(game_data, game_title):
  display_games = []
  for game in game_data:
    if game_title in game['title']:
      display_games.append(game)
  return display_games

def search_price(game_data, price, search_range):
  display_games = []
  for i, game in enumerate(game_data):
    if search_range == '1' and price <= game['price']:
      display_games.append(game)
    elif search_range == '2' and price >= game['price']:
      display_games.append(game)
  return display_games

def value_check(game_data):
  if not game_data:
    print('検索条件に合致するゲームは見つかりませんでした')

def display_game_list(game_data):
  for display_game in game_data:
    print(display_game['title'] + ' ' + str(display_game['price']) + '円')
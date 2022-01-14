def set_search_game_title():
  print('検索したいゲームを入力してください', end=':')
  search_game_title = input() 
  return search_game_title

def set_search_price():
  print('検索したい価格を入力してください', end=':')
  try:
    search_price = int(input())
  except ValueError:
    search_price = 0
  return search_price

def set_search_range(search_price):
  search_range = '0'
  if not search_price == 0:
    print('入力した価格より上か下か、どちらかで検索しますか？(1:上、2:下)', end=':')
    search_range = input()
    while search_range not in ['1', '2']:
      print('半角の1か2で入力してください', end=':')
      search_range = input()
  return search_range
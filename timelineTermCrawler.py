from credentials import *
import tweepy
from pandas import DataFrame
from datetime import date
import os
# Api limitada aos últimos 3000 tweets

os = os
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Criar pastas baseada na data e hora
date = date.today()
area = 'universidades'

# Lista de usuários
userList = [
  'unb_oficial', # (Universidade de Brasília)
  'UFPBoficial', # (Universidade Federal da Paraíba)
  'ufgdoficial', # (Universidade Federal da Grande Dourados)
  'ufg_oficial', # (Universidade Federal de Goiás)
  'UFMT',        # (Universidade Federal de Mato Grosso)'
  'ufmsbr',       # (Universidade Federal de Mato Grosso do Sul)

  ]
# Lista de termos
text_query = ['covid', 'pandemia', 'sars', 'corona']

#  Criar pastas se elas não existirem ainda
if os.path.exists(f'./basesDeDados/{date}') == False:
  os.mkdir(f'./basesDeDados/{date}')

if os.path.exists(f'./basesDeDados/{date}/{area}/') == False:
  os.mkdir(f'./basesDeDados/{date}/{area}/')

# Passar por todos os usuários
for userID in userList:

  # Se o arquivo já existe e foi feito hoje, pular
  if os.path.isfile(f'./basesDeDados/{date}/{area}/{userID}_tweets.csv'):
    print(f'{userID}_tweets.csv já existe, indo para o próximo perfil:')
    continue

  # Caso não exista, criar o arquivo
  tweets = api.user_timeline(
    screen_name=userID, 
    # 200 é o valor máximo da conta
    count=200,
    include_rts = False,
    # Extender os tweets além de 140 caractéres
    tweet_mode = 'extended'
    )

  all_tweets = []
  all_tweets.extend(tweets)
  oldest_id = tweets[-1].id
  tweet_term_list = []

  print(len(tweet_term_list))
  # A tweet_term_list não está esvaziando
  while True:
      tweets = api.user_timeline(
          screen_name=userID, 
          count=200,
          include_rts = False,
          max_id = oldest_id - 1,
          tweet_mode = 'extended'
        )

      # Quebrar o loop se acabarem os tweets
      if len(tweets) == 0:
        break

      oldest_id = tweets[-1].id
      all_tweets.extend(tweets)
      print(f'Numero de tweets analisados do perfil @{userID}: {len(all_tweets)}')

  # Pegar todos os tweets com os termos:
  for tweet in all_tweets:
    i = 0
    while i < len(text_query):
      # Se o tweet tiver os termos, adicionar
      if tweet.full_text.find(text_query[i]) != -1:
        tweet_term_list.append(tweet)
      i += 1

  print(f'Numero de tweets com o termos {text_query}: {len(tweet_term_list)}')

  # Filtra tweets duplicados
  # Sempre corta exatamente a metade dos tweets, algo parece errado
  for tweet in tweet_term_list:
    i = 0
    while i < len(tweet_term_list):
      # retornar a posição, se a posição existir, deve ser retirado
      if tweet.id_str.find(tweet_term_list[i].id_str) != -1:
        tweet_term_list.remove(tweet_term_list[i])
      i += 1

  print(f'Numero de tweets não duplicados: {len(tweet_term_list)}')

  outtweets = [
    [tweet.id_str, 
    tweet.created_at, 
    tweet.favorite_count, 
    tweet.retweet_count, 
    tweet.full_text.encode("utf-8").decode("utf-8")] 
    for idx,tweet in enumerate(tweet_term_list)
    ]
  df = DataFrame(outtweets,columns=["id","postado_em:","numero_de_favoritos","numero_de_retweets", "texto"])
  df.to_csv(f'./basesDeDados/{date}/{area}/{userID}_tweets.csv',index=False)
  df.head(3)
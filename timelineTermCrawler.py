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
  'unb_oficial',    # (Universidade de Brasília)
  'UFPBoficial',    # (Universidade Federal da Paraíba)
  'ufgdoficial',    # (Universidade Federal da Grande Dourados)
  'ufg_oficial',    # (Universidade Federal de Goiás)
  'UFMT',           # (Universidade Federal de Mato Grosso)'
  'ufmsbr',         # (Universidade Federal de Mato Grosso do Sul)
  'ufcatoficial',   # (Universidade Federal de Catalão)'
  'ufj_oficial',    # (Universidade Federal de Jataí)'
  'ufbaempauta',    # (Universidade Federal da Bahia)'
  'UFSB_OFICIAL',   # (Universidade Federal do Sul da Bahia)
  'ufrb',           # (Universidade Federal do Recôncavo da Bahia)
  'unilabbrasil',   # (Universidade Federal da Lusofonia Afro-Brasileira)
  'UfalOficial',    # (Universidade Federal de Alagoas)
  'UFCG',           # (Universidade Federal de Campina Grande)
  'AscomUFPE',      # (Universidade Federal de Pernambuco)
  'ufsoficial',     # (Universidade Federal de Sergipe)
  'UFCinforma ',    # (Universidade Federal do Ceará)
  'UFMAoficial',    # (Universidade Federal do Maranhão)
  'ufpioficial',    # (Universidade Federal do Piauí)
  'ufrnbr',         # (Universidade Federal do Rio Grande do Norte)
  '_univasf',       # (Universidade Federal do Vale do São Francisco)
  'UFRPEOnline',    #  (Universidade Federal Rural de Pernambuco)
  'ufersa',         # (Universidade Federal Rural do Semi-Árido)
  'ascomUNIR',      # (Universidade Federal de Rondônia)
  'UFRROficial',    # (Universidade Federal de Roraima)
  'ufac_oficial',   # (Universidade Federal do Acre)
  'unifapoficial',  # (Universidade Federal do Amapá)
  'UFAM_',          # (Universidade Federal do Amazonas)
  'ufopa',          # (Universidade Federal do Oeste do Pará)
  'UFPA_Oficial',   # (Universidade Federal do Pará)
  'UFToficial',     # (Universidade Federal do Tocantins)
  'UfraOficial',    # (Universidade Federal Rural da Amazônia)
  'unifesspa',      # (Universidade Federal do Sul e Sudeste do Pará)
  'unifalmgOFICIAL',# (Universidade Federal de Alfenas)
  'unifei_oficial', # (Universidade Federal de Itajubá)
  'UFJF_',          # (Universidade Federal de Juiz de Fora)
  'uflabr',         # (Universidade Federal de Lavras)
  'ufmg',           # (Universidade Federal de Minas Gerais)
  'UFOP',           # (Universidade Federal de Ouro Preto)
  'ufscaroficial',  # (Universidade Federal de São Carlos)
  'ufsjbr',         # (Universidade Federal de São João del-Rei)
  'unifesp',        # (Universidade Federal de São Paulo)
  'UFU_Oficial',    # (Universidade Federal de Uberlândia)
  'ufvbr',          # (Universidade Federal de Viçosa)
  'ufabc',          # (Universidade Federal do ABC)
  'ufesoficial',    # (Universidade Federal do Espírito Santo)
  'UNIRIO_Oficial', # (Universidade Federal do Estado do Rio de Janeiro)
  'ufrj',           # (Universidade Federal do Rio de Janeiro)
  'uftmsocial',     # (Universidade Federal do Triângulo Mineiro)
  'uftmsocial',     # (Universidade Federal dos Vales do Jequitinhonha e Mucuri)
  'uff_br',         # (Universidade Federal Fluminense)
  'ufrrjbr',        # (Universidade Federal Rural do Rio de Janeiro)
  'UTFPR_',         # (Universidade Tecnológica Federal do Paraná)
  'uffsonline',     # (Universidade Federal da Fronteira Sul)
  'unila',          # (Universidade Federal da Integração Latino-Americana)
  'UFCSPA',         # (Universidade Federal de Ciências da Saúde de Porto Alegre)
  'UFPel',          # (Universidade Federal de Pelotas)
  'UFSC',           # (Universidade Federal de Santa Catarina)
  'UFSM_oficial',   # (Universidade Federal de Santa Maria)
  'UnipampaOficial',# (Universidade Federal do Pampa)
  'UFPR',           # (Universidade Federal do Paraná)
  'FURG',           # (Universidade Federal do Rio Grande)
  'ufrgsnoticias',  # (Universidade Federal do Rio Grande do Sul)
  'UFAPE_oficial',  # (Universidade Federal do Agreste de Pernambuco)
  'UFDPar',         # (Universidade Federal do Delta do Parnaíba)
  'UFToficial',     # (Universidade Federal do Norte do Tocantins)
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

  # Caso o perfil não possua tweets, pular para a próxima conta
  if len(tweets) != 0:
    oldest_id = tweets[-1].id
  else:
    print(f"O perfil @{userID} não possui nenhum tweet")
    continue

  tweet_term_list = []

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
      # Se o tweet tiver os termos
      if tweet.full_text.find(text_query[i]) != -1:
          # Filtra tweets duplicados
          # Se a lista for menor que 0, adicionar
          if len(tweet_term_list) == 0:
            tweet_term_list.append(tweet)
          # Se for maior, adicione se o id for diferente do id anterior
          # Evita tweets duplicados
          elif tweet.id_str != tweet_term_list[len(tweet_term_list) -1].id_str:
            tweet_term_list.append(tweet)
          # Se o tweet for duplicado, não adicione
          else:
            print("Tweet duplicado")
      i += 1

  print(f'Numero de tweets com o termos {text_query}: {len(tweet_term_list)}')

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
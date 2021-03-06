from credentials import *
import tweepy
from pandas import DataFrame
from datetime import date
import os

os = os
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Criar pastas baseada na data e hora
date = date.today()
area = 'cientificos'
# Lista de termos
# text_query = ['covid', 'pandemia', 'sars', 'corona']
text_query = ['cloroquina', 'hidroxicloroquina', 'Azitromicina']

# Lista de Científicos (Universidades federais + figuras importantes)
user_list = [
#   'usponline',        # (Universidade de São Paulo)
#   'Unesp_Oficial',    # (Universidade Estadual Paulista)
#   'unicampoficial',   # (Universidade Estadual de Campinas)
#   'oficialUEM',       # (Universidade Estadual de Maringá)
#   'unb_oficial',      # (Universidade de Brasília)
#   'UFPBoficial',      # (Universidade Federal da Paraíba)
#   'ufgdoficial',      # (Universidade Federal da Grande Dourados)
#   'ufg_oficial',      # (Universidade Federal de Goiás)
#   'UFMT',             # (Universidade Federal de Mato Grosso)'
#   'ufmsbr',           # (Universidade Federal de Mato Grosso do Sul)
#   'ufcatoficial',     # (Universidade Federal de Catalão)'
#   'ufj_oficial',      # (Universidade Federal de Jataí)'
#   'ufbaempauta',      # (Universidade Federal da Bahia)'
#   'UFSB_OFICIAL',     # (Universidade Federal do Sul da Bahia)
#   'ufrb',             # (Universidade Federal do Recôncavo da Bahia)
#   'unilabbrasil',     # (Universidade Federal da Lusofonia Afro-Brasileira)
#   'UfalOficial',      # (Universidade Federal de Alagoas)
#   'UFCG',             # (Universidade Federal de Campina Grande)
#   'AscomUFPE',        # (Universidade Federal de Pernambuco)
#   'ufsoficial',       # (Universidade Federal de Sergipe)
#   'UFCinforma ',      # (Universidade Federal do Ceará)
#   'UFMAoficial',      # (Universidade Federal do Maranhão)
#   'ufpioficial',      # (Universidade Federal do Piauí)
#   'ufrnbr',           # (Universidade Federal do Rio Grande do Norte)
#   '_univasf',         # (Universidade Federal do Vale do São Francisco)
#   'UFRPEOnline',      #  (Universidade Federal Rural de Pernambuco)
#   'ufersa',           # (Universidade Federal Rural do Semi-Árido)
#   'ascomUNIR',        # (Universidade Federal de Rondônia)
#   'UFRROficial',      # (Universidade Federal de Roraima)
#   'ufac_oficial',     # (Universidade Federal do Acre)
#   'unifapoficial',    # (Universidade Federal do Amapá)
#   'UFAM_',            # (Universidade Federal do Amazonas)
#   'ufopa',            # (Universidade Federal do Oeste do Pará)
#   'UFPA_Oficial',     # (Universidade Federal do Pará)
#   'UFToficial',       # (Universidade Federal do Tocantins)
#   'UfraOficial',      # (Universidade Federal Rural da Amazônia)
#   'unifesspa',        # (Universidade Federal do Sul e Sudeste do Pará)
#   'unifalmgOFICIAL',  # (Universidade Federal de Alfenas)
#   'unifei_oficial',   # (Universidade Federal de Itajubá)
#   'UFJF_',            # (Universidade Federal de Juiz de Fora)
#   'uflabr',           # (Universidade Federal de Lavras)
#   'ufmg',             # (Universidade Federal de Minas Gerais)
#   'UFOP',             # (Universidade Federal de Ouro Preto)
#   'ufscaroficial',    # (Universidade Federal de São Carlos)
#   'ufsjbr',           # (Universidade Federal de São João del-Rei)
#   'unifesp',          # (Universidade Federal de São Paulo)
#   'UFU_Oficial',      # (Universidade Federal de Uberlândia)
#   'ufvbr',            # (Universidade Federal de Viçosa)
#   'ufabc',            # (Universidade Federal do ABC)
#   'ufesoficial',      # (Universidade Federal do Espírito Santo)
#   'UNIRIO_Oficial',   # (Universidade do Estado do Rio de Janeiro)
#   'ufrj',             # (Universidade Federal do Rio de Janeiro)
#   'uftmsocial',       # (Universidade Federal do Triângulo Mineiro)
#   'uftmsocial',       # (Universidade Federal dos Vales do Jequitinhonha e Mucuri)
#   'uff_br',           # (Universidade Federal Fluminense)
#   'ufrrjbr',          # (Universidade Federal Rural do Rio de Janeiro)
#   'UTFPR_',           # (Universidade Tecnológica Federal do Paraná)
#   'uffsonline',       # (Universidade Federal da Fronteira Sul)
#   'unila',            # (Universidade Federal da Integração Latino-Americana)
#   'UFCSPA',           # (Universidade Federal de Ciências da Saúde de Porto Alegre)
#   'UFPel',            # (Universidade Federal de Pelotas)
#   'UFSC',             # (Universidade Federal de Santa Catarina)
#   'UFSM_oficial',     # (Universidade Federal de Santa Maria)
#   'UnipampaOficial',  # (Universidade Federal do Pampa)
#   'UFPR',             # (Universidade Federal do Paraná)
#   'FURG',             # (Universidade Federal do Rio Grande)
#   'ufrgsnoticias',    # (Universidade Federal do Rio Grande do Sul)
#   'UFAPE_oficial',    # (Universidade Federal do Agreste de Pernambuco)
#   'UFDPar',           # (Universidade Federal do Delta do Parnaíba)
#   'UFToficial',       # (Universidade Federal do Norte do Tocantins)
#   'minsaude',         # Ministério da saúde
#   'oatila',           # Atila Iamarino (Cientista famoso no covid no brasil)
#   'fiocruz',          # Fundação Oswaldo Cruz (Ministério da Saúde)
#   'butantanoficial'  # Perfil do Insitituto Butantam
]

# # Lista de oposição (líderes de oposição + politicos dos partidos:
# pt, pcdob, psol, psol, pdt)
# user_list = [
#   'cirogomes',        # Ex-candidato a presidência do país
#   'dilmabr',          # Ex-Presidente do país (PT)
#   'GuilhermeBoulos',  # Coordenação Nacional do Movimento dos Trabalhadores Sem Teto (MTST)
#   'Haddad_Fernando',  # Ex-candidato a presidência do país, (PT)
#   'LulaOficial',      # Ex-Presidente do país, (PT)
#   'MarceloFreixo',    # Presidente da Comissão de Defesa dos Direitos Humanos, (PSOL)
#   'fatimabezerra',    # Governadora do Rio Grande do Norte (PT)
#   'FlavioDino',       # Governador do Maranhão (PCdoB)
#   'waldezoficial',    # Governador do estado de Amapá (PDT)
#   'costa_rui',        # Governador da Bahia (PT)
#   'CamiloSantanaCE',  # Governador do Ceará (PT)
#   'Casagrande_ES',    # Governador do Espírito Santo (PSB)
#   'joaoazevedolins',  # Governador da Paraíba (PPS/Cidadania) FALAR COM ORIENTADOR
#   'PauloCamara40',    # Governador de Pernambuco (PSB) FALAR COM ORIENTADOR
#   'wdiaspi',          # Governador do Piaui (PT)
#   'maurocarlesse'     # Governador de Tocantins (PV) FALAR COM ORIENTADOR
# ]

# Lista de líderes religiosos
# user_list = [
#   'PastorMalafaia', # Líder da Igreja Mundial do Reino de Deus
#   'apvaldemiro',    # Líder da Igreja Mundial do Poder de Deus
#   'BispoMacedo',    # Líder da Igreja Universal
#   'peFabiodemelo',  # Padre católico/cantor
#   'pemarcelorossi', # Líder católico
#   'MCrivella',      # Pastor e prefeito do Rio de Janeiro
#   'marcofeliciano', # Pastor e deputado federal de São Paulo
#   'padremanzotti',  # Padre famoso
# ]

# Lista de situacao (resto dos partidos)
user_list = [
  # 'jairBolsonaro',  # Atual presidente do país
  # 'RodrigoMaia',      # Presidente da câmara dos deputados (Democratas)
  # 'wilsonwitzel',     # Governador do Rio de Janeiro (PSC)
  # 'RenanFilho_',      # Governador de Alagoas (MDB)
  # 'wilsonlimaAM',     # Governador do estado de Amazonas (PSC)
  # 'IbaneisOficial',   # Governador do Distrito Federal (MDB)
  # 'ronaldocaiado',    # Governador de Goiás (DEM)
  # 'Reinaldo45psdb',   # Governador do Mato Grosso do Sul (PSDB)
  # 'RomeuZema',        # Governador de Minas Gerais (NOVO)
  # 'helderbarbalho',   # Governador do Pará (MDB)
  # 'ratinho_jr',       # Governador do Paraná (PSD)
  # 'EduardoLeite_',    # Governador do Rio Grande do Sul (PSDB)
  # 'antoniodenarium',  # Governador de Roraima (Indepedente)
  # 'CarlosMoises',     # Governador de Santa Catarina (PSL)
  # 'belivaldochagas',  # Governador de Sergipe (PSD)
  # 'jdoriajr'          # Governador de São Paulo (PSDB)
]

#  Criar pastas se elas não existirem ainda
if os.path.exists(f'./basesDeDados/{date}') == False:
  os.mkdir(f'./basesDeDados/{date}')

if os.path.exists(f'./basesDeDados/{date}/{area}/') == False:
  os.mkdir(f'./basesDeDados/{date}/{area}/')

# Passar por todos os usuários
for userID in user_list:

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
      i += 1

  if len(tweet_term_list) == 0:
    print(f"O perfil {userID} não possui tweets com as palavras chaves")

  else:
    print(f'Numero de tweets com o termos {text_query}: {len(tweet_term_list)}')
    out_tweets = [
      [tweet.id_str, 
      tweet.created_at, 
      tweet.favorite_count, 
      tweet.retweet_count, 
      tweet.full_text.encode("utf-8").decode("utf-8")] 
      for idx,tweet in enumerate(tweet_term_list)
      ]
    df = DataFrame(out_tweets,columns=["id","postado_em:","numero_de_curtidas","numero_de_retweets", "texto"])
    df.to_csv(f'./basesDeDados/{date}/{area}/{userID}_tweets.csv',index=False)
    df.head(3)
  
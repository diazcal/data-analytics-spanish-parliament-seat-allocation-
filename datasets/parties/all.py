import sys
sys.path.append('../..')
from tools.party_data_generator import PartyHard

its_my_party = PartyHard("datasets/home_affairs_data/PROV_02_201911_1.xlsx")

df_regions_votes_and_parties = its_my_party.getCleanedData()

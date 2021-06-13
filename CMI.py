from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

"""
 * 시가총액 상위 20 (2021.06.13 기준)
  1. BTC    |  2. ETH    |  3. BNB    |  4. ADA    |  5. DOGE   |
  6. XRP    |  7. DOT    |  8. UNI    |  9. LTC    | 10. BCH    |
 11. SOL    | 12. LINK   | 13. MATIC  | 14. THETA  | 15. ICP    |
 16. XLM    | 17. FIL    | 18. TRX    | 19. EOS    | 20. XMR    |
 
 * 가치투자가 가능한 것 상위 15 (2021.06.13 기준)    
 - 기준
    1. 유지가 가능한가?
    2. 좋은 커뮤니티가 있는가?
    3. 확장성(Defi 등)이 있는가? / 그 자체로 밸류(BTC 등)가 있는가?
 
  1. BTC    |  2. ETH    |  3. BNB    |  4. ADA    |  5. DOGE   |
  6. DOT    |  7. SOL    |  8. LINK   |  9. MATIC  | 10. FIL    |
 11. TRX    | 12. XMR    | 13. AAVE   | 14. FTT    | 15. LUNA   |
 
  * 그 중에서도 가능한 것
  
  CMI10 INDEX
  -> BTC ETH BNB ADA DOGE DOT SOL FIL TRX LUNA
    
"""



class CMI():

    def __init__(self):
        CMI.url = 'https://pro-api.coinmarketcap.com/v1/'
        CMI.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '92dea723-abe6-47f9-840e-3ce956f4708d',
        }

    def get_CMI_dominance(self):

        url = CMI.url + "cryptocurrency/quotes/latest"
        parameters = {
            'symbol': "BTC,ETH,BNB,ADA,DOGE,DOT,SOL,FIL,TRX,LUNA",
        }

        session = Session()
        session.headers.update(CMI.headers)

        try:
            response = session.get(
                url=url,
                params=parameters
            ).json()

            crypto_datas = response['data']

            cryptos_dict = {
                crypto_data: {
                    "price": crypto_datas[crypto_data]["quote"]["USD"]["price"],
                    "circulating_supply": crypto_datas[crypto_data]["circulating_supply"],
                    "market_cap": crypto_datas[crypto_data]["quote"]["USD"]["market_cap"],
                } for crypto_data in crypto_datas
            }

            total_market_cap = sum(cryptos_dict[crypto_data]["market_cap"] for crypto_data in cryptos_dict)

            market_cap_per_dict = {
                crypto: round(
                    cryptos_dict[crypto]["market_cap"] / total_market_cap * 100,
                    2)
                for crypto in cryptos_dict
            }
            print(market_cap_per_dict)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)



C = CMI()
print(C.get_CMI_dominance())

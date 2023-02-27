from krxmarket import StockCorps
from krxmarket.performance import get_performance


if __name__ == '__main__':
    corps = StockCorps().corps
    idx = 0
    for stock_code, corp in corps.items():
        print(corp.name, idx + 1, '/', len(corps))
        get_performance(corp.corp_code)
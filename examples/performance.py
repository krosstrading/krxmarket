from krxmarket import StockCorps
from krxmarket import disclosure_list


if __name__ == '__main__':
    corps = StockCorps()
    samsung = corps.search_by_stock_code('005930')
    result = disclosure_list(samsung, '20220101', pblntf_detail_ty='A003')
    print(len(result))
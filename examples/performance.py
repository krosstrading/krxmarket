from krxmarket import StockCorps
from krxmarket import disclosure_list
from krxmarket.common.xbrl.xbrl import Xbrl


if __name__ == '__main__':
    corps = StockCorps()
    samsung = corps.search_by_stock_code('005930')
    result = disclosure_list(samsung, '20220101', pblntf_detail_ty='A003')
    report: Xbrl = result.pop(0)
    if report.xbrl:
        print(report.xbrl.get_fs().to_DataFrame().to_excel('output.xlsx'))
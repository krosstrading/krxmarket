from krxmarket import KrxCorp, disclosure_list
from krxmarket.common.types import MarketType


def test_get_disclosure_list():
    krxCorp = KrxCorp(
        name='미디어젠', stock_code='279600',
        corp_code='01190124', market_type=MarketType.KOSDAQ
    )
    dlist = disclosure_list(krxCorp, start_time='20160101',
                            pblntf_detail_ty='A003')
    print('page count', dlist.page_count)
    print('total count', dlist.total_count)
    for report in dlist.report_list:
        print(report.info)
    


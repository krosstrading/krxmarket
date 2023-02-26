from krxmarket import KrxCorp, disclosure_list
from krxmarket.common.types import MarketType


def test_get_disclosure_list():
    krxCorp = KrxCorp(
        name='삼성전자', stock_code='005930',
        corp_code='00126380', market_type=MarketType.KOSPI
    )
    dlist = disclosure_list(krxCorp, start_time='20220101')
    assert dlist['status'] == '000'
    assert 'list' in dlist
    assert len(dlist['list']) > 0

    dlist = disclosure_list(krxCorp, start_time='20220101', pblntf_detail_ty='A001')
    assert dlist['status'] == '000'
    print(dlist)
    assert len(dlist['list']) > 0
    


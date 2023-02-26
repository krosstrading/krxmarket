

from krxmarket.dart.api import fnltt_singl_acnt_all


def test_financial():
    dlist = fnltt_singl_acnt_all('00126380', '2022', '11012', 'CFS')
    for report in dlist['list']:
        print(report)
            
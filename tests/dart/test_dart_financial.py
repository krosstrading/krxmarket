

from krxmarket.dart.api import fnltt_singl_acnt_all


def test_financial():
    # 1분기보고서:11013, 반기보고서:11012, 3분기보고서:11014, 사업보고서 : 11011

    dlist = fnltt_singl_acnt_all('01190124', '2021', '11011', 'OFS')
    for report in dlist['list']:
        print(report)
            
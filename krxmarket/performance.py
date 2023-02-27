from krxmarket import fnltt_singl_acnt_all


def _fv(item: dict, key: str):
    value = item.get(key)
    return value


def get_performance(corp_code: str):
    """
    json structure
    [
        {
            'year': '2016',
            'quarter': 1,
            'apx_ms': xxxxxxxx
            data: {
                CF: [
                    {},
                    {}
                ],
                IS: {
                
                }
            }
        }
    ]
    """
    year = 2016
    # 1분기보고서:11013, 반기보고서:11012, 3분기보고서:11014, 사업보고서 : 11011
    report_seq = ['11013', '11012', '11014', '11011']
    report_all = []
    has_data = True
    while has_data:
        for i, seq in enumerate(report_seq):
            result = {
                'year': str(year),
                'quarter': str(i + 1),
                'data': {}
            }
            try:
                report = fnltt_singl_acnt_all(corp_code, str(year), seq, 'CFS')
                if report['status'] == '000' and 'list' in report:
                    items = _fv(report, 'list')
                    for item in items:
                        sj_div = _fv(item, 'sj_div')
                        if sj_div not in result['data']:
                            result['data'][sj_div] = []
                        
                        result['data'][sj_div].append({
                            'account_nm': _fv(item, 'account_nm'),
                            'frmtrm_amount': _fv(item, 'frmtrm_amount'),
                            'thstrm_amount': _fv(item, 'thstrm_amount'),
                            'account_id': _fv(item, 'account_id'),
                            'rcept_no': _fv(item, 'rcept_no')
                        })
            except Exception as ex:
                has_data = False
                print('no data on', year, seq, ex)
                break
            report_all.append(result)
        year += 1

    return report_all


if __name__ == '__main__':
    json_content = get_performance('00126380')
    import json
    with open('data.json', 'w') as f:
        json.dump(json_content, f)


from .auth import get_api_key
from ..common.webrequest import request
from .request import api_request
from ..common.file import read_file_from_zip


def get_corp_code() -> list:
    """ DART에 등록되어있는 공시대상회사의 고유번호,회사명,대표자명,종목코드, 최근변경일자 다운로드

    Returns
    -------
    OrderedDict
        고유번호 및 회사 정보
    """
    url = 'https://opendart.fss.or.kr/api/corpCode.xml'
    # Set API KEY
    api_key = get_api_key()
    payload = {'crtfc_key': api_key}

    # Request Download
    file_url = request.download(url=url, payload=payload)
    
    data = read_file_from_zip(file_url, 'CORPCODE.xml')
    if len(data) == 0:
        raise FileNotFoundError('CORPCODE.xml Not Found')
    return data['result']['list']


def get_corp_info(corp_code: str):
    """ 기업 개황 조회

    Parameters
    ----------
    corp_code: str
        공시대상회사의 고유번호(8자리)

    Returns
    -------
    dict
        기업 개황
    """
    path = '/api/company.json'

    return api_request(path=path, corp_code=corp_code)



def get_executive_holders(corp_code: str) -> dict:
    """ 
    임원ㆍ주요주주특정증권등 소유상황보고서 내에 임원ㆍ주요주주 소유보고 
    정보를 제공합니다.

    Parameters
    ----------
    corp_code: str
        공시대상회사의 고유번호(8자리)※ 개발가이드 > 공시정보 > 고유번호 참고
    api_key: str, optional
        DART_API_KEY, 만약 환경설정 DART_API_KEY를 설정한 경우 제공하지 않아도 됨
    Returns
    -------
    dict
        임원ㆍ주요주주 소유보고
    """

    path = '/api/elestock.json'

    return api_request(
        path=path,
        corp_code=corp_code,
    )


def get_major_holder_changes(
    corp_code: str,
) -> dict:
    """ 주식등의 대량보유상황보고서 내에 대량보유 상황보고 정보를 제공합니다.

    Parameters
    ----------
    corp_code: str
        공시대상회사의 고유번호(8자리)※ 개발가이드 > 공시정보 > 고유번호 참고
    api_key: str, optional
        DART_API_KEY, 만약 환경설정 DART_API_KEY를 설정한 경우 제공하지 않아도 됨
    Returns
    -------
    dict
        대량보유 상황보고
    """

    path = '/api/majorstock.json'

    return api_request(
        path=path,
        corp_code=corp_code,
    )

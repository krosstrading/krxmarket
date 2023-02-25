from krxmarket.dart.api import get_corp_code


def test_get_corp_codes():
    print(get_corp_code()[0])
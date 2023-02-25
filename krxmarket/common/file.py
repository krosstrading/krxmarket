import tempfile
import zipfile
import re
import os
import xmltodict


def read_file_from_zip(download_uri: str, filename: str):
    with tempfile.TemporaryDirectory() as path:
        with zipfile.ZipFile(download_uri, 'r') as zip_ref:
            zip_ref.extractall(path=path)

        for root, _, files in os.walk(path):
            for file in files:
                if re.search(filename, file):
                    with open(os.path.join(root, file), encoding='utf8') as f:
                        return xmltodict.parse(f.read())
    return ''
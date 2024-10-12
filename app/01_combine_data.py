import os
import zipfile
import py7zr

import pandas


def get_items():
    folder_path = 'data/tce_rs'
    for file_name in os.listdir(folder_path):
        if not file_name.endswith('.xml.7z'):
            continue
        zip_path = os.path.join(folder_path, file_name)

        with py7zr.SevenZipFile(zip_path, mode='r') as zip_ref:
            zip_ref.extractall()
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_items_name = f'{file_name.removesuffix('.zip')}_NotaFiscalItem.csv'
            with zip_ref.open(file_items_name) as file:
                file.seek(0)
                data_frame = pandas.read_csv(file, delimiter=';', encoding='latin1')
                data_frame.rename(columns={
                    'CHAVE DE ACESSO': 'access_key',
                    'DATA EMISSÃO': 'emission_date',
                    'CPF/CNPJ Emitente': 'emission_owner',
                    'NÚMERO PRODUTO': 'product_index',
                    'DESCRIÇÃO DO PRODUTO/SERVIÇO': 'description',
                    'CÓDIGO NCM/SH': 'ncm',
                    'NCM/SH (TIPO DE PRODUTO)': 'ncm_description',
                    'CFOP': 'cfop',
                    'QUANTIDADE': 'quantity',
                    'UNIDADE': 'unit_kind',
                    'VALOR UNITÁRIO': 'unitary_value',
                    'VALOR TOTAL': 'total_value',
                }, inplace=True)
                yield data_frame \
                    .loc[:, [
                        'access_key',
                        'emission_date',
                        'emission_owner',
                        'product_index',
                        'description',
                        'ncm',
                        'ncm_description',
                        'cfop',
                        'quantity',
                        'unit_kind',
                        'unitary_value',
                        'total_value',
                    ]]


data_frame = pandas.concat(get_items(), ignore_index=True)

data_frame.to_csv('data/combined.csv.gz', index=False, compression='gzip', encoding='utf-8')

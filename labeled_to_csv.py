import pandas as pd
from tqdm import tqdm

import os

path = 'honey'

output_dir = 'honey'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for input_file in tqdm(os.listdir(path)):
    output_file = os.path.join(output_dir, input_file.split('.')[0] + 'optimized.csv')
    print('start opening')

    with open(os.path.join(path, input_file), 'r') as file:
        lines = file.readlines()
    print('ended opening')

    print('start replacing')
    #In the labeled files, there are two instances of a triple space used, instead of a tab, first change these to a tab before splitting
    lines_processed = [line.replace('   ', '\t', 2) for line in lines]
    print('ended replacing')

    print('start writing')
    with open('temp_conn.log', 'w') as file:
        file.writelines(lines_processed)
    print('ended writing')

    print('start reading temp file')
    #After we ensured all seperations are a proper tab, we can split on tab
    df = pd.read_csv('temp_conn.log', sep='\t', comment='#', header=None)
    print('ended reading temp file')

    column_names = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p',
                    'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes',
                    'conn_state', 'local_orig', 'local_resp', 'missed_bytes',
                    'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts',
                    'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed-label']
    df.columns = column_names[:len(df.columns)]

    print('start dropping')
    df.dropna(axis=1, how='any', inplace=True)

    columns_to_drop = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'history', 'tunnel_parents', 'detailed-label']
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    #Create mappings
    protocol_mapping = {'tcp': 0, 'udp': 1, 'icmp': 2}
    service_mapping = {'-': 0, 'http': 1, 'dhcp': 2, 'ssh': 3, 'dns': 4, 'irc': 5}
    label_mapping = {'Malicious': 1, 'benign': 0}
    detailed_label_mapping = {'PartOfAHorizontalPortScan': 1, '-': 0, 'C&C': 2, 'C&C-FileDownload': 2, 'C&C-Mirai': 3,
                             'C&C-HeartBeat': 4, 'C&C-HeartBeat-Attack': 4, 'C&C-HeartBeat-FileDownload': 4,
                             'C&C-Torii': 5, 'DDoS': 6, 'FileDownload': 7, 'Okiru': 8, 'Okiru-Attack': 8,
                             'PartOfAHorizontalPortScan-Attack': 1, 'C&C-PartOfAHorizontalPortScan': 1, 'Attack': 9}
    conn_state_mapping = {'S0': 1, 'REJ': 2, 'SF': 3, 'OTH': 4, 'RSTOS0': 5, 'RSTR': 6, 'S2': 7, 'RSTRH': 8, 'RSTO': 9,
                          'S1': 10, 'SH': 11}

    #Apply mappings
    df['proto'] = df['proto'].map(protocol_mapping)
    df['service'] = df['service'].map(service_mapping)
    df['label'] = df['label'].map(label_mapping)
    df['detailed-label'] = df['detailed-label'].map(detailed_label_mapping)
    df['conn_state'] = df['conn_state'].map(conn_state_mapping)

    #Replace missing values indicated by '-'
    columns_to_replace = ['id.resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes',
                          'conn_state', 'local_orig', 'local_resp', 'missed_bytes',
                          'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes',
                          'label']

    for col in columns_to_replace:
        if col in df.columns:
            df[col] = df[col].replace('-', -1)
    df['detailed-label'] = 0
    df.to_csv(output_file, index=False)

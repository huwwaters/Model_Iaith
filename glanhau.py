import xmltodict
import pprint
import json
import pandas as pd
import os
import re

directory = r'/Users/huwwaters/Documents/Y_Cofnod/Cymraeg'

rhestr = []

for filename in os.listdir(directory):

    if filename.endswith('.xml'):

        print(os.path.join(directory, filename))

        temp = []

        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as input:
            #rhestr.append(json.dumps(xmltodict.parse(input.read(), process_namespaces=True)))
            data = xmltodict.parse(input.read(), process_namespaces=True)
            data = data['dataroot'][list(data['dataroot'].keys())[1]]

            if isinstance(data, list):
                for i in data:
                    rhestr.append(i)
            else:
                rhestr.append(data)


df = pd.DataFrame(rhestr)
df.to_csv(r'/Users/huwwaters/Documents/Y_Cofnod/cymraeg.csv', index=False)

def strip_tags(text):
    text = re.sub('&nbsp;', ' ', text)
    text = re.sub('&acirc;', 'â', text)
    text = re.sub('&ocirc;', 'ô', text)
    text = re.sub('&ecirc;', 'ê', text)
    text = re.sub('&pound;', '£', text)
    text = re.sub('&mdash;', '-', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' +</p>', '</p>', text)
    text = re.sub('<p style="text-align: left;">', '<p>', text)
    
    return text

for col in ['Contribution_English', 'Contribution_Welsh', 'contribution_verbatim', 'contribution_translated']:
    df[col] = df[col].fillna('')
    df[col] = df[col].apply(strip_tags)

def p_swap(text):
    if not text.startswith('<p>'):
        return '<p>' + text + '</p>'
    else:
        return text

df['Contribution_Welsh'] = df['Contribution_Welsh'].apply(p_swap)

def str_count(text):
    if text.count('<p>') == 0:
        return '<p>' + text + '</p>'
    else:
        return text

df['Contribution_Welsh'] = df['Contribution_Welsh'].apply(str_count)

def str_p_split(text):
    return re.split('<p>|</p>', text)

df['Contribution_Welsh'] = df['Contribution_Welsh'].apply(str_p_split)

rhestr = df['Contribution_Welsh'].tolist()

for i, x in enumerate(rhestr):
    rhestr[i] = [re.sub('^ *', '', j) for j in x]
    rhestr[i] = [j for j in x if j != '']

    print(i)
    print(x)
    break



df['Contribution_Welsh'].iloc[0].split(r'<p>|</p>')

def extract(text):
    return re.findall('<p>(.*?)</p>', text)

df['Contribution_Welsh'] = df['Contribution_Welsh'].apply(extract)
df['id'] = df.index + 1

df1 = pd.DataFrame(df['Contribution_Welsh'].tolist(), index=df['id']).stack().reset_index(drop=True, level=1).reset_index(name='Contribution_Welsh')[['Contribution_Welsh', 'id']]
df1['Contribution_Welsh_paragraph_id'] = df1.index + 1
df.rename(columns={'Contribution_Welsh': 'Contribution_Welsh_paragraph'}, inplace=True)

df = df.merge(df1, how='left', on='id')

pd.DataFrame(df['Contribution_Welsh'].apply(extract).tolist()).stack().values

rhestr = df[df['Contribution_Welsh'] != '']['Contribution_Welsh'].tolist()

for i in rhestr:
    if not i.startswith('<p>'):
        print(i)


    print(re.search('^(?<!<p>).*', i))
    print(i)
    break









rhestr = df['Contribution_Welsh'].tolist()

for i in rhestr[1000:2000]:
    if i is not None:
        if i.startswith('<p>'):
            if len(re.findall('<p>(.*?)</p>', i)) > 1:
                for j in re.findall('<p>(.*?)</p>', i):
                    print('\t', j)
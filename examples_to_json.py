# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from glob import glob
import json


def clean_test_without_echidna_function(data):
    return [x for x in data if x['tests'] != ''] 

if __name__ == "__main__":
    data = []  
    for file_name in glob('../echidna_repo/tests/solidity/*/*.sol'):
        yalm_name = file_name[:-4]+'.yaml'
        
        f = open(file_name,'r')
        text = f.read()
        index = text.find('function echidna')
        contract = text[:index]+'\n}'
        tests = text[index:-2]
        yalm_text = ''
        try: 
            yalm_name = file_name[:-4]+'.yaml'
            f = open(yalm_name,'r')
            yalm_text = f.read()
        except:
            pass
        names = file_name.split('/')
        data.append({'name':names[-2]+'/'+names[-1],
                     'contract':contract,
                     'tests':tests,
                     'config':yalm_text})
    data = clean_test_without_echidna_function(data)
    with open('invariants_examples.json', 'w') as f:
        json.dump(data, f)

    
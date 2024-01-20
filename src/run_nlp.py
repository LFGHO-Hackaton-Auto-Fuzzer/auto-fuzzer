#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:54:56 2024

@author: farduh
"""

from langchain.chains import ConversationChain
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

import os   
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def load_invariants():
    f = open('invariants_examples.json')
    data = json.load(f)
    return data

def create_echidna_functions(contract : str) -> str:
    data = load_invariants()
    chat = ChatOpenAI(temperature=0.0, openai_api_key=OPENAI_API_KEY)
    data = load_invariants()
    chat = ChatOpenAI(temperature=0.0, openai_api_key=OPENAI_API_KEY)
    messages =[
        SystemMessage(
            content="""
            You are going to generate echidna function to test a new smart contract, 
            to do that I'm going to give you the following a json with examples in which you are 
            going to find the original contract 'contract', the tests 'tests' and the config file
            needed as 'config'
            """
            ),
        HumanMessage(content=str(data[:20])),
        HumanMessage(content=str(data[30:40])),
        HumanMessage(content=f"""
                        generate a json with two keys 'tests' and 'config' with the echidna function to test
                        and the configfile (if is neeeded) for the following contract: {contract}
                        """),
        ]
    response = chat(messages)
    return json.loads(response.content)


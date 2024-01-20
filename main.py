import sys
from src.run_nlp import create_echidna_functions

def get_contract_content(contract_path):
    f = open(contract_path, "r")
    content = f.read()
    f.close()
    return content

def generate_echidna_functions(path_to_contract):
    content = get_contract_content(path_to_contract)
    echidna_functions = create_echidna_functions(content)
    return echidna_functions

def save_new_contract(echidna_functions, contract_path):
    file_name = contract_path.split('/')[-1]
    content = get_contract_content(contract_path)
    last_character_index = content.rfind('}')

    f = open('outputs/'+file_name, "w")
    f.write(content[:last_character_index-1]
            + "\n  "
            + echidna_functions['tests']
            + '\n}')
    f.close()
    f = open('outputs/'+file_name.split('.')[-2]+'.yaml', "w")
    f.write(echidna_functions['config'])
    f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('python main.py <<path_to_contract>>')
        exit()
    contract_path = sys.argv[1]
    echidna_functions = generate_echidna_functions(contract_path)
    echidna_functions = save_new_contract(echidna_functions, contract_path)
    
import json
import os

def get_path_characters(id):
    our_dir = os.getcwd()
    file_name = str(id) + '.json'
    file_path = os.path.join(our_dir,'core\db\сharacters',file_name)
    return file_path

def save_character(id, data):
    file_path = get_path_characters(id)
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False)

def load_character(id):
    file_path = get_path_characters(id)
    with open(file_path,'r',encoding='utf-8') as f:
        return json.load(f)
    

    
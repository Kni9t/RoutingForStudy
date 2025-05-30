import json

def Save(fileName, data):
    with open(fileName, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.close()
            
def Load(fileName):
    output = None
    
    with open(fileName, 'r', encoding = 'utf-8') as file:
        output = json.loads(file.read())
    
    return output
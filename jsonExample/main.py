import json

def main():
    _jsonExample = ''
    f = open(r'jsonData.json')
    _jsonExample = f.read()
    print(_jsonExample)
    to_json = json.loads(_jsonExample)
    # print(to_json)
    indice = 0
    for entrie in to_json['entries']:
        print(entrie)
        innerJson = entrie['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['jsonData']
        innerJson = json.loads(innerJson.replace('\'','"'))
        print(innerJson)
        for item in innerJson:
            for prop in item:
                entrie[prop] = item[prop]
        print(innerJson)
        print(entrie)
    # para =to_json['entries'][0]['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['jsonData']
    # print(para)


if __name__ == '__main__':
    main()
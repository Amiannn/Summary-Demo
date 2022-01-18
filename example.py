from lib.summer import Summer

if __name__ == '__main__':
    doc = None
    with open('doc.txt', 'r', encoding='utf-8') as fr:
        doc = fr.read()

    summer = Summer()
    result = summer.run(doc, topk=10)
    print('\n' * 2)
    for res in result:
        print(res['sentence'])
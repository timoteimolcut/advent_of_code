import sys
import json

sum = 0
def processJSON(obj):
    global sum
    if isinstance(obj, dict):
        # for part 2
        # if 'red' in obj.values():
            # return
        for k, v in obj.items(): 
            processJSON(v)     
    elif isinstance(obj, list):
        for ll in obj:
            processJSON(ll)
    else:
        print(obj)
        try:
            sum += int(obj)
        except ValueError:
            pass
    return
    

def main():
    fileContent = sys.stdin.read()
    jsonObj = json.loads(fileContent)
    processJSON(jsonObj)
    print(f'Total sum is: {sum}')
    





if __name__ == '__main__':
    main()
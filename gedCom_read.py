import sys, re

tree = {}

def parse(line):
    if 'person' not in parse.__dict__:
        parse.person = {}
    if 'parent' not in parse.__dict__:
        parse.parent = None

    m = re.match('^(\d+) (?:@(\w+)@ )?(\w+)(?: )?(.+)?$', line)
    if m != None:
        layer, id, type, data = m.group(1,2,3,4)

        if type == 'INDI':
            if 'id' in parse.person:
                tree[parse.person['id']] = parse.person
            parse.person = {}
            parse.parent = None
            parse.person['id'] = id
        elif type == 'NAME':
            parse.person['name'] = data
            
with open('My-Family-14-Sep-2020-272.ged', 'r') as ged:
    for line in ged:
        parse(line.strip())
        
def formatOutput(line):
    x = "swag"
    try:
        x=="yeet"
    except:
        print("rip");
        
    output =  line.split()
    output.insert(1,"|")
    output.insert(3,"|")
    checker = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRTL","NOTE"]
    if output[2] in checker:
        output.insert(4,"Y")
    else:
        output.insert(4,"N")
    output.insert(5,"|")
    fOutput = " ".join(output)
    return "<--" +fOutput

print(tree)
output ="";
print("Type stop to end program");

while(output!= "stop"):
    output = input()
    print("-->"+output)
    print(formatOutput(output))

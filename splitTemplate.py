import re

names = [{'name': 'Introduction'},
         {'name': 'Installation'},
         {'name': 'Configuration'},
         {'name': 'Final steps'},
         {'name': 'Installing Asset Plugins'},
         {'name': 'Sanity check Procedures'},
         {'name': 'Diagnosis Procedures'}]

with open('./instalacionTemplate.txt') as template:
    temp = template.read()
    formatedFile = re.sub(r'(-+)\n(.*\n)\1', r'*\______\*\n# \2', temp)
    l = re.split(r'______', formatedFile)
    i = 1
    for nam in names:
        with open('./{}.text'.format(nam.get('name')), 'w') as g:
            g.write('{}\n'.format(l[i]))
            i = i + 1

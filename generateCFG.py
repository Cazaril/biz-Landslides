names = [{'name': 'Introduction'},
         {'name': 'Installation'},
         {'name': 'Configuration'},
         {'name': 'Final steps'},
         {'name': 'Installing Asset Plugins'},
         {'name': 'Sanity check Procedures'},
         {'name': 'Diagnosis Procedures'}]

for nam in names:
    with open('./{}.cfg'.format(nam.get('name')), 'w') as f:
        f.write('[landslide]\n')
        f.write('theme = ./fiwaretheme\n')
        f.write('source = {}.md\n'.format(nam.get('name')))
        f.write('destination = {}.html\n'.format(nam.get('name')))
        f.write('relative = True\n')
        f.write('linenos = no\n')
        f.write('extensions = tables\n')

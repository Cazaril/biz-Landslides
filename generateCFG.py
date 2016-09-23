import re

names = [{'name': 'User-Guide'},
         {'name': 'Profile-Configuration'},
         {'name': 'Admin'},
         {'name': 'Manage-Categories'},
         {'name': 'Seller'},
         {'name': 'Manage-Catalogs'},
         {'name': 'Manage-Product-Specifications'},
         {'name': 'Manage-Product-Offerings'},
         {'name': 'Manage-Revenue-Sharing-Models'},
         {'name': 'Manage-Transactions'},
         {'name': 'Manage-Received-Orders'},
         {'name': 'Customer'},
         {'name': 'List-Available-Offerings'},
         {'name': 'Create-Order'},
         {'name': 'Manage-Acquired-Products'},
         {'name': 'Manage-Requested-Orders'}]


# for nam in names:
#    with open('./{}.cfg'.format(nam.get('name')), 'w') as f:
#        f.write('[landslide]\n')
#        f.write('theme = ./fiwaretheme\n')
#        f.write('source = {}.md\n'.format(nam.get('name')))
#        f.write('destination = {}.html\n'.format(nam.get('name')))
#        f.write('relative = True\n')
#        f.write('linenos = no\n')
#        f.write('extensions = tables\n')


# Con esta regexp te quitas los titulos
# [\w ]*\n(=+|-+)
# Esta va a ser mejor para el split
# =+|-+

# Y con esta pretendo splitear las slides en las imagenes
# .. \w*:: (\/.*)\n.*
with open('./manualTemplate.txt') as template: #, open('./pruebita.txt', 'w+') as g:
    file = template.read()
    formatedFile = re.sub(r'(.*\n)(=+|-+)', r'\2\n\1', file)
#    g.write(formatedFile)
    l = re.split(r'=+|-+', formatedFile)
    i = 1
    for nam in names:
        with open('./{}.md'.format(nam.get('name')), 'w') as g:
            g.write('# Introduction to WireCloud\n')
            g.write('.fx: cover\n')
            g.write('@conwet\n')
            g.write('---\n')
            g.write('{}\n'.format(l[i]))
            i = i + 1

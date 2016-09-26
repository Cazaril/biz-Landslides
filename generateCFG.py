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

# Las notas de las imagenes van a ser un poco mas putada, voy a probar a poner
# cada nota con su imagen, pero no creo que quede bien
# (\.\. note::\n)(.*)
with open('./manualTemplate.txt') as template:
    temp = template.read()
    formatedFile = re.sub(r'(.*\n)(=+|-+)', r'\2\n#\1', temp)
    l = re.split(r'=+|-+', formatedFile)
    i = 1
    for nam in names:
        with open('./{}.text'.format(nam.get('name')), 'w') as g:
            g.write('{}\n'.format(l[i]))
            i = i + 1

for nam in names:
    with open('./{}.text'.format(nam.get('name')), 'r') as g:
        fich = g.read()
        f1Text = re.sub(r'(\.\. \w*:: )(\/.*)\n(.*)\n\n(\.\. note::\n\s*)(.*)',
                        r'---\n#{}\n![\5](.\2)\n---\n#{}\n'.format(nam.get('name'),
                                                                   nam.get('name')),
                        fich)
        f1Text = re.sub(r'(\.\. \w*:: )(\/.*)\n(.*)\n\n(?!\.\.)',
                        r'---\n#{}\n![](.\2)\n---\n'.format(nam.get('name')),
                        f1Text)
        formatedText = ''
        while(formatedText != f1Text):
            formatedText = re.sub(r'(\.\. \w*:: )(\/.*)\n(.*)\n\n(?!\.\.)',
                                  r'---\n#{}\n![](.\2)\n'.format(nam.get('name')),
                                  f1Text)
            aux = formatedText
            formatedText = f1Text
            f1Text = aux

        with open('./{}.md'.format(nam.get('name')), 'w') as md:
            md.write('# Introduction to WireCloud\n')
            md.write('.fx: cover\n')
            md.write('@conwet\n')
            md.write('---\n')
            md.write(formatedText)

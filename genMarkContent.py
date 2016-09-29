import re

names = [{'name': 'Introduction'},
         {'name': 'Installation'},
         {'name': 'Configuration'},
         {'name': 'Final steps'},
         {'name': 'Installing Asset Plugins'},
         {'name': 'Sanity check Procedures'},
         {'name': 'Diagnosis Procedures'}]

# Con esta regexp te quitas los titulos
# [\w ]*\n(=+|-+)
# Esta va a ser mejor para el split
# =+|-+

# Y con esta pretendo splitear las slides en las imagenes
# .. \w*:: (\/.*)\n.*

# Las notas de las imagenes van a ser un poco mas putada, voy a probar a poner
# cada nota con su imagen, pero no creo que quede bien
# (\.\. note::\n)(.*)

# for nam in names:
with open('./Introduction.text') as g:  # .format(nam.get('name')), 'r') as g:
    fich = g.read()
        

# Im sorry for this but its the fastest and ugliest
# way to replace the tokens i wrote
def firstAndLastSlide(this, cadena):
    half = re.sub(r'\\\*',
                  r'# Introduction to Business API ecosystem\n.fx: cover\n@conwet\n---\n',
                  cadena)
    return re.sub(r'\*\\',
                  r'\n---\n.fx: back-cover\nThanks\nFIWARE                                FIWARE Lab\nOPEN APIs FOR OPEN MINDS              Spark your imagination\n\n         www.fiware.org               FIWARE Ops\ntwitter: @Fiware                      Easing your operations\n'
                  , half)


# This will replace all links inside the template, as long as they are
# expresed between `` and later there is the same string beginning with .. _,
# and a : separating the string from the link
def replaceLinks(this, cadena):
    links = re.findall(r'.. _(.+): (.*)', cadena)
    for link in links:
            cadena = re.sub(r'`.*`_',
                            r'[{1}]({2})'.format(link[0], link[1]),
                            cadena)
    cadena = re.sub(r'\* `(.*) <(.*)>`__',
                    r'* [\1](\2)',
                    cadena)
    cadena = re.sub(r'`(.*) <(.*)>`__',
                    r'[\1](\2)',
                    cadena)
    return cadena


def replaceImages(this, cadena):
    return 1


def replaceNotes(this, cadena):
    cadena = re.sub(r'.. note::\n(.*)', r'Note: \1', cadena)
    return cadena
# with open('./instalacionTemplate.txt', 'r+') as template:
#    temp = template.read()
#    formatedFile = re.sub(r'(=+|-+|\++)\n(.*)\n\1', r'\2\n\1', temp)
#    template.seek(0)
#    template.write(formatedFile)
#    template.truncate()

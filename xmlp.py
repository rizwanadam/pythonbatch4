from lxml import etree
def xmlp():
    xmldoc=etree.parse('plant_catalog.xml')
    root=xmldoc.getroot()
    for child in root:
        if child.findtext('BOTANICAL')=='Aquilegia canadensis':
            print(child.findtext('COMMON'))
xmlp()

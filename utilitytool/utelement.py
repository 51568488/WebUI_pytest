from bs4 import BeautifulSoup
import CV
import json
from utilitytool.utXpath import XpathGEN
import utilitytool.utfile as utfile

eletype = ["button","input","span"]

def createObjfile():
    soup = getSoup()
    elementslist = []
    elementslist = getElements(soup)
    for element in elementslist:
        utfile.addNewline(CV.OBJFOLDER_PATH + "object.py", element)


def getSoup():
    strSource = CV.BROWSER.page_source
    soup = BeautifulSoup(strSource)
    return soup

def getElements(soup):
    elementslist = []
    for tag in soup.find_all(eletype):
        if tag.has_attr("type"):
            tagType = str.upper(tag["type"])
        else:
            tagType = tag.name
        if tag.has_attr("id"):
            elementslist.append(tagType + "_" + str.upper(tag["id"]) + "_ID = '" + tag["id"] + "'\n")
        elif tag.has_attr("name"):
            elementslist.append(tagType + "_" + str.upper(tag["name"]) + "_NAME = '" + tag["name"] + "'\n")
        else:
            xpath_gen = XpathGEN(soup, tag)
            xpathl = xpath_gen.get_xpaths()
            for xpathstr in xpathl:
                elementslist.append(tagType + "_" + str.upper(tag.text.replace(" ","")) + "_XPATH = '" + xpathstr + "'\n")
    return elementslist

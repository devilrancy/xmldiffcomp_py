Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import lxml.etree
>>> from xml_diff import compare
>>> dom1 = lxml.etree.parse("book1.xml").getroot()

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dom1 = lxml.etree.parse("book1.xml").getroot()
  File "lxml.etree.pyx", line 3299, in lxml.etree.parse (src\lxml\lxml.etree.c:72655)
  File "parser.pxi", line 1791, in lxml.etree._parseDocument (src\lxml\lxml.etree.c:106263)
  File "parser.pxi", line 1817, in lxml.etree._parseDocumentFromURL (src\lxml\lxml.etree.c:106564)
  File "parser.pxi", line 1721, in lxml.etree._parseDocFromFile (src\lxml\lxml.etree.c:105561)
  File "parser.pxi", line 1122, in lxml.etree._BaseParser._parseDocFromFile (src\lxml\lxml.etree.c:100456)
  File "parser.pxi", line 580, in lxml.etree._ParserContext._handleParseResultDoc (src\lxml\lxml.etree.c:94543)
  File "parser.pxi", line 690, in lxml.etree._handleParseResult (src\lxml\lxml.etree.c:96003)
  File "parser.pxi", line 618, in lxml.etree._raiseParseError (src\lxml\lxml.etree.c:95015)
IOError: Error reading file 'book1.xml': failed to load external entity "book1.xml"
>>> 

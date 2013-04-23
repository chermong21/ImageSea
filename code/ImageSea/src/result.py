'''
Created on Dec 27, 2012

@author: go
'''

import sys

import retrieve
import RetrieveConstants

htmlTemplateBegin = '<html>\
<head></head>\
<body>\
<table border="2">'

htmlSourceImage = '<tr>\
    <td align="center" colspan="2">Query Image:<br><img src="%s"/></td>\
</tr>'

htmlResultImage = '<tr>\
    <td align="center"><img src="%s"/></td>\
    <td>Relevance: %s</td>\
</tr>'

htmlTemplateEnd = '</table>\
</body>\
</html>'

strm = "<html></html>"

def main():
    # Command line check.
    if len(sys.argv) < 2:
        print "Usage: python result.py query_image."
        sys.exit()
    else:
        queryImage = sys.argv[1]
        
    # Get results for query image
    queryResult = retrieve.getResult(queryImage);
    
    # sd
    html = htmlTemplateBegin + htmlSourceImage %(queryImage)
    for image in queryResult:
        html += htmlResultImage %(image[0], image[1])
    html += htmlTemplateEnd
    
    htmlFile = open(RetrieveConstants.RESULT_FILE, "w")
    htmlFile.write(html)
    htmlFile.close()
    
    print queryResult

if __name__ == '__main__':
    main()
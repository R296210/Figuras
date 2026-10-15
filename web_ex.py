import urllib.request
import urllib.error
import gzip


myAddres = "https://www.python.org/"
headers = {"Usser-Agent": "Mozilla/5.0"}

request = urllib.request.Request(myAddres, headers=headers)

try:    
    with urllib.request.urlopen(request, timeout=10) as response:
        htmlText = response.read().decode("utf-8")
    startTag ="<title>"
    endTag ="</title>"
    
    startIndex = htmlText.find(startTag)    
    endIndex = htmlText.find(endTag)

    if startIndex != -1 and endIndex != -1:
        startIndex += len (startTag)
        title = htmlText[startIndex:endIndex]
        print(htmlText[startIndex:endIndex])
    else:
        print("No se encontraron las etiquetas title. ")

except urllib.error.HTTPError as error:
    print("Error HTTP:", error.code)
    print("Descripcion:", error.reason)

except urllib.error.URLError as error:   
    print("Error de conexión", error.reason)    
  

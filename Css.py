import ast
import codeGen




widthList=[]
for tag in range(0, len(codeGen.allList)):
    dictionary = ast.literal_eval(codeGen.allList[tag])
    widthList.append(dictionary["width "])


codeGen.basic_html_code_start()
def html():
    for tag in range(0, len(codeGen.allList)):
        dictionary = ast.literal_eval(codeGen.allList[tag])
        Class1 = dictionary['class']
        y1 = dictionary["y1"]
        tagNumber = codeGen.count(Class1, y1)
        codeGen.CSS(dictionary, tagNumber)

    print("</style>")
    print("</head>")
    print("<body>")
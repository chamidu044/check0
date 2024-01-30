import pandas as pd
import ast
import sectionBreak

excel_file_path = '/Users/chamiduhimantha/Downloads/check0/HTML TAGS DATASET.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)
sectionBreak.sectionBreak()
file = open("all.txt", "r")


def basic_html_code_start():
    print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
<style>''')



def CSS(Dict, tagNumber):
    width = sectionBreak.imageWidth()
    height = sectionBreak.imageHeight()
    print("." + Dict["class"] + str(tagNumber) + "{")
    print("         " +"width:" + str(((Dict["width"]) / width) * 100) + "%" + ";")
    print("         " +"height:" + str(((Dict["height"]) / height) * 100) + "%" + ";")
    print("         " +"border: 1px solid black;")
    print("         " +"position: absolute;")
    print("         " +"left:" + str(((Dict["x1"]) / width) * 100) + "%" + ";")
    print("         " +"top:" + str(((Dict["y1"]) / height) * 100) + "%" + ";" +
          "}")


def basic_html_code_end():
    print('''           
</body>
</html>''')


def generate_tag(Class):
    element_to_generate = Class  # Replace with the actual index you want

    row_index = \
        df.index[df.apply(lambda row: row.astype(str).str.contains(element_to_generate).any(), axis=1)].tolist()[0]

    open_tag = df.loc[row_index, df.columns[1]]

    return open_tag


def close_tag(Class):
    element_to_generate = Class  # Replace with the actual index you want

    row_index = \
        df.index[df.apply(lambda row: row.astype(str).str.contains(element_to_generate).any(), axis=1)].tolist()[0]

    close_tag = df.loc[row_index, df.columns[4]]

    return close_tag


def Inner_Open_Tag(Class):
    element_to_generate = Class
    row_index = \
        df.index[df.apply(lambda row: row.astype(str).str.contains(element_to_generate).any(), axis=1)].tolist()[0]

    Inner_Tag = df.loc[row_index, df.columns[2]]
    return Inner_Tag


def Inner_Close_Tag(Class):
    element_to_generate = Class
    row_index = \
        df.index[df.apply(lambda row: row.astype(str).str.contains(element_to_generate).any(), axis=1)].tolist()[0]

    Inner_C_Tag = df.loc[row_index, df.columns[3]]
    return Inner_C_Tag


allList = []
repeatList = []
for i in file:
    allList.append(i)


def count(Class, y1):
    Count = 0
    for next in range(1, len(allList)):
        Dict3 = ast.literal_eval(allList[next])
        if Class == Dict3["class"] and y1 >= Dict3['y1']:
            Count = Count + 1
    return Count


def inside(Dict):
    for after in range(1, len(allList)):
        Dict4 = ast.literal_eval(allList[after])
        if Dict["x1"] < Dict4["x1"] < Dict["x2"] and Dict["y1"] < Dict4["y1"] < Dict["y2"]:
            repeatList.append(Dict4)

    Boolean = True
    for i in range(len(repeatList)):
        if Dict == repeatList[i]:
            Boolean = False
    return Boolean


def responsive():
    for tag in range(0, len(allList)):
        Dictionary = ast.literal_eval(allList[tag])










for tag in range(0, len(allList)):
    dictionary = ast.literal_eval(allList[tag])
    Class1 = dictionary['class']
    y1 = dictionary["y1"]
    tagNumber = count(Class1, y1)
    echo = inside(dictionary)

    CSS(dictionary, tagNumber)

print("</style>")
print("</head>")
print("<body>")

for i in range(0, len(allList)):
    Dict = ast.literal_eval(allList[i])
    Class1 = Dict['class']
    y1 = Dict["y1"]
    tagNumber = count(Class1, y1)
    echo = inside(Dict)
    if echo == False:
        continue



    if Class1 == "Navigation Bar":
        Nav_text = Dict["text"][0].split()
        print("         " + generate_tag(Class1) + " Class = " +"NavigationBar" + str(tagNumber) + ">")
        for text in range(len(Nav_text)):
            print("             " + Inner_Open_Tag(Class1)+">" + str(Nav_text))
            print("             " + Inner_Close_Tag(Class1))
        print("         " + close_tag(Class1))
    else:
        print("         " + generate_tag(Class1) + " Class = " + Class1 + str(tagNumber) + ">" + str(Dict["text"][0]))
        for j in range(1, len(allList)):
            Dict1 = ast.literal_eval(allList[j])
            if Dict["x1"] < Dict1["x1"] < Dict["x2"] and Dict["y1"] < Dict1["y1"] < Dict["y2"]:
                Class2 = Dict1["class"]
                print("             " + generate_tag(Class2) + " Class = " + Class2 + str(tagNumber) + ">" + str(Dict1["text"][0]))

                print("             " + close_tag(Class2))
        print("         " + close_tag(Class1))

basic_html_code_end()
open('all.txt', 'w').close()

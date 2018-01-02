"""
    File Differ
    Compares textA with textB

    constraint:
        for now, It only works efficiently with one character per line.
        But testing purpose you sure can have a String lines
"""

import LCS
from yattag import Doc, indent
import webbrowser


def getFileContent(path):
    with open(path) as f:
        return list(f)


def generateMarkUp(operations, A, B):
    doc, tag, text, line = Doc().ttl()
    with tag('html'):
        with tag('head'):
            doc._append('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">')
            doc._append('<script src="https://use.fontawesome.com/35ac922f38.js"></script>')
        with tag('body', klass='container bg-light'):
            line('h2', 'File Differ', klass='text-center display-2')
            with tag('div', klass='card'):
                with tag('div', klass='card-body'):
                    line('h4', 'File A content = ' + A)
                    doc._append('<br>')
                    line('h4', 'File B content = ' + B)

            line('h6', 'You Can Convert A To B with these operations', klass='text-center display-4')

            with tag('div', klass='container'):
                for op in operations:
                    if op[:3] == 'ADD':
                        with tag('div', klass="bg-success"):
                            line('i', '', klass="fa fa-plus mr-3 pull-right")
                            line('h3', op[3:], klass="text-white ml-5")
                    elif op[:3] == 'REM':
                        with tag('div', klass="bg-danger"):
                            line('i', '', klass="fa fa-remove mr-3 pull-right")
                            line('h3', op[3:], klass="text-white ml-5")
                    elif op[:3] == 'LCS':
                        with tag('div', klass="bg-primary"):
                            line('i', '', klass="fa fa-star mr-3 pull-right")
                            line('h3', op[3:], klass="text-white ml-5")
		doc._append('<h6>Developed by github/makaravind</h6>')
    return indent(doc.getvalue())


def saveMarkedUpContentToFile(content):
    with open('markedup.html', 'w') as f:
        f.write(content)


if __name__ == "__main__":
    A = getFileContent('textA.txt')
    B = getFileContent('textB.txt')
    ops = LCS.LongestCommonSubsequence(A, B)
    print 'operations to convert A->B', ops
    _A = ''.join(A)
    _B = ''.join(B)
    saveMarkedUpContentToFile(generateMarkUp(ops, _A, _B))
    webbrowser.open("http://localhost:63342/File_Differ/markedup.html", autoraise=False)

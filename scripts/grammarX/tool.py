import language_tool_python
import sys
from pathlib import Path
script_location = Path(__file__).absolute().parent


def checkGrammar(data):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(data)
    corrected = language_tool_python.utils.correct(data, matches)
    tool.close()
    formatAndDisplay(data, matches, corrected)


def formatAndDisplay(data='', matches=[], corrected=''):
    print('***'*30)
    print('Original Text')
    print('***'*30)
    print(data)
    print('***'*30)
    print('Grammar mistakes & Improvements')
    print('***'*30)
    for match in matches:
        incorrect_text = match.sentence.replace(match.matchedText, '\033[44;33m{}\033[m'.format(match.matchedText))
        rule_text = '\033[3;31;40m{}\033[m'.format(match.message)
        suggestion = '\033[4;32;40m{}\033[m'.format(match.replacements[0])
        print(f"{rule_text} => {incorrect_text}")
        print(f"Suggestion : {suggestion}")

    # Corrected ----------
    print('***'*30)
    print('CORRECTED TEXT')
    print('***'*30)
    print('\033[3;33;40m{}\033[m'.format(corrected))
    print('---'*30)


try:
    file_location = script_location / 'demoFile.txt'
    f = open(file_location, "r")
    fileText = f.read()
    checkGrammar(fileText)

except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = exception_traceback.tb_lineno
    print(f'line {line_number}: {exception_type} - {e}')

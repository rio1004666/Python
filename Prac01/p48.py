# Python에서 문자열은 막강한 기능을 제공한다
# 문자열은 문자들의 집합  단일따옴표(') 이중따옴표(") 삼중따옴표(''' or """)
# 삼중따옴표는 여러줄의 문자들을 저장할 때 사용한다
oneLine = "this is one line string"
print('한줄만 출력: ', oneLine)
multiLine = """
this is 
multi line 
string"""
print('삼중따옴표 여러줄 출력: ', multiLine)
multiLine2 = "this is \nmulit line \nstring";
print('개행문자로 여러줄 출력:', multiLine2)
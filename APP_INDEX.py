import requests
import streamlit as st
import streamlit.components.v1 as components

# def main():
#     with open("index.html", "r", encoding="utf-8") as file:
#         html_code = file.read()
#     # st.components.v1.html(html_code, height=1000, scrolling=True)
#     # 使用st.write函数将HTML内容显示到Streamlit应用程序中
#     st.write(html_code, unsafe_allow_html=True)


def main():
    components.iframe("index.html")



# write-html-2-mac.py
import webbrowser

f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///Users/username/Desktop/AnotherWorld/' + 'helloworld.html'
webbrowser.open_new_tab(filename)



if __name__ == "__main__":
    
    main()
import webbrowser
import webpage_generator

def webchange():
    f = open("staytuned.html", "w")
    message = """<html>
            <body><h1>Stay tuned for our amazing summer sale!</h1><p>
            {}</p></body></html>""".format(background.get)
    f.write(message)
    f.close()
    webbrowser.open_new_tab("staytuned.html")

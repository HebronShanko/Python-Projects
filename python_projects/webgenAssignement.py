

import os

from tkinter import *
import webpage_GUI
import webbrowser



def userInput(self):
    userInput =  self.txt_body.get()

   
    with open("WebPageGenerator.html", "w") as file1:
        file1.write("""<html> 
                 <body> 
                    <h1>
                    """
                       + userInput +   
                    """</h1>
                 </body> 
            </html>""")
        file1.close()
    
    # Reading from file

    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("WebPageGenerator.html")


if __name__ == "__main__":
    pass

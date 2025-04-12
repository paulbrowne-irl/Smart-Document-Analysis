# import required modules
from selenium import webdriver


# Driver Code
if __name__ == '__main__':

    # create object
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")

    # open browser and navigate to lambdatest Login Page
    edgeBrowser.get('https://www.lambdatest.com')


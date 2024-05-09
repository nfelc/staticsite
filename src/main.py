from textnode import TextNode

def main():
    Test = TextNode('this is a test', 'bold', 'https://www.boot.dev')

    print(Test.__repr__())


main()
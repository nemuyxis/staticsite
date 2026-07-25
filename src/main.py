from textnode import TextNode, TextType

def main():
    print("hello world")
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)

main()
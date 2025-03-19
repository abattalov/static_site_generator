from textnode import TextType, TextNode

def main():
    node = TextNode("hello world", TextType.TEXT)
    print(node)

if __name__ == "__main__":
    main()
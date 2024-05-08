from textnode import TextNode


def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    textnode2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode.__eq__(textnode2))
    print(textnode.__repr__())


if __name__ == '__main__':
    main()

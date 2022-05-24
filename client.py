import socket
from colors import greenText, yellowText, redText, blueText

def printColor (serverMessage):
    if serverMessage[0] == 'G':
        greenText(serverMessage[1])
    elif serverMessage[0] == 'Y':
        yellowText(serverMessage[1])
    elif serverMessage[0] == 'R':
        redText(serverMessage[1])
    elif serverMessage[0] == 'B':
        blueText(serverMessage[1])
    else:
        redText('Data sending ERROR')


if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))

    while True:
        greenText("1. Load and print data from the DB \n" +
                 "2. Add a new author \n" +
                 "3. Add a new book \n" +
                 "4. Edit an author \n" +
                 "5. Edit a book \n" +
                 "6. Delete an author \n" +
                 "7. Delete a book \n" +
                 "8. Find an author by id \n" +
                 "9. Find a book by id \n" +
                 "10. Print all authors \n" +
                 "11. Get books number \n" +
                 "12. Print all books \n" +
                 "13. Print all books of author \n" +
                 "14. Exit")
        greenText('Enter command:')
        command = int(input())
        query = str(command)

        if command == 1:
            s.send(query.encode())
        elif command == 2:
            greenText("Enter author's name: ")
            name = input()
            query = query + "#" + name
            s.send(query.encode())
        elif command == 3:
            greenText("Enter the author id: ")
            author_id = int(input())
            greenText("Enter the title: ")
            title = input()
            greenText("Enter the genre: ")
            genre = input()
            greenText("Enter the number of pages: ")
            pages = int(input())
            query = query + "#" + str(author_id) + '#' + title + '#' + genre + '#' + str(pages)
            s.send(query.encode())
        elif command == 4:
            greenText("Enter the author id: ")
            authorId = int(input())
            greenText("Enter new author name: ")
            authorName = input()
            query = query + "#" + str(authorId) + '#' + authorName
            s.send(query.encode())
        elif command == 5:
            greenText("Enter the book id: ")
            bookId = int(input())
            greenText("What do you want to edit? \n" +
                        "1. Title \n" +
                        "2. Genre \n" +
                        "3. Pages number")
            choice = int(input())
            if choice == 1:
                greenText("Enter new title: ")
                bookTitle = input()
                query = query + "#" + str(bookId) + '#' + str(choice) + '#' + bookTitle
            elif choice == 2:
                greenText("Enter new genre: ")
                bookGenre = input()
                query = query + "#" + str(bookId) + '#' + str(choice) + '#' + bookGenre
            elif choice == 3:
                greenText("Enter new number of pages: ")
                bookPages = int(input())
                query = query + "#" + str(bookId) + '#' + str(choice) + '#' + str(bookPages)
            else:
                redText("Unknown command")
                continue
            s.send(query.encode())
        elif command == 6:
            greenText("Enter the author id: ")
            authorId = int(input())
            query = query + "#" + str(authorId)
            s.send(query.encode())
        elif command == 7:
            greenText("Enter the book id: ")
            bookId = int(input())
            query = query + "#" + str(bookId)
            s.send(query.encode())
        elif command == 8:
            greenText("Enter the author id: ")
            authorId = int(input())
            query = query + "#" + str(authorId)
            s.send(query.encode())
        elif command == 9:
            greenText("Enter the book id: ")
            bookId = int(input())
            query = query + "#" + str(bookId)
            s.send(query.encode())
        elif command == 10:
            s.send(query.encode())
        elif command == 11:
            s.send(query.encode())
        elif command == 12:
            s.send(query.encode())
        elif command == 13:
            greenText("Enter the author id: ")
            authorId = int(input())
            query = query + "#" + str(authorId)
            s.send(query.encode())
        elif command == 14:
            s.send(query.encode())
            exit()
        else:
            s.send(query.encode())

        serverMessage = s.recv(1024).decode().split('#')
        printColor(serverMessage)
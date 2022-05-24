import socket
from author import Author
from book import Book
from library import Library

if __name__ == '__main__':
	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.bind((host, port))

	s.listen(5)
	print('Waiting for a client')
	conn, addr = s.accept()
	print('Got connection from ', addr)

	library = Library()
	while True:
		clientMessage = conn.recv(1024).decode().split('#')
		command = int(clientMessage[0])
		if command == 1:
			conn.send(library.loadFromDB().encode())
		elif command == 2:
			name = clientMessage[1]
			author = Author(0, name)
			conn.send(library.addAuthor(author).encode())
		elif command == 3:
			author_id = int(clientMessage[1])
			title = clientMessage[2]
			genre = clientMessage[3]
			pages = int(clientMessage[4])
			book = Book(0, author_id, title, genre, pages)
			conn.send(library.addBook(book).encode())
		elif command == 4:
			authorId = int(clientMessage[1])
			name = clientMessage[2]
			conn.send(library.editAuthor(authorId, name).encode())
		elif command == 5:
				bookId = int(clientMessage[1])
				action = int(clientMessage[2])
				changed = clientMessage[3]
				conn.send(library.editBook(bookId, action, changed).encode())
		elif command == 6:
			authorId = int(clientMessage[1])
			conn.send(library.deleteAuthor(authorId).encode())
		elif command == 7:
			bookId = int(clientMessage[1])
			conn.send(library.deleteBook(bookId).encode())
		elif command == 8:
			authorId = int(clientMessage[1])
			conn.send(library.getAuthor(authorId, True).encode())
		elif command == 9:
			bookId = int(clientMessage[1])
			conn.send(library.getBook(bookId, True).encode())
		elif command == 10:
			conn.send(library.printAllAuthors().encode())
		elif command == 11:
			conn.send(library.getBooksNumber().encode())
		elif command == 12:
			conn.send(library.printAllBooks().encode())
		elif command == 13:
			authorId = int(clientMessage[1])
			conn.send(library.printAllBooksOfAuthor(authorId).encode())
		elif command == 14:
			exit()
		else:
			conn.send('R#Unknown command'.encode())
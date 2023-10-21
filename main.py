import json

def main():
    #initializing an empty list
    booklist = []
    try:
     
        infile = open('library.txt', 'r')
        line = infile.readline()

        while line != "":
            line = line.rstrip("\n")
            newline = json.loads(line)
            booklist.append(newline)
            line = infile.readline()             
        infile.close()
        
    except FileNotFoundError :
        print("the <library.txt> file is not found ")
        print("Starting a new books list!")
    

    option = 0
    while option != 4:

        try:

            print('Choose from below menu')
            print('1. Add a book')
            print('2. Remove a book')
            print('3. View book details')
            print('4. Exit')

            option = int(input('Provide your choice : '))

            if option == 1:
                print('Provide details of the book to add: ')
                nbook= input('Enter name of the book: ')
                abook = input('Enter name of the author: ')
                pbook = input('Enter number of pages: ')
                newbook = {}
                newbook['name']= nbook
                newbook['author']= abook
                newbook['no_of_pages']= pbook
                # print(booklist)
                booklist.append(newbook)
                print(booklist)
                outfile = open('library.txt', 'a')
                newline = json.dumps(newbook)
                outfile.write(newline + "\n")
                outfile.close()
            elif option == 2:
                keyword = ''
                i = 0
                while True:
                    
                    keyword = input('Enter book name to remove: ')
                    if keyword != '':
                        break
                        # print('Please enter valid book name')
                        
                    else :
                        
                        print('Please enter valid book name')
                        
                        i+=1
                        
                        if i >= 3:
                            print('Max attempts reached. Please start over again')
                            
                    
                for x in booklist:
                    print('inside loop')
                    if keyword == x['name']:
                        print('keyword present')
                        booklist.remove(x)
                        print(booklist)
                        break
                        
                else :
                    print(f'No book found with name {keyword}')
            
                    
            elif option == 3:
                print(booklist)
                    

            elif option == 4 :
                print('Thank you for using the service')
                break

        except:
            print('Please provide valid input between 1 to 4')   


        outfile = open('library.txt', 'w')
        for book in booklist:
            newline = json.dumps(book)
            outfile.write(newline + "\n")
        outfile.close()


if __name__ == "__main__":
    main()
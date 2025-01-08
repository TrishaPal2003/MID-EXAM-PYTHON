class star_cinema:
    def __init__(self):
        self.hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no, cinema):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[id] = [['free' for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f'Show ID {id} does not exist.')
            return

        for row, col in seat_list:
            if row >= self.rows or col >= self.cols:
                print(f'Invalid seat: ({row}, {col}).')
                continue

            if self.seats[id][row][col] == 'booked':
                print(f'Seat ({row}, {col}) is already booked.')
            else:
                self.seats[id][row][col] = 'booked'
                print(f'Seat ({row}, {col}) booked successfully.')

    def view_show_list(self):
        if not self.show_list:
            print('No shows available.')
        else:
            for show in self.show_list:
                print(f'ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f'Show ID {id} does not exist.')
            return

        print(f'Available seats for Show ID {id}:')
        for row in range(self.rows):
            for col in range(self.cols):
                seat = self.seats[id][row][col]
                print(f'({row}, {col}): {seat}', end='\t')
            print()

cinema = star_cinema()
cinema = Hall(5, 5, 1, cinema)  # Example hall with 5 rows, 5 columns, hall_no = 1

run = True
while run:
    print("1. Entry Show")
    print("2. Book Seat")
    print("3. View Show List")
    print("4. View Available Seats")
    print("0. Exit")

    option = int(input('Enter Your Choice: '))

    if option == 1:
        id = int(input('Enter Show ID: '))class star_cinema:
    def __init__(self):
        self.hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)
#show entry system
#show id unique
#invalid seat massage


class Hall:
    def __init__(self, rows, cols, hall_no, cinema):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        

        cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[id] = [['free' for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f'Show ID {id} does not exist.')
            return

        for row, col in seat_list:
            if row >= self.rows or col >= self.cols:
                print(f'Invalid seat: ({row}, {col}).')
                continue

            if self.seats[id][row][col] == 'booked':
                print(f'Seat ({row}, {col}) is already booked.')
            else:
                self.seats[id][row][col] = 'booked'
                print(f'Seat ({row}, {col}) booked successfully.')

    def view_show_list(self):
        if not self.show_list:
            print('No shows available.')
        else:
            for show in self.show_list:
                print(f'ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}')
            print()
    def view_available_seats(self, id):
        if id not in self.seats:
            print(f'Show ID {id} does not exist.')
            return

        print(f'Available seats for Show ID {id}:')
        count_seat = 0
        for row in range(self.rows):
            for col in range(self.cols):
                seat = self.seats[id][row][col]
                if seat == 'free':
                    count_seat+=1
                print(f'({row}, {col}): {seat}', end='\t')
            print()
        print(f'total free seat: {count_seat}')

cinema = star_cinema()
cinema = Hall(5, 5, 3, cinema)  

cinema.entry_show('s1', 'Hami', '10-2-2025')
cinema.entry_show('s2', 'pusto', '11-2-2025')
cinema.entry_show('s3', 'pk', '12-2-2025')
print()
cinema.entry_show('s4', 'harry poter', '10-2-2025')
cinema.entry_show('s5', 'finding nimo', '10-2-2025')
cinema.entry_show('s6', 'moana', '10-2-2025')

run = True
while run:

    print(f'1.Kindly make your way into the cinema hall')
    print(f'0.Kindly make your way out of the cinema hall')

    option = int(input(f'Enter your choice: '))
    print()
    if option == 1:
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print()
        print("Welcome to our cinema Hall sir/mam!!")
        print()
        # print("1. Entry Show")
        print("1. Book Seat")
        print("2. View Show List")
        print("3. View Available Seats")
        print("0. back")

        option = int(input('Enter Your Choice: '))
        print(f'*************************************')

    # if option == 1:
    #     id = input('Enter Show ID: ')
    #     movie_name = input('Enter Movie Name: ')
    #     time = input('Enter Time: ')
    #     cinema.entry_show(id, movie_name, time)

        if option == 1:
            id = input('Enter Show ID: ')
            num_seats = int(input('Enter number of seats to book: '))
            seat_list = []
            for _ in range(num_seats):
                row =int(input(f'Enter row: '))
                col =int(input(f'Enter col: '))
                seat_list.append((row, col))
            cinema.book_seats(id, seat_list)

        elif option == 2:
            cinema.view_show_list()

        elif option == 3:
            id = input('Enter Show ID: ')
            cinema.view_available_seats(id)
        

        elif option == 0:
            print("return!!")
        else:
            print(f'Sorry, sir, this option is not available to choose from!')

        print(f'*************************************')

    elif option == 0:

        print(f'*************************************')
        print(f'Thank you! We look forward to seeing you again.')
        print(f'*************************************')
        run = False

    

        movie_name = input('Enter Movie Name: ')
        time = input('Enter Time: ')
        cinema.entry_show(id, movie_name, time)

    elif option == 2:
        id = int(input('Enter Show ID: '))
        num_seats = int(input('Enter number of seats to book: '))
        seat_list = []
        for _ in range(num_seats):
            row =int(input(f'Enter row: '))
            col =int(input(f'Enter col: '))
            seat_list.append((row, col))
        cinema.book_seats(id, seat_list)

    elif option == 3:
        cinema.view_show_list()

    elif option == 4:
        id = int(input('Enter Show ID: '))
        cinema.view_available_seats(id)

    elif option == 0:
        print('Goodbye!')
        run = False

    else:
        print('Invalid option. Try again.')

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
        id = int(input('Enter Show ID: '))
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

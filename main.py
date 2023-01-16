from clients import clients

if __name__ == '__main__':
    user_list = []
    add_user = 1

    def add_new_user():
        print("1:User\n2:Clint")
        input_user_type = int(input('Enter the number, Are you user or clint: '))
        full_name = str(input('Enter the full name: '))
        age = int(input('Enter the age: '))
        id = int(input('Enter the id: '))
        id_no = int(input('Enter the Id NO: '))
        emplyment_type = str(input('Eplyment type Full/ Part: '))
        add_new = int(input('Do you want add anther user, type (1): '))
        global add_user
        add_user = add_new
        clit = clients()

        if input_user_type == 1:
            clit.set_new_user(
                    user_type='User',
                    full_name=full_name,
                    age=age,
                    id=id,
                    id_no=id_no,
                    emplyment_type=emplyment_type,
                )
        else:
            clit.set_new_user(
                    user_type='Clint',
                    full_name=full_name,
                    age=age,
                    id=id,
                    id_no=id_no,
                    emplyment_type=emplyment_type,
                )
        user_info = clit.get_new_user()
        user_list.append(user_info)

    add_new_user()
    while add_user == 1:
        add_new_user()

    print('----------------------------------------')
    print(user_list)




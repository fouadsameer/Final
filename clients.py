class clients:
    user_type = ''
    user_info = {}

    def set_new_user(
            self,
            user_type,
            id,
            full_name,
            id_no,
            age,
            emplyment_type='full'
                     ):
        self.user_info = {
            'user_type':user_type,
            'id': id,
            'full_name': full_name,
            'id_no': id_no,
            'age':age,
            'emplyment_type':emplyment_type
        }

    def get_new_user(self):
        return self.user_info
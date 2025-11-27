class UserInputValidator:
    def validate_positvie_integers(self, values):

        valid_integers = []
        for v in values: 
            try: 
                number = int(v)
                if number >0:
                    valid_integers.append(number)
            except(ValueError, TypeError):
                pass
        return valid_integers

    def display_message(self, values):
        valid_v = self.validate_positvie_integers(values)
        if valid_v:
            print(f"list is validated, and contain the positive numbers: {valid_v} ")
        else:
            print('no positive numbers found ')


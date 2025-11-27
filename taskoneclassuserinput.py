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




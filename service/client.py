""" Class representing a client
    """
class Client():

    def __init__(self, name, last_name, doc_id):
        """ init client"""
        self.name = name
        self.last_name = last_name
        self.doc_id = doc_id
        self.preexistence = []

    def add_preexistence(self, n_preexistence):
        """ Add a preexistances"""
        self.preexistence.append(n_preexistence)
        return len(self.preexistence) - 1

    def get_preexistence(self, p_Index):
        """ Get a preexistance given the index"""
        if p_Index >= len(self.preexistence):
            return 'There is no such preexistence'

    def get_all_preexistence(self):
        """ Get all preexistances"""
        return self.preexistence

    def remove_preexistence(self, n_preexistence):
        """ Get all preexistances"""
        self.preexistence.pop(n_preexistence)
        return len(self.preexistence) - 1

    def get_formatted_name(self):
        """ Get full name"""
        return self.name + ' ' + self.last_name


if __name__ == '__main__':
    client_instance = Client('uno', 'dos', '113565')
    print('User Abbas has been added with id ', client_instance.get_formatted_name())

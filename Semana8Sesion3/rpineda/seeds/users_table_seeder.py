from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        with self.db.transaction():
            self.db.table('users').insert({
                'name': 'twittor',
                'email': 'twittor@twittor.com',
                'city': 'Lima'
            })
            self.db.table('users').insert({
                'name': 'john',
                'email': 'john@doe.com',
                'city': 'Quito'
            })
            self.db.table('users').insert({
                'name': 'jane',
                'email': 'jane@doe.com',
                'city': 'Chiclayo'
            })


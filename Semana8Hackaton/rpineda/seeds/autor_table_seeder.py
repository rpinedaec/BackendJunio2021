from orator.seeds import Seeder


class AutorTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('autor').insert({
            'nombre':'Javier Santaolalla',
            'descripcion': 'avier Santaolalla Camino nació en Burgos pero es canario de adopción y corazón.',
            'ideditorial': 1
        })
        self.db.table('autor').insert({
            'nombre':'Kip S. Thorne',
            'descripcion': 'Kip S. Thorne (n. 1940) ocupó hasta 2009 la cátedra Feynman de Física Teórica en el California Institute of Technology.',
            'ideditorial': 2
        })


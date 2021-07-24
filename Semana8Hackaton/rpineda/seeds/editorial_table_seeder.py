from orator.seeds import Seeder


class EditorialTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('editorial').insert({
            'nombre':'La Esfera de los Libros',
            'descripcion': 'La Esfera de los Libros'
        })
        self.db.table('editorial').insert({
            'nombre':'Editorial Crítica',
            'descripcion': 'Editorial Crítica'
        })


from orator.seeds import Seeder


class EstadoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('estado').insert({
            'nombre':'Activo',
            'descripcion': 'Activo'
        })
        self.db.table('estado').insert({
            'nombre':'Inactivo',
            'descripcion': 'Inactivo'
        })


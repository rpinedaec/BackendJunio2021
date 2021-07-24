from orator.seeds import Seeder


class EstadolibroTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('estadolibro').insert({
            'nombre': 'Disponible',
            'descripcion': 'Disponible'
        })
        self.db.table('estadolibro').insert({
            'nombre': 'Reservado',
            'descripcion': 'Reservado'
        })
        self.db.table('estadolibro').insert({
            'nombre': 'Prestado',
            'descripcion': 'Prestado'
        })

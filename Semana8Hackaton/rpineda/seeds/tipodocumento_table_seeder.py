from orator.seeds import Seeder


class TipodocumentoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('tipodocumento').insert({
            'nombre':'DNI',
            'descripcion': 'DNI'
        })
        self.db.table('tipodocumento').insert({
            'nombre':'CE',
            'descripcion': 'Carnet de Extranjeria'
        })
        self.db.table('tipodocumento').insert({
            'nombre':'RUC',
            'descripcion': 'RUC'
        })
        self.db.table('tipodocumento').insert({
            'nombre':'CM',
            'descripcion': 'Cedula Militar'
        })
        self.db.table('tipodocumento').insert({
            'nombre':'CB',
            'descripcion': 'Carnet Biblioteca'
        })


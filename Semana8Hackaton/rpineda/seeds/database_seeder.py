from orator.seeds import Seeder
from .estado_table_seeder import EstadoTableSeeder
from .estadolibro_table_seeder import EstadolibroTableSeeder
from .tipodocumento_table_seeder import TipodocumentoTableSeeder
from .editorial_table_seeder import EditorialTableSeeder
from .autor_table_seeder import AutorTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(EstadoTableSeeder)
        self.call(EstadolibroTableSeeder)
        self.call(TipodocumentoTableSeeder)
        self.call(EditorialTableSeeder)
        self.call(AutorTableSeeder)


from orator.migrations import Migration


class CreateEstadolibroTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('estadolibro') as table:
           table.increments('id')
           table.string('nombre')
           table.string('descripcion')
           table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('estadolibro')

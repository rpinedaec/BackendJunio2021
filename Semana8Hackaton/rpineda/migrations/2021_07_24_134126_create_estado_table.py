from orator.migrations import Migration


class CreateEstadoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('estado') as table:
           table.increments('id')
           table.string('nombre')
           table.string('descripcion')
           table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('estado')

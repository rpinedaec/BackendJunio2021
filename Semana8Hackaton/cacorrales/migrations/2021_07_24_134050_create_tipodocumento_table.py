from orator.migrations import Migration


class CreateTipodocumentoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tipodocumento') as table:
           table.increments('id')
           table.string('nombre')
           table.string('descripcion')
           table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tipodocumento')

from orator.migrations import Migration


class CreateAutorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('autor') as table:
           table.increments('id')
           table.string('nombre')
           table.string('descripcion')
           table.integer('ideditorial').unsigned()
           table.foreign('ideditorial').references('id').on('editorial')
           
           table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('autor')
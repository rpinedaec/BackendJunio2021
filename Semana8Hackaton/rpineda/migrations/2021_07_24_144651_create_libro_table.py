from orator.migrations import Migration


class CreateLibroTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('libro') as table:
            table.increments('id')
            table.string('nombre')
            table.string('descripcion')
            table.integer('autor_id').unsigned()
            table.foreign('autor_id').references('id').on('autor')
            table.integer('estado_libro_id').unsigned()
            table.foreign('estado_libro_id').references('id').on('estadolibro')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('libro')
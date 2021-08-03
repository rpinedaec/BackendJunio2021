from orator.migrations import Migration


class CreateLectorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('lector') as table:
           table.increments('id')
           table.string('nombre')
           table.string('correo')
           table.integer('idtipodocumento').unsigned()
           table.foreign('idtipodocumento').references('id').on('tipodocumento')
           table.string('documento')
           table.integer('idestado').unsigned()
           table.foreign('idestado').references('id').on('estado')
           table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('lector')


from cement import Controller, ex, fs
from cement.utils.version import get_version_banner
from ..core.version import get_version


VERSION_BANNER = """
obtencion, mantencion, ideas, etc. con informacion de digimon %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'obtencion, mantencion, ideas, etc. con informacion de digimon'

        # text displayed at the bottom of --help output
        epilog = 'Usage: digimondata command1 --foo bar'

        # controller level arguments. ex: 'digimondata --version'
        arguments = [
            ### add a version banner
            ( 
                [ '-v', '--version' ],
                { 
                    'action'  : 'version',
                    'version' : VERSION_BANNER 
                } 
            ),
            (
                ['-g','--get'],
                {
                    'help' : '[number of elements] or "all", Gets the number of elements or all elements from the DigimonAPI',
                    'action' : 'store',
                    'dest' : 'arg_element'
                }
           )
        ]


    def _default(self):
        """Default action if no sub-command is passed."""
        n_elements = 0
        response_result = None

        if self.app.pargs.arg_element is None:
            self.app.args.print_help()
        else:            
            arg_element = self.app.pargs.arg_element if 'arg_element' in self.app.pargs else None

            data_get_digi = self.app.api.get_digi(arg_element)
            
            if data_get_digi['success'] is False:
                self.app.log.error(data_get_digi['message'])
            else:
                data = data_get_digi['data']
                # insertar datos a la DB
                response_insert = self.app.db.insert_data_in_collection('digimon-collection', data)
                if response_insert['success'] is False:
                    self.app.log.error('Error al insertar carga\n{0}'.format(response_insert["message"]))
                else:                    
                    self.app.render(response_insert['data'], headers="keys")


    @ex(
        help='list a digimons on database, default priority [id, name, level]',
        arguments=[
            (
                ['-i','--id'],
                {
                    'help' : 'get digimon by id',
                    'action' : 'store',
                    'dest' : 'arg_id'
                }
            ),
            (
                ['-n','--name'],
                {
                    'help' : 'get digimon by name',
                    'action' : 'store',
                    'dest' : 'arg_name'
                }
            ),
            (
                ['-l','--level'],
                {
                    'help' : 'get digimon by level',
                    'action' : 'store',
                    'dest' : 'arg_level'
                }
            )
        ]
    )
    def listDigimon(self):
        response_result = None
        arg_id = self.app.pargs.arg_id if self.app.pargs.arg_id else None
        arg_name = self.app.pargs.arg_name if self.app.pargs.arg_name else None
        arg_level = self.app.pargs.arg_level if self.app.pargs.arg_level else None
        
        response_result = self.app.db.Buscar(arg_id, arg_name, arg_level)    

        if response_result["success"] is False:
            self.app.log.error(response_result["message"])
        else:
            self.app.render(response_result["data"], headers="keys")

    @ex(
        help='delete database',

        # sub-command level arguments. ex: 'digimondata command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            # ( [ '-f', '--foo' ],
            #   { 'help' : 'notorious foo option',
            #     'action'  : 'store',
            #     'dest' : 'foo' } ),
        ],
    )
    def deleteDb(self):
        """Example sub-command."""
        path, exist = fs.join_exists('.','database')
        if exist is True:
            for file in fs.os.listdir(path):
                fs.os.remove(fs.join(path, file))

            fs.os.removedirs(path)
        self.app.log.info('Eliminacion de carpeta de dababase : {0}'.format(path))
        

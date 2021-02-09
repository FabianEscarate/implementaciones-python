
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
        response_insert = None
        response_result = None

        if self.app.pargs.arg_element is None:
            self.app.args.print_help()
        else:            
            arg_element = self.app.pargs.arg_element
            if arg_element == 'all':
                n_elements = -1
            else:
                try:
                    n_elements = int(arg_element)                    
                except Exception as _ex:
                    self.app.log.error("Invalid value, can't convert str to int")

            data_get_digi = self.app.api.get_digi(n_elements)
            if data_get_digi['success'] is False:
                self.app.log.error(data['message'])
            else:
                data = data_get_digi['data']
                # insertar datos a la DB
                response_insert = self.app.db.insert_data_in_collection('digimon-collection', data)
                if response_insert['success'] is False:
                    self.app.log.error('Error al insertar carga')
                else:
                    data_inserted = response_insert['data']

            headers = ['success','data_inserted']
            self.app.render(response_insert, headers=headers)


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
        path = fs.abspath('.')
        self.app.log.info(path)
        

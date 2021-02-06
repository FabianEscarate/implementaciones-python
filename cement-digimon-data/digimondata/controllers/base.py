
from cement import Controller, ex
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
        if self.app.pargs.arg_element is None:
            self.app.args.print_help()
        else:
            n_elements = 0
            arg_element = self.app.pargs.arg_element
            if arg_element == 'all':
                n_elements = -1
            else:
                try:
                    n_elements = int(arg_element)                    
                except Exception as _ex:
                    self.app.log.error("Invalid value, can't convert str to int")

            self.app.log.info('Obtencion de {0} elementos'.format('todo' if n_elements < 0 else n_elements))
            data_get_digi = self.app.api.get_digi(n_elements)
            if data['success'] is False:
                self.app.log.info(data['message'])
            else:
                data = data['data']
                # insertar datos a la DB



    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'digimondata command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-f', '--foo' ],
              { 'help' : 'notorious foo option',
                'action'  : 'store',
                'dest' : 'foo' } ),
        ],
    )
    def command1(self):
        """Example sub-command."""

        data = {
            'foo' : 'bar',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'command1.jinja2')

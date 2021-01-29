
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import DigimonDataError
from .controllers.base import Base

from .db.connection import ConnectionManager

# configuration defaults
CONFIG = init_defaults('digimondata')
CONFIG['digimondata']['foo'] = 'bar'

# preparacion de base de datos
def config_db_manager(app):
    app.log.info('configuracion y conexion a base de datos')
    database_info_dict = app.config['DATABASE']

    app.extend('db', ConnectionManager(database_info_dict))

class DigimonData(App):
    """digimon-data primary application."""

    class Meta:
        label = 'digimondata'

        # configuration defaults
        # config_defaults = CONFIG
        config_files = ['config/digimondata.yml']
        

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base
        ]

        # Hooks
        hooks = [
            ('post_setup', config_db_manager),
        ]


class DigimonDataTest(TestApp,DigimonData):
    """A sub-class of DigimonData that is better suited for testing."""

    class Meta:
        label = 'digimondata'


def main():
    with DigimonData() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except DigimonDataError as e:
            print('DigimonDataError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()

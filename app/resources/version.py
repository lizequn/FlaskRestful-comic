import logging
from flask.views import MethodView
from tomlkit.toml_file import TOMLFile
from app.main import app

'''
Get current running version
'''


class VersionResource(MethodView):

    def get(self):
        logging.debug("version-get")
        poetry_config = app.config['POETRY_CONFIG']
        toml = TOMLFile(poetry_config)
        content = toml.read()
        info_key = ['name', 'version', 'description', 'authors']
        info = content['tool']['poetry']
        return {key: info[key] for key in info_key}

from yapsy.VersionedPluginManager import VersionedPluginManager


class PluginManager():
    ''' Its purpose is to provide more integrated way to manage modules/ plugins. '''
    def __init__(self, plugin_dir, debug = False):
        self.plugin_dir = plugin_dir
        self.spm = VersionedPluginManager()
        self.spm.setPluginPlaces([self.plugin_dir])
        self.spm.collectPlugins()
        self.available_plugins = []
        self.debug = debug
from ._base import Base

__all__ = ["Plugins"]


class Plugins(Base):

    def upload_plugin(self, files, data=None):
        """Upload plugin

        plugin: The plugin image to be uploaded
        force: Set to 'true' to overwrite a previously installed plugin with the same ID, if any

        `Read in Mattermost API docs (plugins - UploadPlugin) <https://api.mattermost.com/#tag/plugins/operation/UploadPlugin>`_

        """
        return self.client.post("""/api/v4/plugins""", files=files, data=data)

    def get_plugins(self):
        """Get plugins
        `Read in Mattermost API docs (plugins - GetPlugins) <https://api.mattermost.com/#tag/plugins/operation/GetPlugins>`_

        """
        return self.client.get("""/api/v4/plugins""")

    def install_plugin_from_url(self):
        """Install plugin from url
        `Read in Mattermost API docs (plugins - InstallPluginFromUrl) <https://api.mattermost.com/#tag/plugins/operation/InstallPluginFromUrl>`_

        """
        return self.client.post("""/api/v4/plugins/install_from_url""")

    def remove_plugin(self, plugin_id):
        """Remove plugin

        plugin_id: Id of the plugin to be removed

        `Read in Mattermost API docs (plugins - RemovePlugin) <https://api.mattermost.com/#tag/plugins/operation/RemovePlugin>`_

        """
        return self.client.delete(f"/api/v4/plugins/{plugin_id}")

    def enable_plugin(self, plugin_id):
        """Enable plugin

        plugin_id: Id of the plugin to be enabled

        `Read in Mattermost API docs (plugins - EnablePlugin) <https://api.mattermost.com/#tag/plugins/operation/EnablePlugin>`_

        """
        return self.client.post(f"/api/v4/plugins/{plugin_id}/enable")

    def disable_plugin(self, plugin_id):
        """Disable plugin

        plugin_id: Id of the plugin to be disabled

        `Read in Mattermost API docs (plugins - DisablePlugin) <https://api.mattermost.com/#tag/plugins/operation/DisablePlugin>`_

        """
        return self.client.post(f"/api/v4/plugins/{plugin_id}/disable")

    def get_webapp_plugins(self):
        """Get webapp plugins
        `Read in Mattermost API docs (plugins - GetWebappPlugins) <https://api.mattermost.com/#tag/plugins/operation/GetWebappPlugins>`_

        """
        return self.client.get("""/api/v4/plugins/webapp""")

    def get_plugin_statuses(self):
        """Get plugins status
        `Read in Mattermost API docs (plugins - GetPluginStatuses) <https://api.mattermost.com/#tag/plugins/operation/GetPluginStatuses>`_

        """
        return self.client.get("""/api/v4/plugins/statuses""")

    def install_marketplace_plugin(self, options):
        """Installs a marketplace plugin

        id: The ID of the plugin to install.
        version: The version of the plugin to install.

        `Read in Mattermost API docs (plugins - InstallMarketplacePlugin) <https://api.mattermost.com/#tag/plugins/operation/InstallMarketplacePlugin>`_

        """
        return self.client.post("""/api/v4/plugins/marketplace""", options=options)

    def get_marketplace_plugins(self, params=None):
        """Gets all the marketplace plugins

        page: Page number to be fetched. (not yet implemented)
        per_page: Number of item per page. (not yet implemented)
        filter: Set to filter plugins by ID, name, or description.
        server_version: Set to filter minimum plugin server version. (not yet implemented)
        local_only: Set true to only retrieve local plugins.

        `Read in Mattermost API docs (plugins - GetMarketplacePlugins) <https://api.mattermost.com/#tag/plugins/operation/GetMarketplacePlugins>`_

        """
        return self.client.get("""/api/v4/plugins/marketplace""", params=params)

    def get_marketplace_visited_by_admin(self):
        """Get if the Plugin Marketplace has been visited by at least an admin.
        `Read in Mattermost API docs (plugins - GetMarketplaceVisitedByAdmin) <https://api.mattermost.com/#tag/plugins/operation/GetMarketplaceVisitedByAdmin>`_

        """
        return self.client.get("""/api/v4/plugins/marketplace/first_admin_visit""")

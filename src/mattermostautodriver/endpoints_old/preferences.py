from ._base import Base

__all__ = ["Preferences"]


class Preferences(Base):

    def get_preferences(self, user_id):
        """Get the user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - GetPreferences) <https://api.mattermost.com/#tag/preferences/operation/GetPreferences>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences")

    def update_preferences(self, user_id, options):
        """Save the user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - UpdatePreferences) <https://api.mattermost.com/#tag/preferences/operation/UpdatePreferences>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/preferences", options=options)

    def delete_preferences(self, user_id, options):
        """Delete user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - DeletePreferences) <https://api.mattermost.com/#tag/preferences/operation/DeletePreferences>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/preferences/delete", options=options)

    def get_preferences_by_category(self, user_id, category):
        """List a user's preferences by category

        user_id: User GUID
        category: The category of a group of preferences

        `Read in Mattermost API docs (preferences - GetPreferencesByCategory) <https://api.mattermost.com/#tag/preferences/operation/GetPreferencesByCategory>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences/{category}")

    def get_preferences_by_category_by_name(self, user_id, category, preference_name):
        """Get a specific user preference

        user_id: User GUID
        category: The category of a group of preferences
        preference_name: The name of the preference

        `Read in Mattermost API docs (preferences - GetPreferencesByCategoryByName) <https://api.mattermost.com/#tag/preferences/operation/GetPreferencesByCategoryByName>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences/{category}/name/{preference_name}")

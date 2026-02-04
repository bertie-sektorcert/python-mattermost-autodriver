from ._base import Base

__all__ = ["Recaps"]


class Recaps(Base):

    def create_recap(self, options):
        """Create a channel recap

        title: Title for the recap
        channel_ids: List of channel IDs to include in the recap
        agent_id: ID of the AI agent to use for generating the recap

        `Read in Mattermost API docs (recaps - CreateRecap) <https://developers.mattermost.com/api-documentation/#/operations/CreateRecap>`_

        """
        return self.client.post("""/api/v4/recaps""", options=options)

    def get_recaps_for_user(self, params=None):
        """Get current user's recaps

        page: The page to select.
        per_page: The number of recaps per page.

        `Read in Mattermost API docs (recaps - GetRecapsForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetRecapsForUser>`_

        """
        return self.client.get("""/api/v4/recaps""", params=params)

    def get_recap(self, recap_id):
        """Get a specific recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - GetRecap) <https://developers.mattermost.com/api-documentation/#/operations/GetRecap>`_

        """
        return self.client.get(f"/api/v4/recaps/{recap_id}")

    def delete_recap(self, recap_id):
        """Delete a recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - DeleteRecap) <https://developers.mattermost.com/api-documentation/#/operations/DeleteRecap>`_

        """
        return self.client.delete(f"/api/v4/recaps/{recap_id}")

    def mark_recap_as_read(self, recap_id):
        """Mark a recap as read

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - MarkRecapAsRead) <https://developers.mattermost.com/api-documentation/#/operations/MarkRecapAsRead>`_

        """
        return self.client.post(f"/api/v4/recaps/{recap_id}/read")

    def regenerate_recap(self, recap_id):
        """Regenerate a recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - RegenerateRecap) <https://developers.mattermost.com/api-documentation/#/operations/RegenerateRecap>`_

        """
        return self.client.post(f"/api/v4/recaps/{recap_id}/regenerate")

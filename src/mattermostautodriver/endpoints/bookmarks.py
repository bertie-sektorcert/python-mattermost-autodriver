from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Bookmarks"]


class Bookmarks(Base):

    def list_channel_bookmarks_for_channel(self, channel_id: str, bookmarks_since: float | None = None):
        """Get channel bookmarks for Channel

        channel_id: Channel GUID
        bookmarks_since: Timestamp to filter the bookmarks with. If set, the
        endpoint returns bookmarks that have been added, updated
        or deleted since its value


        `Read in Mattermost API docs (bookmarks - ListChannelBookmarksForChannel) <https://api.mattermost.com/#tag/bookmarks/operation/ListChannelBookmarksForChannel>`_

        """
        __params = {"bookmarks_since": bookmarks_since}
        return self.client.get(f"/api/v4/channels/{channel_id}/bookmarks", params=__params)

    def create_channel_bookmark(
        self,
        channel_id: str,
        display_name: str,
        type: str,
        file_id: str | None = None,
        link_url: str | None = None,
        image_url: str | None = None,
        emoji: str | None = None,
    ):
        """Create channel bookmark

        channel_id: Channel GUID
        file_id: The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
        display_name: The name of the channel bookmark
        link_url: The URL associated with the channel bookmark. Required for bookmarks of type 'link'
        image_url: The URL of the image associated with the channel bookmark. Optional, only applies for bookmarks of type 'link'
        emoji: The emoji of the channel bookmark
        type: * ``link`` for channel bookmarks that reference a link. ``link_url`` is requied
        * ``file`` for channel bookmarks that reference a file. ``file_id`` is required


        `Read in Mattermost API docs (bookmarks - CreateChannelBookmark) <https://api.mattermost.com/#tag/bookmarks/operation/CreateChannelBookmark>`_

        """
        __options = {
            "file_id": file_id,
            "display_name": display_name,
            "link_url": link_url,
            "image_url": image_url,
            "emoji": emoji,
            "type": type,
        }
        return self.client.post(f"/api/v4/channels/{channel_id}/bookmarks", options=__options)

    def update_channel_bookmark(
        self,
        channel_id: str,
        bookmark_id: str,
        file_id: str | None = None,
        display_name: str | None = None,
        sort_order: int | None = None,
        link_url: str | None = None,
        image_url: str | None = None,
        emoji: str | None = None,
        type: str | None = None,
    ):
        """Update channel bookmark

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID
        file_id: The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
        display_name: The name of the channel bookmark
        sort_order: The order of the channel bookmark
        link_url: The URL associated with the channel bookmark. Required for type bookmarks of type 'link'
        image_url: The URL of the image associated with the channel bookmark
        emoji: The emoji of the channel bookmark
        type: * ``link`` for channel bookmarks that reference a link. ``link_url`` is requied
        * ``file`` for channel bookmarks that reference a file. ``file_id`` is required


        `Read in Mattermost API docs (bookmarks - UpdateChannelBookmark) <https://api.mattermost.com/#tag/bookmarks/operation/UpdateChannelBookmark>`_

        """
        __options = {
            "file_id": file_id,
            "display_name": display_name,
            "sort_order": sort_order,
            "link_url": link_url,
            "image_url": image_url,
            "emoji": emoji,
            "type": type,
        }
        return self.client.patch(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}", options=__options)

    def delete_channel_bookmark(self, channel_id: str, bookmark_id: str):
        """Delete channel bookmark

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID

        `Read in Mattermost API docs (bookmarks - DeleteChannelBookmark) <https://api.mattermost.com/#tag/bookmarks/operation/DeleteChannelBookmark>`_

        """
        return self.client.delete(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}")

    def update_channel_bookmark_sort_order(self, channel_id: str, bookmark_id: str, options: float | None = None):
        """Update channel bookmark's order

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID

        `Read in Mattermost API docs (bookmarks - UpdateChannelBookmarkSortOrder) <https://api.mattermost.com/#tag/bookmarks/operation/UpdateChannelBookmarkSortOrder>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order", options=options)

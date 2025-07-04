from ._base import Base
from typing import Any, BinaryIO

__all__ = ["SharedChannels"]


class SharedChannels(Base):

    def get_all_shared_channels(self, team_id: str, page: int | None = 0, per_page: int | None = 0):
        """Get all shared channels for team.

        team_id: Team Id
        page: The page to select.
        per_page: The number of sharedchannels per page.

        `Read in Mattermost API docs (shared_channels - GetAllSharedChannels) <https://api.mattermost.com/#tag/shared_channels/operation/GetAllSharedChannels>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/sharedchannels/{team_id}", params=__params)

    def get_shared_channel_remotes_by_remote_cluster(
        self,
        remote_id: str,
        include_unconfirmed: bool | None = None,
        exclude_confirmed: bool | None = None,
        exclude_home: bool | None = None,
        exclude_remote: bool | None = None,
        include_deleted: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ):
        """Get shared channel remotes by remote cluster.

        remote_id: The remote cluster GUID
        include_unconfirmed: Include those Shared channel remotes that are unconfirmed
        exclude_confirmed: Show only those Shared channel remotes that are not confirmed yet
        exclude_home: Show only those Shared channel remotes that were shared with this server
        exclude_remote: Show only those Shared channel remotes that were shared from this server
        include_deleted: Include those Shared channel remotes that have been deleted
        page: The page to select
        per_page: The number of shared channels per page

        `Read in Mattermost API docs (shared_channels - GetSharedChannelRemotesByRemoteCluster) <https://api.mattermost.com/#tag/shared_channels/operation/GetSharedChannelRemotesByRemoteCluster>`_

        """
        __params = {
            "include_unconfirmed": include_unconfirmed,
            "exclude_confirmed": exclude_confirmed,
            "exclude_home": exclude_home,
            "exclude_remote": exclude_remote,
            "include_deleted": include_deleted,
            "page": page,
            "per_page": per_page,
        }
        return self.client.get(f"/api/v4/remotecluster/{remote_id}/sharedchannelremotes", params=__params)

    def get_remote_cluster_info(self, remote_id: str):
        """Get remote cluster info by ID for user.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (shared_channels - GetRemoteClusterInfo) <https://api.mattermost.com/#tag/shared_channels/operation/GetRemoteClusterInfo>`_

        """
        return self.client.get(f"/api/v4/sharedchannels/remote_info/{remote_id}")

    def invite_remote_cluster_to_channel(self, remote_id: str, channel_id: str):
        """Invites a remote cluster to a channel.

        remote_id: The remote cluster GUID
        channel_id: The channel GUID to invite the remote cluster to

        `Read in Mattermost API docs (shared_channels - InviteRemoteClusterToChannel) <https://api.mattermost.com/#tag/shared_channels/operation/InviteRemoteClusterToChannel>`_

        """
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/invite")

    def uninvite_remote_cluster_to_channel(self, remote_id: str, channel_id: str):
        """Uninvites a remote cluster to a channel.

        remote_id: The remote cluster GUID
        channel_id: The channel GUID to uninvite the remote cluster to

        `Read in Mattermost API docs (shared_channels - UninviteRemoteClusterToChannel) <https://api.mattermost.com/#tag/shared_channels/operation/UninviteRemoteClusterToChannel>`_

        """
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/uninvite")

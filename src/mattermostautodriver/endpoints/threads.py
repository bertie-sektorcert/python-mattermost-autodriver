from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Threads"]


class Threads(Base):

    def get_user_threads(
        self,
        user_id: str,
        team_id: str,
        since: int | None = None,
        deleted: bool | None = False,
        extended: bool | None = False,
        page: int | None = 0,
        per_page: int | None = 60,
        totalsOnly: bool | None = False,
        threadsOnly: bool | None = False,
    ):
        """Get all threads that user is following

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        since: Since filters the threads based on their LastUpdateAt timestamp.
        deleted: Deleted will specify that even deleted threads should be returned (For mobile sync).
        extended: Extended will enrich the response with participant details.
        page: Page specifies which part of the results to return, by per_page.
        per_page: The size of the returned chunk of results.
        totalsOnly: Setting this to true will only return the total counts.
        threadsOnly: Setting this to true will only return threads.

        `Read in Mattermost API docs (threads - GetUserThreads) <https://api.mattermost.com/#tag/threads/operation/GetUserThreads>`_

        """
        __params = {
            "since": since,
            "deleted": deleted,
            "extended": extended,
            "page": page,
            "per_page": per_page,
            "totalsOnly": totalsOnly,
            "threadsOnly": threadsOnly,
        }
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/threads", params=__params)

    def get_thread_mention_counts_by_channel(self, user_id: str, team_id: str):
        """Get all unread mention counts from followed threads, per-channel

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.

        `Read in Mattermost API docs (threads - GetThreadMentionCountsByChannel) <https://api.mattermost.com/#tag/threads/operation/GetThreadMentionCountsByChannel>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/threads/mention_counts")

    def update_threads_read_for_user(self, user_id: str, team_id: str):
        """Mark all threads that user is following as read

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.

        `Read in Mattermost API docs (threads - UpdateThreadsReadForUser) <https://api.mattermost.com/#tag/threads/operation/UpdateThreadsReadForUser>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/teams/{team_id}/threads/read")

    def update_thread_read_for_user(self, user_id: str, team_id: str, thread_id: str, timestamp: str):
        """Mark a thread that user is following read state to the timestamp

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to update
        timestamp: The timestamp to which the thread's "last read" state will be reset.

        `Read in Mattermost API docs (threads - UpdateThreadReadForUser) <https://api.mattermost.com/#tag/threads/operation/UpdateThreadReadForUser>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}")

    def set_thread_unread_by_post_id(self, user_id: str, team_id: str, thread_id: str, post_id: str):
        """Mark a thread that user is following as unread based on a post id

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to update
        post_id: The ID of a post belonging to the thread to mark as unread.

        `Read in Mattermost API docs (threads - SetThreadUnreadByPostId) <https://api.mattermost.com/#tag/threads/operation/SetThreadUnreadByPostId>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}")

    def start_following_thread(self, user_id: str, team_id: str, thread_id: str):
        """Start following a thread

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to follow

        `Read in Mattermost API docs (threads - StartFollowingThread) <https://api.mattermost.com/#tag/threads/operation/StartFollowingThread>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following")

    def stop_following_thread(self, user_id: str, team_id: str, thread_id: str):
        """Stop following a thread

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to update

        `Read in Mattermost API docs (threads - StopFollowingThread) <https://api.mattermost.com/#tag/threads/operation/StopFollowingThread>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following")

    def get_user_thread(self, user_id: str, team_id: str, thread_id: str):
        """Get a thread followed by the user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to follow

        `Read in Mattermost API docs (threads - GetUserThread) <https://api.mattermost.com/#tag/threads/operation/GetUserThread>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}")

from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Authentication"]


class Authentication(Base):

    def migrate_auth_to_ldap(self, from_: str, match_field: str, force: bool):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (authentication - MigrateAuthToLdap) <https://api.mattermost.com/#tag/authentication/operation/MigrateAuthToLdap>`_

        """
        __options = {"from": from_, "match_field": match_field, "force": force}
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=__options)

    def migrate_auth_to_saml(self, from_: str, matches: dict[str, Any], auto: bool):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (authentication - MigrateAuthToSaml) <https://api.mattermost.com/#tag/authentication/operation/MigrateAuthToSaml>`_

        """
        __options = {"from": from_, "matches": matches, "auto": auto}
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=__options)

from ._base import Base

__all__ = ["SAML"]


class SAML(Base):

    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (SAML - MigrateAuthToSaml) <https://api.mattermost.com/#tag/SAML/operation/MigrateAuthToSaml>`_

        """
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=options)

    def get_saml_metadata(self):
        """Get metadata
        `Read in Mattermost API docs (SAML - GetSamlMetadata) <https://api.mattermost.com/#tag/SAML/operation/GetSamlMetadata>`_

        """
        return self.client.get("""/api/v4/saml/metadata""")

    def get_saml_metadata_from_idp(self, options=None):
        """Get metadata from Identity Provider

        saml_metadata_url: The URL from which to retrieve the SAML IDP data.

        `Read in Mattermost API docs (SAML - GetSamlMetadataFromIdp) <https://api.mattermost.com/#tag/SAML/operation/GetSamlMetadataFromIdp>`_

        """
        return self.client.post("""/api/v4/saml/metadatafromidp""", options=options)

    def upload_saml_idp_certificate(self, files, data=None):
        """Upload IDP certificate

        certificate: The IDP certificate file

        `Read in Mattermost API docs (SAML - UploadSamlIdpCertificate) <https://api.mattermost.com/#tag/SAML/operation/UploadSamlIdpCertificate>`_

        """
        return self.client.post("""/api/v4/saml/certificate/idp""", files=files, data=data)

    def delete_saml_idp_certificate(self):
        """Remove IDP certificate
        `Read in Mattermost API docs (SAML - DeleteSamlIdpCertificate) <https://api.mattermost.com/#tag/SAML/operation/DeleteSamlIdpCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/idp""")

    def upload_saml_public_certificate(self, files, data=None):
        """Upload public certificate

        certificate: The public certificate file

        `Read in Mattermost API docs (SAML - UploadSamlPublicCertificate) <https://api.mattermost.com/#tag/SAML/operation/UploadSamlPublicCertificate>`_

        """
        return self.client.post("""/api/v4/saml/certificate/public""", files=files, data=data)

    def delete_saml_public_certificate(self):
        """Remove public certificate
        `Read in Mattermost API docs (SAML - DeleteSamlPublicCertificate) <https://api.mattermost.com/#tag/SAML/operation/DeleteSamlPublicCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/public""")

    def upload_saml_private_certificate(self, files, data=None):
        """Upload private key

        certificate: The private key file

        `Read in Mattermost API docs (SAML - UploadSamlPrivateCertificate) <https://api.mattermost.com/#tag/SAML/operation/UploadSamlPrivateCertificate>`_

        """
        return self.client.post("""/api/v4/saml/certificate/private""", files=files, data=data)

    def delete_saml_private_certificate(self):
        """Remove private key
        `Read in Mattermost API docs (SAML - DeleteSamlPrivateCertificate) <https://api.mattermost.com/#tag/SAML/operation/DeleteSamlPrivateCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/private""")

    def get_saml_certificate_status(self):
        """Get certificate status
        `Read in Mattermost API docs (SAML - GetSamlCertificateStatus) <https://api.mattermost.com/#tag/SAML/operation/GetSamlCertificateStatus>`_

        """
        return self.client.get("""/api/v4/saml/certificate/status""")

    def reset_saml_auth_data_to_email(self, options=None):
        """Reset AuthData to Email

        include_deleted: Whether to include deleted users.
        dry_run: If set to true, the number of users who would be affected is returned.
        user_ids: If set to a non-empty array, then users whose IDs are not in the array will be excluded.

        `Read in Mattermost API docs (SAML - ResetSamlAuthDataToEmail) <https://api.mattermost.com/#tag/SAML/operation/ResetSamlAuthDataToEmail>`_

        """
        return self.client.post("""/api/v4/saml/reset_auth_data""", options=options)

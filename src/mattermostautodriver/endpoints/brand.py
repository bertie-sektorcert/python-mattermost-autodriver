from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Brand"]


class Brand(Base):

    def get_brand_image(self):
        """Get brand image
        `Read in Mattermost API docs (brand - GetBrandImage) <https://api.mattermost.com/#tag/brand/operation/GetBrandImage>`_

        """
        return self.client.get("""/api/v4/brand/image""")

    def upload_brand_image(self, image: BinaryIO):
        """Upload brand image

        image: The image to be uploaded

        `Read in Mattermost API docs (brand - UploadBrandImage) <https://api.mattermost.com/#tag/brand/operation/UploadBrandImage>`_

        """
        __files = {"image": image}
        return self.client.post("""/api/v4/brand/image""", files=__files)

    def delete_brand_image(self):
        """Delete current brand image
        `Read in Mattermost API docs (brand - DeleteBrandImage) <https://api.mattermost.com/#tag/brand/operation/DeleteBrandImage>`_

        """
        return self.client.delete("""/api/v4/brand/image""")

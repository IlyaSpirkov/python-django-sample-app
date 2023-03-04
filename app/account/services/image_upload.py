import os
from hashlib import blake2s

import boto3
from botocore import exceptions
from django.conf import settings


class ImageUploader:
    BUCKET_NAME = settings.BUCKET_NAME
    BUCKET_DIR = settings.BUCKET_DIR

    def upload_avatar_to_s3(self, file, user_id: int) -> str | None:
        path = self._generate_path(file.name, user_id)
        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            s3.upload_fileobj(file, self.BUCKET_NAME, path)
        except exceptions.BotoCoreError as e:
            return
        return self._generate_link(path)

    def _generate_path(self, filename: str, user_id: int) -> str:
        new_filename = blake2s(bytes(str(user_id), encoding="utf-8")).hexdigest()
        old_name, ext = os.path.splitext(filename)
        new_filename += ext
        return f"{self.BUCKET_DIR}{new_filename}"

    def _generate_link(self, path: str) -> str:
        return f"https://{self.BUCKET_NAME}.s3.us-east-2.amazonaws.com/{path}"

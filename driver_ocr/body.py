## imports
import io
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.oauth2 import service_account


class Drive_OCR:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.SCOPES = ['https://www.googleapis.com/auth/drive']

        # TODO: add the json key file received from google cloud project
        self.credentials = r"D:\harel\הראל\עבודה\פרויקטים\weedex\harelproj-47493ecd8ae9.json"
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials

        # If you have drive account you can add folder id
        # self.folder_id = "1iH-iCIFArFqUTwChE0fSBgdQV35zrkQi"

    def upkouading_image(self):
        """
        Upload image to directory in your drive
        :return: file id.
        """
        global service, file
        # For Uploading Image into Drive
        service = build('drive', 'v3', credentials=self.creds)
        mime = 'application/vnd.google-apps.document'
        file_metadata = {'name': self.filename, 'mimeType': mime}  # , 'parents': [self.folder_id]
        file = service.files().create(
            body=file_metadata,
            media_body=MediaFileUpload(self.filename, mimetype=mime, resumable=True),
            fields='id'
        ).execute()

        print('File ID: %s' % file.get('id'))

    def downloading(self):
        """
        Downloading the result from the Driver OCR.
        :return:
        """
        global fh
        # For Downloading Doc Image data by request
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

    def main(self) -> str:

        """ Drive v3 API.
        1. Uploading image to drive ocr api
        2. Downloading result
        3. Delete image from drive api
        4. Decode result
        return: Text
        """
        global request
        self.creds = service_account.Credentials.from_service_account_file(self.credentials, scopes=self.SCOPES)

        # uploading image
        self.upkouading_image()

        # It will export drive image into Doc
        request = service.files().export_media(fileId=file.get('id'), mimeType="text/plain")

        # For Downloading Doc Image data by request
        self.downloading()

        # It will delete the file from drive base on ID
        service.files().delete(fileId=file.get('id')).execute()

        # It will print data into terminal
        output = fh.getvalue().decode()

        return output




if __name__ == '__main__':
    image_path = r""
    ob = Drive_OCR(image_path)
    print(ob.main())




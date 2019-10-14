"""
====================================
Author: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
Date: 10/09/2019
====================================
Class for downloading images
from Google.
====================================
"""


from google_images_download import google_images_download


class ImagesDownloader(object):
    """Class for downloading images from Google."""
    def __init__(self, path = "\."):
        """Constructor for the class.

        It takes the path of the directory
        where the class will save the downloaded images."""
        self.path = path

    def download_images(self, limit, categories, output_dir, img_format):
        """It downloads the images of the given categories
        from Google."""
        response = google_images_download.googleimagesdownload() # Instance for the class.
        kwords = ",".join(categories)
        arguments = {
                        "keywords": kwords,

                        "limit": limit, 

                        "print_urls": False,

                        "output_directory":output_dir, 

                        "chromedriver":"C:\\Users\\User\\Desktop\\Chromedriver\\chromedriver",
                        #"chromedriver": "C:\\Users\\Johann\\Desktop\\chromedriver", # Path to chromedriver.

                        "format": img_format # jpg, png, etc...
                    }
        paths = response.download(arguments)

if __name__ == "__main__":
    # Example.
    img_downloader = ImagesDownloader()
    img_downloader.download_images(50, ["Rhino","Bird","Elephant","pencil","Airplane","fish"], "data", "jpg")
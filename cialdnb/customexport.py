from scrapy.extensions.feedexport import FileFeedStorage


class OverwriteFileFeedStorage(FileFeedStorage):
    """
    A File Feed Storage extension that overwrites existing files.
    """

    def __init__(self, uri, *, feed_options=None):
        super().__init__(uri=uri, feed_options=feed_options)
        self.write_mode = 'wb'

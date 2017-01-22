from IprBase import IprDownloader

class IprDownloaderPg(IprDownloader):
    def __init__(self, dbname, dbhost=None, dbport=None, dbuser=None, dbpasswd=None, dbschema=None):
        IprDownloader.__init__(self)
        self.dbname = dbname
        self.dbhost = dbhost
        self.dbport = dbport
        self.dbuser = dbuser
        self.dbpasswd = dbpasswd
        self.dbschema = dbschema

    def import_data(self, crs, overwrite):
        def conn_string():
            dbconn = 'PG:dbname={0}'.format(self.dbname)
            if self.dbhost:
                dbconn += ' host={0}'.format(self.dbhost)
            if self.dbport:
                dbconn += ' port={0}'.format(self.dbport)
            if self.dbuser:
                dbconn += ' user={0}'.format(self.dbuser)
            if self.dbpasswd:
                dbconn += ' password={0}'.format(self.dbpasswd)

            return dbconn

        dsn_output = conn_string()

        for item in self.filename:
            if item.split('.')[-1] != 'zip':
                continue
            dsn_input = self._unzip_file(item)
            self._import_gdal(dsn_input, dsn_output, overwrite, crs, format_output='PostgreSQL')

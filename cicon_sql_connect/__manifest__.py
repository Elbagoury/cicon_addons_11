
{
    'name': 'Import data from ODBC sources',
    'version': '11-1',
    'category': 'Tools',
    'description': """
Import data directly from other databases.
Installed in the Administration module, menu Configuration -> Import from ODBC.

Features:
* Connects to other databases using ODBC (pyodbc) or Oracle Client (cx_Oracle).
* Fetched data from the databases are used to build lines equivalent to regular import files. These are imported using the standard "import_data()" ORM method, benefiting from all its features, including xml_ids.
* Each table import is defined by an SQL statement, used to build the equivalent for an import file. Each column's name should correspond to the column names you would use in an import file. The first column must provide an unique identifier for the record, and will be used to build it's xml_id.
* SQL columns names "None" are ignored by the import. One use for this is to provide a row's unique id (SQL first column) that doesn't need to be imported to OpenERP.
* The last sync date is the last (successfull) execution. You can select only records changed since the last execution by adding a WHERE clause using "?".
* When errors are found, only the record with the error fails import. The other correct records are commited. However, the "last sync date" will only be automaticaly updated when no errors are found.
* The "Ignore relationship Errors" flag tells the import to be retried without each or all of the relationship fields (".../id" or "...:id" columns).
* The import execution can be scheduled to run automaticaly.

Example SQL:
SELECT PRODUCT_CODE as "ref", PRODUCT_NAME as "name", 'product_category_id_'+SUPPLIER_ID as "partner_id/id"
FROM T_PRODUCTS 
WHERE DATE_CHANGED >= ?

To use ODBC you need to install unixodbc and python-pyodbc packages.
To connect to SQLServer you need to install and configure a driver, such as FreeTDS (tdsodbc package), and create an ODBC data source.
To connect to Oracle you need to install and configure the Instant Client, and install the cx_Oracle python library. This library can be used to establish the connection without the nedd for ODBC.
    """,
    'author': 'Daniel Reis',
    'website': '',
    'depends': ['base'],
    'init_xml': [],
    'data': [
        'views/import_odbc_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'test': [], 
    'installable': True,
    'active': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

from dataflows import Flow, PackageWrapper, ResourceWrapper, validate
from dataflows import add_metadata, dump_to_path, load, set_type, printer


def rename_resources(package: PackageWrapper):
    package.pkg.descriptor['resources'][0]['name'] = 'quarterly'
    package.pkg.descriptor['resources'][0]['path'] = 'data/quarterly.csv'
    package.pkg.descriptor['resources'][1]['name'] = 'annual'
    package.pkg.descriptor['resources'][1]['path'] = 'data/annual.csv'
    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    second: ResourceWrapper = next(res_iter)
    yield first.it
    yield second.it
    yield from package


bond_uk = Flow(
    add_metadata(
        name="bond-yields-uk-10y",
        title= "10y UK Government Bond Yields (long-term interest rate)",
        sources=[
            {
              "name": "Bank of England",
              "path": "http://www.bankofengland.co.uk/boeapps/iadb/index.asp?Travel=NIxIRx&levels=1&XNotes=Y&C=DUS&G0Xtop.x=51&G0Xtop.y=7&XNotes2=Y&Nodes=X41514X41515X41516X41517X55047X76909X4051X4052X4128X33880X4053X4058&SectionRequired=I&HideNums=-1&ExtraInfo=true#BM",
              "title": "Bank of England"
            }
        ],
        licenses=[
            {
              "id": "odc-pddl",
              "path": "http://opendatacommons.org/licenses/pddl/",
              "name": "public_domain_dedication_and_license"
            }
        ],
        views=[
            {
              "name": "graph",
              "title": "Average yield from British Government Securities, 10 year Nominal Par Yield",
              "specType": "simple",
              "spec": {"type": "line","group": "Date","series": ["Rate"]}
            }
        ]
    ),
    load(
        load_source='http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUQAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963',
        skip_rows=[1],
        headers=['Date', 'Rate']
    ),
    set_type('Date', type='date', format='any'),
    set_type('Rate', type='number', description='Quarterly average yield from British Government Securities, 10 year Nominal Par Yield'),
    load(
        load_source='http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUAAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963',
        skip_rows=[1],
        headers=['Year', 'Rate']
    ),
    set_type('Year', type='date', format='any'),
    set_type('Rate', type='number', description='Annual average yield from British Government Securities, 10 year Nominal Par Yield'),
    rename_resources,
    validate(),
    printer(),
    dump_to_path(),
)


if __name__ == '__main__':
    bond_uk.process()

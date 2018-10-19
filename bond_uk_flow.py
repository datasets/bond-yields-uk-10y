import os

from dataflows import Flow, PackageWrapper, ResourceWrapper, validate
from dataflows import add_metadata, load, set_type, update_resource

def readme(fpath='README.md'):
    if os.path.exists(fpath):
        return open(fpath).read()

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
        ],
        readme=readme()
    ),
    load(
        load_source='http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUQAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963',
        skip_rows=[1],
        headers=['Date', 'Rate'],
        format='csv',
        name='quarterly'
    ),
    load(
        load_source='http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUAAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963',
        skip_rows=[1],
        headers=['Year', 'Rate'],
        format='csv',
        name='annual'
    ),
    set_type('Date', resources='quarterly', type='date', format='any'),
    set_type('Rate', resources='quarterly', type='number', description='Quarterly average yield from British Government Securities, 10 year Nominal Par Yield'),
    set_type('Year', resources='annual', type='date', format='any'),
    set_type('Rate', resources='annual', type='number', description='Annual average yield from British Government Securities, 10 year Nominal Par Yield'),
    update_resource('quarterly', **{'path':'data/quarterly.csv', 'dpp:streaming': True}),
    update_resource('annual', **{'path':'data/annual.csv', 'dpp:streaming': True}),
    validate()
)

def flow(parameters, datapackage, resources, stats):
    return bond_uk

if __name__ == '__main__':
    bond_uk.process()

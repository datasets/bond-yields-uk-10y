<a href="https://datahub.io/core/bond-yields-uk-10y"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

10 year nominal yields on UK government bonds from the bank of England. The 10
year government bond yield is considered a standard indicator of long-term
interest rates. This is a direct extract from the Bank of [England IUAAMNPY
series: "Annual average yield from British Government Securities, 10 year
Nominal Par Yield"][boe].

[boe]: http://www.bankofengland.co.uk/boeapps/iadb/index.asp?Travel=NIxIRx&levels=1&XNotes=Y&C=DUS&G0Xtop.x=51&G0Xtop.y=7&XNotes2=Y&Nodes=X41514X41515X41516X41517X55047X76909X4051X4052X4128X33880X4053X4058&SectionRequired=I&HideNums=-1&ExtraInfo=true#BM

## Data

Data from Bank of England (series IUAAMNPY "Annual average yield from British
Government Securities, 10 year Nominal Par Yield") with some minor processing
(see scripts).

Full information about the BoE Yields data may be found on the BoE website at [bankofengland official site](http://www.bankofengland.co.uk/statistics/Pages/iadb/notesiadb/Yields.aspx)

There are several relevant series:

* 10y par yields Annual average - IUAAMNPY - Annual
  * [www.bankofengland.co.uk](http://www.bankofengland.co.uk/boeapps/iadb/index.asp?Travel=NIxIRx&levels=1&XNotes=Y&G0Xtop.x=56&G0Xtop.y=10&C=DUS&XNotes2=Y&Nodes=X41514X41515X41516X41517X55047X76909X4051X4052X4128X33880X4053X4058&SectionRequired=I&HideNums=-1&ExtraInfo=true#BM)
  * 1984-present
  * [Direct download URLs look like](http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUMAMNPY&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/1963&Dateto=01/Jan/2015)
* There are also versions of this series at other granularities down to a day
  * Daily - IUDMNPY - Daily
  * Month average - IUMAMNPY - Monthly
  * End month - IUMMNPY - Monthly
  * Quarterly average - IUQAMNPY - Quarterly
  * End quarter - IUQMNPY - Quarterly
  * Annual average - IUAAMNPY - Annual
  * End year - IUAMNPY - Annual
* 10y par gross redemption yield Annual average - IUAAAJLW - Annual
  * 1984-2007 (not clear why this ends in 2007)

## Preparation

You will need Python 3.6 or greater and dataflows library to run the script

To update the data run the process script locally:

```
# Install dataflows
pip install dataflows

# Run the script
python bond_uk_flow.py
```

## License

The [Bank of England Terms of Use][tou] appear only to allow non-commercial
use:

> Statistical Interactive Database (IADB) Terms and Conditions
>
> The content of the database is for general information only, and is provided
> to users free of charge. Commercial use for financial gain is not permitted
> without the express permission of the Bank of England.  The Bank of England
> reserves the right to terminate or restrict user access if it determines that
> a user is acting in a manner contrary to the interests of other users of the
> database e.g. excessive usage. [retrieved 2013-04-07]

[tou]: http://www.bankofengland.co.uk/pages/disclaimer.aspx#Statistics

However, the amounts of data provided in this dataset is so minimal as likely to fall
below any threshold for Database Rights.

As such the maintainers feel warranted in putting the dataset out under the
Public Domain Dedication and License but that they can, obviously, only license
(or dedicate) material they control (or in which there are no rights).

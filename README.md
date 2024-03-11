# ImportSplineCSVg
Import Splines from CSV to Autodesk Fusion (globalized)

Unlike the standard Autodesk's sample script, this import respects alternative data delimiters in CSV files (Czech, German), can import multiple profiles in one go (delimited by an empty line in the CSV file), allows comma as a decimal separator, and allows to import X/Y-only CSV files.

It also creates the spline(s) in the active (not root) component and assumes millimeter units (keeps imported numbers 1:1, not 10x larger).

See more at www.cadforum.cz

# ImportSplineCSVg
Import Splines from CSV to Autodesk Fusion (globalized)

Unlike the standard Autodesk's sample script, this import respects alternative data delimiters in CSV files (Czech, German), can import multiple profiles in one go (delimited by an empty line in the CSV file), allows comma as a decimal separator, and allows to import X/Y-only CSV files.

It also creates the spline(s) in the active (not root) component and assumes millimeter units (keeps imported numbers 1:1, not 10x larger).

See more at www.cadforum.cz

![csv1](https://github.com/CADstudioCZ/ImportSplineCSVg/assets/46652150/2d350213-3abf-4cc1-bb17-d859eddff61f)

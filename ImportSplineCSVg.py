#Author-Autodesk Inc. + ARKANCE (2024)
#Description-Import spline from csv file, globalized, multiple, 2D

import adsk.core, adsk.fusion, traceback
import io

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        # Get all components in the active design.
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        root = design.activeComponent # or design.rootComponent
        title = 'Import Spline csv'
        if not design:
            ui.messageBox('No active Fusion design', title)
            return
        
        dlg = ui.createFileDialog()
        dlg.title = 'Open CSV File'
        dlg.filter = 'Comma Separated Values (*.csv);;All Files (*.*)'
        if dlg.showOpen() != adsk.core.DialogResults.DialogOK :
            return
        
        filename = dlg.filename
        with io.open(filename, 'r', encoding='utf-8-sig') as f:
            prf = 0
            prevline = ""
            points = adsk.core.ObjectCollection.create()
            line = f.readline()
            listdelim = "," #CS
            aux = line.split(';')
            if len(aux) > 1 :
                listdelim = ";"
            data = []
            linecnt = 0
            while line:
                cleanline = line.replace(listdelim,"").rstrip('\n').strip('\r') # CS
                if linecnt > 0 and cleanline == "" and prevline > "" :
                    if points.count:
                        sketch = root.sketches.add(root.xYConstructionPlane)
                        sketch.sketchCurves.sketchFittedSplines.add(points)
                    else:
                        ui.messageBox('No valid points', title)            
                    prf = prf+1
                    points.clear()
                prevline = cleanline
                pntStrArr = line.split(listdelim)
                for pntStr in pntStrArr:
                    try:
                        if pntStr.find(",") >= 0 :
                            pntStr = pntStr.replace(",",".")
                        data.append(float(pntStr))
                    except:
                        break
                if len(pntStrArr) == 2 :
                    data.append(0)
                if len(data) >= 3 :
                    point = adsk.core.Point3D.create(data[0], data[1], data[2])
                    points.add(point)
                line = f.readline()
                linecnt = linecnt+1
                data.clear()            
        if points.count:
            sketch = root.sketches.add(root.xYConstructionPlane)
            sketch.sketchCurves.sketchFittedSplines.add(points)
        else:
            ui.messageBox('No valid points', title)            
            
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

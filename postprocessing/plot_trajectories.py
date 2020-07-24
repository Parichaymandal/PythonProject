from qgis.utils import iface
from qgis.core import *
import os
from qgis.gui import *
from preprocessing.import_shapefile import *
from PyQt5.QtGui import *

def plot_trajectories(layer, output_path):
    '''
        Plot trajectories, add legends, and exports to image
        
        Parameters:
        ____________
            layer: qgis vector layer
                vector layers of lines.shp
            output_path: string
                where the output image will be saved
    '''
    
    ##################################
    ## Plot trajectories
    ##################################
    
    # set world map path
    world_path = os.path.join(QgsApplication.pkgDataPath(), "resources", "data", "world_map.gpkg")
    countries_layer_path = world_path + "|layername=countries"
    
    # load world map
    map_layer = QgsVectorLayer(countries_layer_path, "Countries layer", "ogr")
    if not map_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(map_layer)

    # define static rules: label, condition, color, scale
    rules = (
        ('Goose 72364', '"name" LIKE \'72364-72364\'', 'magenta', None),
        ('Goose 73054', '"name" LIKE \'73054-73054\'', 'blue', None),
        ('Goose 72417', '"name" LIKE \'72417-72417\'', 'gray', None),
        ('Goose 72413', '"name" LIKE \'72413-72413\'', 'green', None),
        ('Goose 79694', '"name" LIKE \'79694-79694\'', 'yellow', None),
        ('Goose 73053', '"name" LIKE \'73053-73053\'', 'orange', None),
        ('Goose 79698', '"name" LIKE \'79698-79698\'', 'red', None),
    )
    
    # create a new rule-based renderer
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    renderer = QgsRuleBasedRenderer(symbol)
    
    # get the root rule
    root_rule = renderer.rootRule()
    
    # Apply all rules
    for label, condition, color, scale in rules:
        # clone the default root
        rule = root_rule.children()[0].clone()
        # set label
        rule.setLabel(label)
        # set condition
        rule.setFilterExpression(condition)
        # set color
        rule.symbol().setColor(QColor(color))
        # set width
        rule.symbol().setWidth(.5)
        # set the scale limits if specified
        if scale is not None:
            rule.setScaleMinDenom(scale[0])
            rule.setScaleMaxDenom(scale[1])
            
        # append the rule to the list of rules
        root_rule.appendChild(rule)

    # delete the default rule
    root_rule.removeChildAt(0)
    # apply the renderer to the layer
    layer.setRenderer(renderer)
    
    ####################################
    ## Create layouts,legends to export
    ####################################
    
    # get project instance
    project = QgsProject.instance()
    # get project manager
    manager = project.layoutManager()
    
    # set layout name
    layoutName = 'Export Layer'
    layouts_list = manager.printLayouts()
    
    # remove duplicates 
    for layout in layouts_list:
        if layout.name() == layoutName:
            manager.removeLayout(layout)
    
    # remove layers those are not to be mapped    
    layers_to_map = [map_layer, layer]
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr not in layers_to_map:
            QgsProject.instance().removeMapLayers([lyr.id()])
            
    # set print layout        
    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName(layoutName)
    manager.addLayout(layout)
    # create map item in the layout
    map = QgsLayoutItemMap(layout)
    map.setRect(20, 20, 20, 20)
 
    # set the map extent
    ms = QgsMapSettings()
    ms.setLayers([layer]) # set layers to be mapped
    rect = QgsRectangle(ms.fullExtent())
    rect.scale(1.0)
    ms.setExtent(rect)
    map.setExtent(rect)
    map.setBackgroundColor(QColor(255, 255, 255, 0))
    
    # add to layout
    layout.addLayoutItem(map)
 
    map.attemptMove(QgsLayoutPoint(5, 20, QgsUnitTypes.LayoutMillimeters))
    map.attemptResize(QgsLayoutSize(250, 180, QgsUnitTypes.LayoutMillimeters))
    
    # add legend to the layout
    legend = QgsLayoutItemLegend(layout)
    # set layout title
    legend.setTitle("Legend")
    layerTree = QgsLayerTree()
    layerTree.addLayer(layer)
    legend.model().setRootGroup(layerTree)
    layout.addLayoutItem(legend)
    legend.attemptMove(QgsLayoutPoint(260, 15, QgsUnitTypes.LayoutMillimeters))
    
    # get layout from project manager
    layout = manager.layoutByName(layoutName)
    # Initiate exporter
    exporter = QgsLayoutExporter(layout)
    # export as image
    exporter.exportToImage(output_path, QgsLayoutExporter.ImageExportSettings())

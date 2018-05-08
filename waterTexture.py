import bpy

def empty_materials():
    for mat in mats.keys():
        mats.remove(mats[mat])

def create_cycles_material(settings):
    
    scn = bpy.context.scene
    if not scn.render.engine == 'CYCLES':
        scn.render.engine = 'CYCLES'

    mat = bpy.data.materials.new('zheight')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes

    '''Make or move nodes'''
    node = nodes['Noise Texture']
    node.location = 600, 120
    
    node = nodes['Noise Texture']
    node.location = 800, 120
    
    node = nodes('VoronoiTexture')
    node.name = 'Voronoi_Texture'
    node.location = 1200, 120
    
    node = nodes.new('Mix')
    node.operation = 'Mix'
    node.label = 'Color1'
    node.label = 'Color2'
    node.name = 'Mix'    
    node.location = 700, 160
    
    node = nodes.new('Invert')
    node.operation = 'Invert'
    node.label = 'Color'    
    node.name = 'Invert'        
    node.location = 100, 120

    node = nodes.new('Add')
    node.operation = 'ADD'
    node.label = 'Color1'  
    node.label = 'Color2'   
    node.name = 'ADD'        
    node.location = 100, 120


    node = nodes.new('Glass BSDF')
    node.operation = 'BSDF'
    node.label = 'BSDF'     
    node.name = 'BSDF'        
    node.location = 100, 120

    node = nodes.new('Diffuse BSDF')
    node.operation = 'BSDF'
    node.label = 'BSDF'     
    node.name = 'BSDF'        
    node.location = 100, 120

    node = nodes.new('Mix Shader')
    node.operation = 'Mix Shader'
    node.label = 'Shader'
    node.label = 'Shader'
    node.name = 'Mix Shader'    
    node.location = 700, 160
    
    node = nodes.new('Material Output')
    node.location = 300, 120
    
    '''Connect nodes
    Geometry|Position > ADD_0|0
    #ADD_0|Vector > DOT_0|0 
    #DOT_0|Value > ColorRamp|Fac
    #ColorRamp|Color_Out > DiffuseBSDF|Color_In
    '''
    
    ''' Noise Texture > Mix '''
    output = nodes['Noise Texture'].outputs['Color']
    input = nodes['Mix_0'].inputs['Color1']
    mat.node_tree.links.new(output, input)

    ''' Noise Texture > Mix '''
    output = nodes['Noise Texture'].outputs['Color']
    input = nodes['Mix_0'].inputs[Color2]
    mat.node_tree.links.new(output, input)

    ''' Voronoi Texture > Invert '''
    output = nodes['Voronoi Texture'].outputs['Color']
    input = nodes['Invert'].inputs['Color']
    mat.node_tree.links.new(output, input)

    ''' Mix > Add'''
    output = nodes['Mix'].outputs['Color']
    input = nodes['Add'].inputs['Color1']
    mat.node_tree.links.new(output, input)

    ''' Invert > Add'''
    output = nodes['Invert'].outputs['Color']
    input = nodes['Add'].inputs['Color2']
    mat.node_tree.links.new(output, input)
    
    ''' Glass BSDF > Mix Shader'''
    output = nodes['Diffuse BSDF'].outputs['BDSF']
    input = nodes['Mix Shader'].inputs['Shader']    
    mat.node_tree.links.new(output, input)

    ''' Diffuse BSDF > Mix Shader'''
    output = nodes['Diffuse BSDF'].outputs['BDSF']
    input = nodes['Mix Shader'].inputs['Shader']    
    mat.node_tree.links.new(output, input)

    ''' Add > Material Output'''
    output = nodes['Add'].outputs['Color']
    input = nodes['Material Output'].inputs['Displacement']    
    mat.node_tree.links.new(output, input)

    ''' Mix Shader > Material Output'''
    output = nodes['Mix Shader'].outputs['Shader']
    input = nodes['Material Output'].inputs['Surface']    
    mat.node_tree.links.new(output, input)
    
    
create_cycles_material()
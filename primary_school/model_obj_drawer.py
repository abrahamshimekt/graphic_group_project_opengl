import pygame
from pygame.locals import *
from OpenGL.GL.shaders import *
import os
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from model_texture_loader import load_texture
from model_obj_loader import ObjLoader
import time


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()


def init():
    global VAO, textures, model_loc, \
        fence_indices, field_indices, trunk1_indices, branch1_indices, \
        house_position, fence_position, field_position, \
        trunk1_position, branch1_position, trunk2_indices, branch2_indices, branch2_position, trunk2_position, \
        trunk3_indices, branch3_indices, branch3_position, trunk3_position, trunk4_indices, branch4_indices, branch4_position, trunk4_position, \
        trunk5_indices, branch5_indices, branch5_position, trunk5_position, trunk6_indices, branch6_indices, branch6_position, trunk6_position, \
        trunk7_indices, branch7_indices, branch7_position, trunk7_position, trunk8_indices, branch8_indices, branch8_position, trunk8_position, \
        trunk9_indices, trunk9_position, branch9_indices, branch9_position, trunk10_indices, trunk10_position, branch10_indices, branch10_position, \
        poll_indices, poll_position, green_indices, green_position, yellow_indices, yellow_position, red_indices, red_position, \
        grass_indices, grass_position, left_indices, left_position, right_indices, right_position, front1_indices, front1_position, \
        front2_indices, front2_position, poll_field_indices, poll_field_position, road_center_indices, road_center_position, zebra_indices, \
        zebra_position, flowers_indices, back_road_center_indices_indices, back_road_center_position, room1_indices, room1_position, room2_indices, room2_position, room3_indices, \
        room3_position, room4_indices, room4_position, room5_indices, room5_position, room6_indices, room6_position, room7_indices, \
        room7_position, roof11_indices, roof11_position, roof12_indices, roof12_position, roof21_indices, roof21_position, roof22_indices, \
        roof22_position, roof31_indices, roof31_position, roof32_indices, roof32_position, roof41_indices, roof41_position, roof42_indices, \
        roof42_position, roof51_indices, roof51_position, roof52_indices, roof52_position, roof61_indices, roof61_position, roof62_indices, \
        roof62_position, roof71_indices, roof71_position, roof72_indices, roof72_position, door1_indices, door1_position, door2_indices, \
        door2_position, door3_indices, door3_position, door4_indices, door4_position, door5_indices, door5_position, door6_indices, \
        door6_position, door7_indices, door7_position, window1_indices, window1_position, window2_indices, window2_position, window3_indices, \
        window3_position, window4_indices, window4_position, window5_indices, window5_position, window6_indices, window6_position, window7_indices, window7_position
    pygame.init()
    display = (1020, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    vertexShaderContent = getFileContents("school.vertex.shader")
    fragmentShaderContent = getFileContents("school.fragment.shader")

    shader = compileProgram(compileShader(vertexShaderContent, GL_VERTEX_SHADER),
                            compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER))
    fence_indices, fence_buffer = ObjLoader.load_model("fence_objs/fences.obj")
    field_indices, field_buffer = ObjLoader.load_model("field_objs/field.obj")

    room1_indices, room1_buffer = ObjLoader.load_model("house_objs/room1.obj")
    room2_indices, room2_buffer = ObjLoader.load_model("house_objs/room2.obj")
    room3_indices, room3_buffer = ObjLoader.load_model("house_objs/room3.obj")
    room4_indices, room4_buffer = ObjLoader.load_model("house_objs/room4.obj")
    room5_indices, room5_buffer = ObjLoader.load_model("house_objs/room5.obj")
    room6_indices, room6_buffer = ObjLoader.load_model("house_objs/room6.obj")
    room7_indices, room7_buffer = ObjLoader.load_model("house_objs/room7.obj")

    door1_indices, door1_buffer = ObjLoader.load_model("house_objs/door1.obj")
    door2_indices, door2_buffer = ObjLoader.load_model("house_objs/door2.obj")
    door3_indices, door3_buffer = ObjLoader.load_model("house_objs/door3.obj")
    door4_indices, door4_buffer = ObjLoader.load_model("house_objs/door4.obj")
    door5_indices, door5_buffer = ObjLoader.load_model("house_objs/door5.obj")
    door6_indices, door6_buffer = ObjLoader.load_model("house_objs/door6.obj")
    door7_indices, door7_buffer = ObjLoader.load_model("house_objs/door7.obj")

    window1_indices, window1_buffer = ObjLoader.load_model("house_objs/window1.obj")
    window2_indices, window2_buffer = ObjLoader.load_model("house_objs/window2.obj")
    window3_indices, window3_buffer = ObjLoader.load_model("house_objs/window3.obj")
    window4_indices, window4_buffer = ObjLoader.load_model("house_objs/window4.obj")
    window5_indices, window5_buffer = ObjLoader.load_model("house_objs/window5.obj")
    window6_indices, window6_buffer = ObjLoader.load_model("house_objs/window6.obj")
    window7_indices, window7_buffer = ObjLoader.load_model("house_objs/window7.obj")

    roof11_indices, roof11_buffer = ObjLoader.load_model("house_objs/roof11.obj")
    roof12_indices, roof12_buffer = ObjLoader.load_model("house_objs/roof12.obj")

    roof21_indices, roof21_buffer = ObjLoader.load_model("house_objs/roof21.obj")
    roof22_indices, roof22_buffer = ObjLoader.load_model("house_objs/roof22.obj")

    roof31_indices, roof31_buffer = ObjLoader.load_model("house_objs/roof31.obj")
    roof32_indices, roof32_buffer = ObjLoader.load_model("house_objs/roof32.obj")

    roof41_indices, roof41_buffer = ObjLoader.load_model("house_objs/roof41.obj")
    roof42_indices, roof42_buffer = ObjLoader.load_model("house_objs/roof42.obj")

    roof51_indices, roof51_buffer = ObjLoader.load_model("house_objs/roof51.obj")
    roof52_indices, roof52_buffer = ObjLoader.load_model("house_objs/roof52.obj")

    roof61_indices, roof61_buffer = ObjLoader.load_model("house_objs/roof61.obj")
    roof62_indices, roof62_buffer = ObjLoader.load_model("house_objs/roof62.obj")

    roof71_indices, roof71_buffer = ObjLoader.load_model("house_objs/roof71.obj")
    roof72_indices, roof72_buffer = ObjLoader.load_model("house_objs/roof72.obj")

    trunk1_indices, trunk1_buffer = ObjLoader.load_model("tree_objs/trunck1.obj")
    branch1_indices, branch1_buffer = ObjLoader.load_model("tree_objs/branch1.obj")

    trunk2_indices, trunk2_buffer = ObjLoader.load_model("tree_objs/trunck2.obj")
    branch2_indices, branch2_buffer = ObjLoader.load_model("tree_objs/branch2.obj")

    trunk3_indices, trunk3_buffer = ObjLoader.load_model("tree_objs/trunck3.obj")
    branch3_indices, branch3_buffer = ObjLoader.load_model("tree_objs/branch3.obj")

    trunk4_indices, trunk4_buffer = ObjLoader.load_model("tree_objs/trunk4.obj")
    branch4_indices, branch4_buffer = ObjLoader.load_model("tree_objs/branch4.obj")

    trunk5_indices, trunk5_buffer = ObjLoader.load_model("tree_objs/trunck5.obj")
    branch5_indices, branch5_buffer = ObjLoader.load_model("tree_objs/branch5.obj")

    trunk6_indices, trunk6_buffer = ObjLoader.load_model("tree_objs/trunch6.obj")
    branch6_indices, branch6_buffer = ObjLoader.load_model("tree_objs/branch6.obj")

    trunk7_indices, trunk7_buffer = ObjLoader.load_model("tree_objs/trunk7.obj")
    branch7_indices, branch7_buffer = ObjLoader.load_model("tree_objs/branch7.obj")

    trunk8_indices, trunk8_buffer = ObjLoader.load_model("tree_objs/trunk8.obj")
    branch8_indices, branch8_buffer = ObjLoader.load_model("tree_objs/branch8.obj")

    trunk9_indices, trunk9_buffer = ObjLoader.load_model("tree_objs/trunk9.obj")
    branch9_indices, branch9_buffer = ObjLoader.load_model("tree_objs/branch9.obj")

    trunk10_indices, trunk10_buffer = ObjLoader.load_model("tree_objs/trunk10.obj")
    branch10_indices, branch10_buffer = ObjLoader.load_model("tree_objs/branch10.obj")

    poll_indices, poll_buffer = ObjLoader.load_model("flag_objs/poll.obj")
    green_indices, green_buffer = ObjLoader.load_model("flag_objs/green.obj")
    yellow_indices, yellow_buffer = ObjLoader.load_model("flag_objs/yellow.obj")
    red_indices, red_buffer = ObjLoader.load_model("flag_objs/red.obj")
    grass_indices, grass_buffer = ObjLoader.load_model("field_objs/back_field.obj")

    left_indices, left_buffer = ObjLoader.load_model("field_objs/left.obj")
    right_indices, right_buffer = ObjLoader.load_model("field_objs/right.obj")
    front1_indices, front1_buffer = ObjLoader.load_model("field_objs/front1.obj")
    front2_indices, front2_buffer = ObjLoader.load_model("field_objs/front2.obj")
    poll_field_indices, poll_field_buffer = ObjLoader.load_model("field_objs/poll_field.obj")

    road_center_indices, road_center_buffer = ObjLoader.load_model("road_objs/road_center.obj")
    zebra_indices, zebra_buffer = ObjLoader.load_model("road_objs/zebra.obj")
    back_road_center_indices_indices, back_road_center_buffer = ObjLoader.load_model("road_objs/road_center_back.obj")

    objects_buffers = [fence_buffer, field_buffer,
                       room1_buffer, room2_buffer,
                       room3_buffer, room4_buffer,
                       room5_buffer, room6_buffer,
                       room7_buffer, door1_buffer,
                       door2_buffer, door3_buffer,
                       door4_buffer, door5_buffer,
                       door6_buffer, door7_buffer,
                       window1_buffer, window2_buffer,
                       window3_buffer, window4_buffer,
                       window5_buffer, window6_buffer,
                       window7_buffer,
                       roof11_buffer, roof12_buffer,
                       roof21_buffer, roof22_buffer,
                       roof31_buffer, roof32_buffer,
                       roof41_buffer, roof42_buffer,
                       roof51_buffer, roof52_buffer,
                       roof61_buffer, roof62_buffer,
                       roof71_buffer, roof72_buffer,

                       trunk1_buffer, trunk2_buffer,
                       trunk3_buffer, trunk4_buffer,
                       trunk5_buffer, trunk6_buffer,
                       trunk7_buffer, trunk8_buffer,
                       trunk9_buffer, trunk10_buffer,
                       branch1_buffer,branch2_buffer,
                       branch3_buffer,branch4_buffer,
                       branch5_buffer, branch6_buffer,
                       branch7_buffer,branch8_buffer,
                       branch9_buffer,branch10_buffer,
                       poll_buffer, green_buffer, yellow_buffer,
                       red_buffer, grass_buffer, left_buffer,
                       right_buffer, front1_buffer, front2_buffer,
                       poll_field_buffer, road_center_buffer, zebra_buffer,
                       back_road_center_buffer]

    VAO = glGenVertexArrays(70)
    VBO = glGenBuffers(70)
    for i in range(70):
        glBindVertexArray(VAO[i])
        glBindBuffer(GL_ARRAY_BUFFER, VBO[i])
        glBufferData(GL_ARRAY_BUFFER, objects_buffers[i].nbytes, objects_buffers[i], GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, objects_buffers[i].itemsize * 8, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, objects_buffers[i].itemsize * 8, ctypes.c_void_p(12))
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, objects_buffers[i].itemsize * 8, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

    textures = glGenTextures(70)
    object_textures = ["fence_textures/fences.png", "field_textures/field.png",
                       "house_textures/wall.jpg", "house_textures/wall.jpg",
                       "house_textures/wall.jpg", "house_textures/wall.jpg",
                       "house_textures/wall.jpg", "house_textures/wall.jpg",
                       "house_textures/wall.jpg",

                       "house_textures/door.jpg",
                       "house_textures/door.jpg",
                       "house_textures/door.jpg",
                       "house_textures/door.jpg",
                       "house_textures/door.jpg",
                       "house_textures/door.jpg",
                       "house_textures/door.jpg",

                       "house_textures/window.jpg",
                       "house_textures/window.jpg",
                       "house_textures/window.jpg",
                       "house_textures/window.jpg",
                       "house_textures/window.jpg",
                       "house_textures/window.jpg",
                       "house_textures/window.jpg",

                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",
                       "house_textures/roof.jpg", "house_textures/roof.jpg",

                       "tree_textures/trunk.jpg", "tree_textures/trunk.jpg",
                       "tree_textures/trunk.jpg", "tree_textures/trunk.jpg",
                       "tree_textures/trunk.jpg", "tree_textures/trunk.jpg",
                       "tree_textures/trunk.jpg", "tree_textures/trunk.jpg",
                       "tree_textures/trunk.jpg", "tree_textures/trunk.jpg",

                       "tree_textures/branch.png","tree_textures/branch.png",
                       "tree_textures/branch.png","tree_textures/branch.png",
                       "tree_textures/branch.png","tree_textures/branch.png",
                       "tree_textures/branch.png","tree_textures/branch.png",
                       "tree_textures/branch.png","tree_textures/branch.png",

                       "flag_textures/poll.png", "flag_textures/green.png",
                       "flag_textures/yellow.png", "flag_textures/red.png",
                       "field_textures/grass.jpg", "field_textures/grass.jpg",
                       "field_textures/grass.jpg", "field_textures/grass.jpg",
                       "field_textures/grass.jpg", "field_textures/grass.jpg",
                       "flag_textures/yellow.png", "road_textures/zebra.png", "flag_textures/yellow.png"]
    for i in range(70):
        load_texture(object_textures[i], textures[i])

    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
    room1_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    room2_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    room3_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    room4_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    room5_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    room6_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    room7_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    door1_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    door2_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    door3_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    door4_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    door5_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    door6_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    door7_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    window1_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    window2_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    window3_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    window4_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    window5_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    window6_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    window7_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    roof11_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof12_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof21_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof22_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    roof31_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof32_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof41_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof42_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    roof51_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof52_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof61_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof62_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof71_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    roof72_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    fence_position, field_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk1_position, branch1_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk2_position, branch2_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk3_position, branch3_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk4_position, branch4_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk5_position, branch5_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk6_position, branch6_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk7_position, branch7_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk8_position, branch8_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk9_position, branch9_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    trunk10_position, branch10_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    poll_position, green_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    yellow_position, red_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25])), pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    grass_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    left_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    right_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    front1_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    front2_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    poll_field_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))

    road_center_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    zebra_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))
    back_road_center_position = pyrr.matrix44.create_from_translation(
        pyrr.Vector3([0, -5, -25]))

    view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))
    model_loc = glGetUniformLocation(shader, "model")
    proj_loc = glGetUniformLocation(shader, "projection")
    view_loc = glGetUniformLocation(shader, "view")

    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)


def draw(x_position=0,y_position =0,z_position=0):
    global VAO, textures, model_loc, \
        fence_indices, field_indices, trunk1_indices, branch1_indices, \
        house_position, fence_position, field_position, \
        trunk1_position, branch1_position, trunk2_indices, branch2_indices, branch2_position, trunk2_position, \
        trunk3_indices, branch3_indices, branch3_position, trunk3_position, trunk4_indices, branch4_indices, branch4_position, trunk4_position, \
        trunk5_indices, branch5_indices, branch5_position, trunk5_position, trunk6_indices, branch6_indices, branch6_position, trunk6_position, \
        trunk7_indices, branch7_indices, branch7_position, trunk7_position, trunk8_indices, branch8_indices, branch8_position, trunk8_position, \
        trunk9_indices, trunk9_position, branch9_indices, branch9_position, trunk10_indices, trunk10_position, branch10_indices, branch10_position, \
        poll_indices, poll_position, green_indices, green_position, yellow_indices, yellow_position, red_indices, red_position, \
        grass_indices, grass_position, left_indices, left_position, right_indices, right_position, front1_indices, front1_position, \
        front2_indices, front2_position, poll_field_indices, poll_field_position, road_center_indices, road_center_position, zebra_indices, \
        zebra_position, flowers_indices, back_road_center_indices_indices, back_road_center_position, room1_indices, room1_position, room2_indices, room2_position, room3_indices, \
        room3_position, room4_indices, room4_position, room5_indices, room5_position, room6_indices, room6_position, room7_indices, \
        room7_position, roof11_indices, roof11_position, roof12_indices, roof12_position, roof21_indices, roof21_position, roof22_indices, \
        roof22_position, roof31_indices, roof31_position, roof32_indices, roof32_position, roof41_indices, roof41_position, roof42_indices, \
        roof42_position, roof51_indices, roof51_position, roof52_indices, roof52_position, roof61_indices, roof61_position, roof62_indices, \
        roof62_position, roof71_indices, roof71_position, roof72_indices, roof72_position, door1_indices, door1_position, door2_indices, \
        door2_position, door3_indices, door3_position, door4_indices, door4_position, door5_indices, door5_position, door6_indices, \
        door6_position, door7_indices, door7_position, window1_indices, window1_position, window2_indices, window2_position, window3_indices, \
        window3_position, window4_indices, window4_position, window5_indices, window5_position, window6_indices, window6_position, window7_indices, window7_position

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    objects = [(fence_indices, fence_position),
               (field_indices, field_position),
               (room1_indices, room1_position),
               (room2_indices, room2_position),
               (room3_indices, room3_position),
               (room4_indices, room4_position),
               (room5_indices, room5_position),
               (room6_indices, room6_position),
               (room7_indices, room7_position),

               (door1_indices, door1_position),
               (door2_indices, door2_position),
               (door3_indices, door3_position),
               (door4_indices, door4_position),
               (door5_indices, door5_position),
               (door6_indices, door6_position),
               (door7_indices, door7_position),

               (window1_indices, window1_position),
               (window2_indices, window2_position),
               (window3_indices, window3_position),
               (window4_indices, window4_position),
               (window5_indices, window5_position),
               (window6_indices, window6_position),
               (window7_indices, window7_position),

               (roof11_indices, roof11_position),
               (roof12_indices, roof12_position),

               (roof21_indices, roof21_position),
               (roof22_indices, roof22_position),
               (roof31_indices, roof31_position),
               (roof32_indices, roof32_position),
               (roof41_indices, roof41_position),
               (roof42_indices, roof42_position),
               (roof51_indices, roof51_position),
               (roof52_indices, roof52_position),
               (roof61_indices, roof61_position),
               (roof62_indices, roof62_position),
               (roof71_indices, roof71_position),
               (roof72_indices, roof72_position),

               (trunk1_indices, trunk1_position),
               (trunk2_indices, trunk2_position),
               (trunk3_indices, trunk3_position),
               (trunk4_indices, trunk4_position),
               (trunk5_indices, trunk5_position),
               (trunk6_indices, trunk6_position),
               (trunk7_indices, trunk7_position),
               (trunk8_indices, trunk8_position),
               (trunk9_indices, trunk9_position),
               (trunk10_indices, trunk10_position),

               (branch1_indices, branch1_position),
               (branch2_indices, branch2_position),
               (branch3_indices, branch3_position),
               (branch4_indices, branch4_position),
               (branch5_indices, branch5_position),
               (branch6_indices, branch1_position),
               (branch7_indices, branch7_position),
               (branch8_indices, branch8_position),
               (branch9_indices, branch9_position),
               (branch10_indices, branch10_position),

               (poll_indices, poll_position),
               (green_indices, green_position),
               (yellow_indices, yellow_position),
               (red_indices, red_position),
               (grass_indices, grass_position),
               (left_indices, left_position),
               (right_indices, right_position),
               (front1_indices, front1_position),
               (front2_indices, front2_position),
               (poll_field_indices, poll_field_position),

               (road_center_indices, road_center_position),
               (zebra_indices, zebra_position),
               (back_road_center_indices_indices, back_road_center_position),

               ]
    object_positions = [fence_position, field_position,
                        room1_position,
                        room2_position, room3_position,
                        room4_position, room5_position,
                        room6_position, room7_position,
                        door1_position, door2_position,
                        door3_position, door4_position,
                        door5_position, door6_position,
                        door7_position, window1_position,
                        window2_position, window3_position,
                        window4_position, window5_position,
                        window6_position, window7_position,
                        roof11_position, roof12_position,
                        roof21_position, roof22_position,
                        roof31_position, roof32_position,
                        roof41_position, roof42_position,
                        roof51_position, roof52_position,
                        roof61_position, roof62_position,
                        roof71_position, roof72_position,
                        trunk1_position,
                        trunk2_position,trunk3_position,
                        trunk4_position,trunk5_position,
                        trunk6_position,trunk7_position,
                        trunk8_position,trunk9_position,
                        trunk10_position,branch1_position,
                        branch2_position,branch3_position,
                        branch4_position,branch5_position,
                        branch1_position,branch7_position,
                        branch8_position,branch9_position,
                        branch10_position,poll_position,
                        green_position,yellow_position,
                        red_position,grass_position,
                        left_position,right_position,
                        front1_position,front2_position,
                        poll_field_position,road_center_position,
                        zebra_position, back_road_center_position]
    for i in range(70) :
        object_positions[i] = pyrr.matrix44.create_from_translation(pyrr.Vector3([0+x_position, -5+y_position, -25+z_position]))
    for i in range(70):
        rot_y = pyrr.Matrix44.from_y_rotation(0.01*time.time())
        model = pyrr.matrix44.multiply(rot_y, object_positions[i])
        glBindVertexArray(VAO[i])
        glBindTexture(GL_TEXTURE_2D, textures[i])
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawArrays(GL_TRIANGLES, 0, len(objects[i][0]))


def main():
    init()
    z_position =0
    x_position = 0
    y_position = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            x_position -= 0.1
        elif keys_pressed[pygame.K_RIGHT]:
            x_position += 0.1
        elif keys_pressed[pygame.K_TAB]:
            y_position -= 0.1
        elif keys_pressed[pygame.K_CAPSLOCK]:
            y_position +=0.1
        elif keys_pressed[pygame.K_DOWN]:
            z_position -=  0.1
        elif keys_pressed[pygame.K_UP]:
            z_position += 0.1
        draw(x_position,y_position,z_position)
        pygame.display.flip()
        pygame.time.wait(10)


main()

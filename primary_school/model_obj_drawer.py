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
    global VAO, textures, model_loc, house_indices, fence_indices, house_position, fence_position
    pygame.init()
    display = (1020, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # glViewport(100,100,950,600)

    vertexShaderContent = getFileContents("school.vertex.shader")
    fragmentShaderContent = getFileContents("school.fragment.shader")

    shader = compileProgram(compileShader(vertexShaderContent, GL_VERTEX_SHADER),
                            compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER))

    house_indices, house_buffer = ObjLoader.load_model("houses.obj")
    fence_indices, fence_buffer = ObjLoader.load_model("fences.obj")

    # VAO and VBO
    VAO = glGenVertexArrays(2)
    VBO = glGenBuffers(2)
    # EBO = glGenBuffers(1)

    # houses VAO
    glBindVertexArray(VAO[0])
    # houses Vertex Buffer Object
    glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
    glBufferData(GL_ARRAY_BUFFER, house_buffer.nbytes, house_buffer, GL_STATIC_DRAW)

    # houses vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, house_buffer.itemsize * 8, ctypes.c_void_p(0))
    # houses textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, house_buffer.itemsize * 8, ctypes.c_void_p(12))
    # houses normals
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, house_buffer.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    # fence VAO
    glBindVertexArray(VAO[1])
    # fence Vertex Buffer Object
    glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
    glBufferData(GL_ARRAY_BUFFER, fence_buffer.nbytes, fence_buffer, GL_STATIC_DRAW)

    # fence vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, fence_buffer.itemsize * 8, ctypes.c_void_p(0))
    # fence textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, fence_buffer.itemsize * 8, ctypes.c_void_p(12))
    # fence normals
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, fence_buffer.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    textures = glGenTextures(2)
    load_texture("houses.png", textures[0])
    load_texture("fences.png", textures[1])

    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
    house_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))
    fence_position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))

    view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

    model_loc = glGetUniformLocation(shader, "model")
    proj_loc = glGetUniformLocation(shader, "projection")
    view_loc = glGetUniformLocation(shader, "view")

    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)


def draw():
    global VAO, textures, model_loc, house_indices, fence_indices, house_position, fence_position
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * time.time())
    model = pyrr.matrix44.multiply(rot_y, house_position)

    # draw the house
    glBindVertexArray(VAO[0])
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(house_indices))

    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * time.time())
    model = pyrr.matrix44.multiply(rot_y, fence_position)

    # draw the fence
    glBindVertexArray(VAO[1])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(fence_indices))


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()

import pygame
from pygame.locals import *
from OpenGL.GL.shaders import *
import os
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from model_texture_loader import Texture_loader
from model_obj_loader import ObjLoader
import time


class ObjectDrawer:
    def __int__(self):
        self.VAO = None
        self.VBO = None
        self.textures = None
        self.model_loc = None
        self.indices_buffers = None

    def getFileContents(self, filename):
        p = os.path.join(os.getcwd(), "shaders", filename)
        return open(p, 'r').read()

    def shader(self):
        vertexShaderContent = self.getFileContents("school.vertex.shader")
        fragmentShaderContent = self.getFileContents("school.fragment.shader")
        shader = compileProgram(compileShader(vertexShaderContent, GL_VERTEX_SHADER),
                                compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER))
        return shader

    def load_obj_file(self):
        obj_loader = ObjLoader()
        self.indices_buffers = []
        obj_files = ["fence_objs/fences.obj", "field_objs/field.obj", "house_objs/room1.obj",
                     "house_objs/room2.obj", "house_objs/room3.obj", "house_objs/room4.obj",
                     "house_objs/room5.obj", "house_objs/room6.obj", "house_objs/room7.obj",
                     "house_objs/door1.obj", "house_objs/door2.obj", "house_objs/door3.obj",
                     "house_objs/door4.obj", "house_objs/door5.obj", "house_objs/door6.obj",
                     "house_objs/door7.obj", "house_objs/window1.obj", "house_objs/window2.obj",
                     "house_objs/window3.obj", "house_objs/window4.obj", "house_objs/window5.obj",
                     "house_objs/window6.obj", "house_objs/window7.obj", "house_objs/roof11.obj",
                     "house_objs/roof12.obj", "house_objs/roof21.obj", "house_objs/roof22.obj",
                     "house_objs/roof31.obj", "house_objs/roof32.obj",
                     "house_objs/roof41.obj", "house_objs/roof42.obj", "house_objs/roof51.obj",
                     "house_objs/roof52.obj", "house_objs/roof61.obj", "house_objs/roof62.obj",
                     "house_objs/roof71.obj", "house_objs/roof72.obj", "tree_objs/trunck1.obj",
                     "tree_objs/trunck2.obj", "tree_objs/trunck3.obj", "tree_objs/trunk4.obj",
                     "tree_objs/trunck5.obj", "tree_objs/trunch6.obj", "tree_objs/trunk7.obj",
                     "tree_objs/trunk8.obj", "tree_objs/trunk9.obj", "tree_objs/trunk10.obj",
                     "tree_objs/branch1.obj", "tree_objs/branch2.obj",
                     "tree_objs/branch3.obj", "tree_objs/branch4.obj", "tree_objs/branch5.obj",
                     "tree_objs/branch6.obj", "tree_objs/branch7.obj", "tree_objs/branch8.obj",
                     "tree_objs/branch9.obj", "tree_objs/branch10.obj",
                     "flag_objs/poll.obj", "flag_objs/green.obj", "flag_objs/yellow.obj", "flag_objs/red.obj",
                     "field_objs/back_field.obj", "field_objs/left.obj", "field_objs/right.obj",
                     "field_objs/front1.obj", "field_objs/front2.obj", "field_objs/poll_field.obj",
                     "road_objs/road_center.obj", "road_objs/zebra.obj", "road_objs/road_center_back.obj"
                     ]
        for i in range(70):
            self.indices_buffers.append(obj_loader.load_model(obj_files[i]))

        self.VAO = glGenVertexArrays(70)
        self.VBO = glGenBuffers(70)
        for i in range(70):
            glBindVertexArray(self.VAO[i])
            glBindBuffer(GL_ARRAY_BUFFER, self.VBO[i])
            glBufferData(GL_ARRAY_BUFFER, self.indices_buffers[i][1].nbytes, self.indices_buffers[i][1], GL_STATIC_DRAW)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.indices_buffers[i][1].itemsize * 8, ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.indices_buffers[i][1].itemsize * 8,
                                  ctypes.c_void_p(12))
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.indices_buffers[i][1].itemsize * 8,
                                  ctypes.c_void_p(20))
            glEnableVertexAttribArray(2)

    def loade_object_texture(self):
        texture_loader = Texture_loader()
        self.textures = glGenTextures(70)
        object_textures = ["fence_textures/fences.png", "field_textures/field.png",
                           "house_textures/wall.jpg", "house_textures/wall.jpg",
                           "house_textures/wall.jpg", "house_textures/wall.jpg",
                           "house_textures/wall.jpg", "house_textures/wall.jpg",
                           "house_textures/wall.jpg", "house_textures/door.jpg",
                           "house_textures/door.jpg", "house_textures/door.jpg",
                           "house_textures/door.jpg", "house_textures/door.jpg",
                           "house_textures/door.jpg", "house_textures/door.jpg",

                           "house_textures/window.jpg", "house_textures/window.jpg",
                           "house_textures/window.jpg", "house_textures/window.jpg",
                           "house_textures/window.jpg", "house_textures/window.jpg",
                           "house_textures/window.jpg", "house_textures/roof.jpg",
                           "house_textures/roof.jpg",
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

                           "tree_textures/branch.png", "tree_textures/branch.png",
                           "tree_textures/branch.png", "tree_textures/branch.png",
                           "tree_textures/branch.png", "tree_textures/branch.png",
                           "tree_textures/branch.png", "tree_textures/branch.png",
                           "tree_textures/branch.png", "tree_textures/branch.png",

                           "flag_textures/poll.png", "flag_textures/green.png",
                           "flag_textures/yellow.png", "flag_textures/red.png",
                           "field_textures/grass.jpg", "field_textures/grass.jpg",
                           "field_textures/grass.jpg", "field_textures/grass.jpg",
                           "field_textures/grass.jpg", "field_textures/grass.jpg",
                           "flag_textures/yellow.png", "road_textures/zebra.png",
                           "flag_textures/yellow.png"]
        for i in range(70):
            texture_loader.load_texture(object_textures[i], self.textures[i])

    def projection(self):
        shader = self.shader()
        glUseProgram(shader)
        glClearColor(0, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
        view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))
        self.model_loc = glGetUniformLocation(shader, "model")
        proj_loc = glGetUniformLocation(shader, "projection")
        view_loc = glGetUniformLocation(shader, "view")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    def draw(self, x_position=0, y_position=0, z_position=0, rotation=0.1):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        objects_indices = []
        for i in range(70):
            objects_indices.append(
                ([self.indices_buffers[i][0], pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -25]))]))
        for i in range(70):
            objects_indices[i][1] = pyrr.matrix44.create_from_translation(
                pyrr.Vector3([0 + x_position, -5 + y_position, -25 + z_position]))
        for i in range(70):
            rot_y = pyrr.Matrix44.from_y_rotation(0.01 * time.time() * rotation)
            model = pyrr.matrix44.multiply(rot_y, objects_indices[i][1])
            glBindVertexArray(self.VAO[i])
            glBindTexture(GL_TEXTURE_2D, self.textures[i])
            glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, model)
            glDrawArrays(GL_TRIANGLES, 0, len(objects_indices[i][0]))

    def init(self):
        pygame.init()
        display = (1020, 700)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        self.load_obj_file()
        self.loade_object_texture()
        self.projection()

    def main(self):
        self.init()
        z_position = 0
        x_position = 0
        y_position = 0
        rotation = 1
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
                y_position += 0.1
            elif keys_pressed[pygame.K_DOWN]:
                z_position -= 0.1
            elif keys_pressed[pygame.K_UP]:
                z_position += 0.1
            elif keys_pressed[pygame.K_l]:
                rotation -= 0.05
            elif keys_pressed[pygame.K_r]:
                rotation += 0.05
            self.draw(x_position, y_position, z_position, rotation)
            pygame.display.flip()
            pygame.time.wait(10)


object_drawer = ObjectDrawer()
object_drawer.main()

import glm
import pyglet
import pyshaders

vert = """#version 130

in vec3 vert;
in vec2 texCoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;

out vec2 TexCoords;

void main()
{
  TexCoords = texCoords;
  gl_Position =  proj * view * model * vec4(vert, 1);
}
"""

frag = """#version 130

in vec2 TexCoords;

out vec4 color_frag;

uniform sampler2D tex;
uniform sampler2D tex2;

void main()
{
  color_frag = texture(tex, TexCoords);
}
"""


def quad(x, y):
    return (
        x - 0.3, y - 0.3,
        x + 0.3, y - 0.3,
        x + 0.3, y + 0.3,
        x - 0.3, y + 0.3,
    )


def cube(x, y, z):
    return (
        -0.3, -0.3, -0.3,
        0.3, -0.3, -0.3,
        0.3,  0.3, -0.3,
        0.3,  0.3, -0.3,
        -0.3,  0.3, -0.3,
        -0.3, -0.3, -0.3,

        -0.3, -0.3,  0.3,
        0.3, -0.3,  0.3,
        0.3,  0.3,  0.3,
        0.3,  0.3,  0.3,
        -0.3,  0.3,  0.3,
        -0.3, -0.3,  0.3,

        -0.3,  0.3,  0.3,
        -0.3,  0.3, -0.3,
        -0.3, -0.3, -0.3,
        -0.3, -0.3, -0.3,
        -0.3, -0.3,  0.3,
        -0.3,  0.3,  0.3,

        0.3,  0.3,  0.3,
        0.3,  0.3, -0.3,
        0.3, -0.3, -0.3,
        0.3, -0.3, -0.3,
        0.3, -0.3,  0.3,
        0.3,  0.3,  0.3,

        -0.3, -0.3, -0.3,
        0.3, -0.3, -0.3,
        0.3, -0.3,  0.3,
        0.3, -0.3,  0.3,
        -0.3, -0.3,  0.3,
        -0.3, -0.3, -0.3,

        -0.3,  0.3, -0.3,
        0.3,  0.3, -0.3,
        0.3,  0.3,  0.3,
        0.3,  0.3,  0.3,
        -0.3,  0.3,  0.3,
        -0.3,  0.3, -0.3,
    )


def triangle(x, y):
    return (
        x - 0.2, y - 0.2,
        x + 0.2, y - 0.2,
        x, y + 0.2,
    )


RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
CYAN = (0, 1, 1)
PURPLE = (1, 0, 1)
YELLOW = (1, 1, 0)
WHITE = (1, 1, 1)


def start():
    window = pyglet.window.Window(resizable=True)
    pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)
    pyshaders.transpose_matrices(False)
    shader = pyshaders.from_string(vert, frag)
    shader.use()

    view = glm.lookAt(
        glm.vec3(1.2, 1.2, 1.2),
        glm.vec3(0, 0, 0),
        glm.vec3(0, 0, 1),
    )

    proj = glm.perspective(glm.radians(45), 800/600, 1, 10)

    pattern = pyglet.image.CheckerImagePattern()
    tex = pattern.create_image(64, 64).get_texture()
    textured = pyglet.graphics.TextureGroup(tex)

    batch = pyglet.graphics.Batch()

    batch.add(
        36, pyglet.gl.GL_TRIANGLES, textured,
        ("0g3f", cube(0, 0, 0)),
        ("1g2f", (0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 0) * 6)
    )

    t = 0

    def update(dt):
        nonlocal t
        m = glm.mat4(1)
        m = glm.rotate(m, t, (0, 0, 1))
        shader.uniforms.model = m
        shader.uniforms.view = view
        shader.uniforms.proj = proj

        t += dt

    pyglet.clock.schedule(update)

    @window.event()
    def on_draw():
        window.clear()
        batch.draw()


if __name__ == "__main__":
    start()
    pyglet.app.run()

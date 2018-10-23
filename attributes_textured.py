import pyglet
import pyshaders

vert = """#version 130

in vec2 vert;
in vec2 texCoords;

out vec2 TexCoords;

void main()
{
  TexCoords = texCoords;
  gl_Position = vec4(vert, 1, 1);
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
        x - 0.2, y - 0.2,
        x + 0.2, y - 0.2,
        x + 0.2, y + 0.2,
        x - 0.2, y + 0.2,
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
    shader = pyshaders.from_string(vert, frag)
    shader.use()

    pattern = pyglet.image.CheckerImagePattern((255, 0, 0, 255), (0, 0, 255, 255))
    tex = pattern.create_image(64, 64).get_texture()
    textured = pyglet.graphics.TextureGroup(tex)

    pattern2 = pyglet.image.CheckerImagePattern()
    tex2 = pattern2.create_image(64, 64).get_texture()
    textured2 = pyglet.graphics.TextureGroup(tex2)

    batch = pyglet.graphics.Batch()

    batch.add(
        4, pyglet.gl.GL_QUADS, textured,
        ("0g2f", quad(0.3, 0.4)),
        ("1g2f", (0, 0, 2, 0, 2, 2, 0, 2))
    )

    batch.add(
        4, pyglet.gl.GL_QUADS, textured2,
        ("0g2f", quad(-0.2, 0)),
        ("1g2f", (0, 0, 2, 0, 2, 2, 0, 2))
    )

    t = 0

    def update(dt):
        nonlocal t
        t += dt

    pyglet.clock.schedule(update)

    @window.event()
    def on_draw():
        window.clear()
        batch.draw()


if __name__ == "__main__":
    start()
    pyglet.app.run()

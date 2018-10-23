import pyglet
import pyshaders
import math

vert = """#version 130
in vec2 vert;
in vec3 color;

out vec3 fcolor;

void main()
{
  fcolor = color;
  gl_Position = vec4(vert, 1, 1);
}
"""

frag = """#version 130
out vec4 color_frag;
in vec3 fcolor;

void main()
{
  color_frag = vec4(fcolor, 1.0);
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

    batch = pyglet.graphics.Batch()

    batch.add(
        4, pyglet.gl.GL_QUADS, None,
        ("0g2f", quad(0.3, 0.4)),
        ("1g3f", RED + BLUE + GREEN + YELLOW)
    )

    batch.add(
        3, pyglet.gl.GL_TRIANGLES, None,
        ("0g2f", triangle(-0.2, 0)),
        ("1g3f", CYAN + YELLOW + PURPLE)
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

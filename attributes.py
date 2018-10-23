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


def triangle():
    return (-0.8, -0.8, 0.8, -0.8, 0, 0.8)


def start():
    window = pyglet.window.Window()
    shader = pyshaders.from_string(vert, frag)
    shader.use()

    tri = pyglet.graphics.vertex_list(
        3, ("0g2f", triangle()),
        ("1g3f", (1, 0, 0, 0, 1, 0, 0, 0, 1))
    )

    t = 0

    def update(dt):
        nonlocal t
        t += dt

    pyglet.clock.schedule(update)

    @window.event()
    def on_draw():
        window.clear()
        tri.draw(pyglet.gl.GL_TRIANGLES)


if __name__ == "__main__":
    start()
    pyglet.app.run()
